"""Utilities for auto discovery of light models."""

from __future__ import annotations

import logging
import os
import re
from typing import NamedTuple, Optional

import homeassistant.helpers.device_registry as dr
import homeassistant.helpers.entity_registry as er
from awesomeversion.awesomeversion import AwesomeVersion
from homeassistant.const import __version__ as HA_VERSION
from homeassistant.helpers.typing import HomeAssistantType

from .const import (
    CONF_CUSTOM_MODEL_DIRECTORY,
    CONF_MANUFACTURER,
    CONF_MODEL,
    MANUFACTURER_ALIASES,
)
from .errors import ModelNotSupported
from .light_model import LightModel

_LOGGER = logging.getLogger(__name__)


async def get_light_model(
    hass: HomeAssistantType,
    config: dict,
    entity_entry: Optional[er.RegistryEntry] = None,
) -> Optional[LightModel]:
    manufacturer = config.get(CONF_MANUFACTURER)
    model = config.get(CONF_MODEL)
    if (manufacturer is None or model is None) and entity_entry:
        model_info = await autodiscover_model(hass, entity_entry)
        if model_info:
            manufacturer = config.get(CONF_MANUFACTURER) or model_info.manufacturer
            model = config.get(CONF_MODEL) or model_info.model

    if manufacturer is None or model is None:
        return None

    custom_model_directory = config.get(CONF_CUSTOM_MODEL_DIRECTORY)
    if custom_model_directory:
        custom_model_directory = os.path.join(
            hass.config.config_dir, custom_model_directory
        )

    return LightModel(hass, manufacturer, model, custom_model_directory)


async def is_supported_model(
    hass: HomeAssistantType, entry: er.RegistryEntry, sensor_config: dict = {}
) -> bool:
    try:
        await get_light_model(hass, sensor_config, entry)
        return True
    except ModelNotSupported:
        return False


async def autodiscover_model(
    hass: HomeAssistantType, entity_entry: er.RegistryEntry
) -> Optional[ModelInfo]:
    """Try to auto discover manufacturer and model from the known device information"""

    if not await is_supported_for_autodiscovery(hass, entity_entry):
        _LOGGER.error(
            "%s: Cannot autodiscover model, manufacturer or model unknown from device registry",
            entity_entry.entity_id,
        )
        return None

    device_registry = await dr.async_get_registry(hass)
    device_entry = device_registry.async_get(entity_entry.device_id)
    model_id = device_entry.model
    match = re.search("\((.*)\)$", device_entry.model)
    if match:
        model_id = match.group(1)

    manufacturer = device_entry.manufacturer
    if MANUFACTURER_ALIASES.get(manufacturer):
        manufacturer = MANUFACTURER_ALIASES.get(manufacturer)

    model_info = ModelInfo(manufacturer, model_id)

    # This check can be removed in future version
    if (
        AwesomeVersion(HA_VERSION) <= AwesomeVersion("2021.11")
        and match is None
        and entity_entry.platform == "hue"
    ):
        model_info = await autodiscover_from_hue_bridge(hass, entity_entry)
        if model_info is None:
            return None

    _LOGGER.debug(
        "%s: Auto discovered model (manufacturer=%s, model=%s)",
        entity_entry.entity_id,
        model_info.manufacturer,
        model_info.model,
    )
    return model_info


async def is_supported_for_autodiscovery(
    hass: HomeAssistantType, entity_entry: er.RegistryEntry | None
):
    """See if we have enough information in device registry to automatically setup the power sensor"""

    if entity_entry is None:
        return False

    device_registry = await dr.async_get_registry(hass)
    device_entry = device_registry.async_get(entity_entry.device_id)
    if device_entry is None:
        return False

    if device_entry.manufacturer is None or device_entry.model is None:
        return False

    return True


async def autodiscover_from_hue_bridge(
    hass: HomeAssistantType, entity_entry: er.RegistryEntry
):
    # Code below is for BC purposes. Will be removed in a future version
    light = await find_hue_light(hass, entity_entry)
    if light is None:
        _LOGGER.error(
            "%s: Cannot autodiscover model, not found in the hue bridge api",
            entity_entry.entity_id,
        )
        return None

    return ModelInfo(light.manufacturername, light.modelid)


async def find_hue_light(hass: HomeAssistantType, entity_entry: er.RegistryEntry):
    """Find the light in the Hue bridge, we need to extract the model id."""

    if not hass.data.get("hue"):
        return None

    bridge = hass.data["hue"][entity_entry.config_entry_id]
    lights = bridge.api.lights
    for light_id in lights:
        light = bridge.api.lights[light_id]
        if light.uniqueid == entity_entry.unique_id:
            return light

    return None


class ModelInfo(NamedTuple):
    manufacturer: str
    model: str
