from __future__ import annotations

import inspect
import logging
from typing import Union

from homeassistant.components.utility_meter.const import (
    CONF_METER_NET_CONSUMPTION,
    CONF_METER_TYPE,
    CONF_SOURCE_SENSOR,
    CONF_TARIFFS,
    DATA_TARIFF_SENSORS,
    DATA_UTILITY,
)
from homeassistant.components.utility_meter.sensor import UtilityMeterSensor
from homeassistant.const import __short_version__
from homeassistant.helpers.typing import HomeAssistantType

from custom_components.powercalc.const import (
    CONF_CREATE_UTILITY_METERS,
    CONF_UTILITY_METER_OFFSET,
    CONF_UTILITY_METER_TYPES,
)
from custom_components.powercalc.migrate import async_set_unique_id
from custom_components.powercalc.sensors.energy import (
    DailyEnergySensor,
    VirtualEnergySensor,
)
from custom_components.powercalc.sensors.group import GroupedEnergySensor

_LOGGER = logging.getLogger(__name__)


async def create_utility_meters(
    hass: HomeAssistantType,
    energy_sensor: Union[VirtualEnergySensor, GroupedEnergySensor, DailyEnergySensor],
    sensor_config: dict,
) -> list[UtilityMeterSensor]:
    """Create the utility meters"""
    utility_meters = []

    if not sensor_config.get(CONF_CREATE_UTILITY_METERS):
        return []

    meter_types = sensor_config.get(CONF_UTILITY_METER_TYPES)
    for meter_type in meter_types:
        name = f"{energy_sensor.name} {meter_type}"
        entity_id = f"{energy_sensor.entity_id}_{meter_type}"
        _LOGGER.debug("Creating utility_meter sensor: %s", name)

        if not DATA_UTILITY in hass.data:
            hass.data[DATA_UTILITY] = {}
        hass.data[DATA_UTILITY][entity_id] = {
            CONF_SOURCE_SENSOR: energy_sensor.entity_id,
            CONF_METER_TYPE: meter_type,
            CONF_TARIFFS: [],
            CONF_METER_NET_CONSUMPTION: False,
        }

        params = {
            "source_entity": energy_sensor.entity_id,
            "name": name,
            "meter_type": meter_type,
            "meter_offset": sensor_config.get(CONF_UTILITY_METER_OFFSET),
            "net_consumption": False,
        }

        signature = inspect.signature(UtilityMeterSensor.__init__)
        if "parent_meter" in signature.parameters:
            params["parent_meter"] = entity_id
        if "delta_values" in signature.parameters:
            params["delta_values"] = False

        utility_meter = VirtualUtilityMeter(**params)

        if energy_sensor.unique_id:
            unique_id = f"{energy_sensor.unique_id}_{meter_type}"
            # Set new unique id if this entity already exists in the entity registry
            async_set_unique_id(hass, entity_id, unique_id)
            utility_meter.unique_id = unique_id

        hass.data[DATA_UTILITY][entity_id][DATA_TARIFF_SENSORS] = [utility_meter]
        utility_meters.append(utility_meter)

    return utility_meters


class VirtualUtilityMeter(UtilityMeterSensor):
    @property
    def unique_id(self):
        """Return the name of the group."""
        return self._attr_unique_id

    @unique_id.setter
    def unique_id(self, value):
        """Set last changed datetime."""
        self._attr_unique_id = value
