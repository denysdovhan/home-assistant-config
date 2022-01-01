"""Component to integrate with presence_simulation."""

import logging
import time
import asyncio
import json
import pytz
from datetime import datetime,timedelta,timezone
from homeassistant.components.recorder.history import get_significant_states
import homeassistant.util.dt as dt_util
from homeassistant.const import EVENT_HOMEASSISTANT_START
from homeassistant.components.recorder.models import States
from homeassistant.components.recorder.const import DATA_INSTANCE
from .const import (
        DOMAIN,
        SWITCH_PLATFORM,
        SWITCH,
        RESTORE_SCENE,
        SCENE_PLATFORM
)
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry):
    """Set up this component using config flow."""
    _LOGGER.debug("async setup entry %s", entry.data["entities"])
    unsub = entry.add_update_listener(update_listener)

    # Use `hass.async_create_task` to avoid a circular dependency between the platform and the component
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, SWITCH_PLATFORM))
    if 'interval' in entry.data:
        interval = entry.data['interval']
    else:
        interval = 30
    if 'restore' in entry.data:
        restore = entry.data['restore']
    else:
        restore = False
    return await async_mysetup(hass, [entry.data["entities"]], entry.data["delta"], interval, restore)

async def async_setup(hass, config):
    """Set up this component using YAML."""
    if config.get(DOMAIN) is None:
        # We get here if the integration is set up using config flow
        return True
    return await async_mysetup(hass, config[DOMAIN].get("entity_id",[]), config[DOMAIN].get('delta', "7"), config[DOMAIN].get('interval', '30'), config[DOMAIN].get('restore', False))


async def async_mysetup(hass, entities, deltaStr, refreshInterval, restoreParam):
    """Set up this component (YAML or UI)."""
    #delta is the size in days of the historic to get from the DB
    delta = int(deltaStr)
    #interval is the number of seconds the component will wait before checking if the entity need to be switch
    interval = int(refreshInterval)
    restoreAfterStop = restoreParam
    _LOGGER.debug("Config: Entities for presence simulation: %s", entities)
    _LOGGER.debug("Config: Cycle of %s days", delta)
    _LOGGER.debug("Config: Scan interval of %s seconds", interval)
    _LOGGER.debug("Config: Restore state: %s", restoreAfterStop)
    _LOGGER.debug("Config: Timezone that will be used to display datetime: %s", hass.config.time_zone)

    async def stop_presence_simulation(err=None, restart=False):
        """Stop the presence simulation, raising a potential error"""
        #get the switch entity
        entity = hass.data[DOMAIN][SWITCH_PLATFORM][SWITCH]
        #set the state of the switch to off. Not calling turn_off to avoid calling the stop service again
        entity.internal_turn_off()
        if not restart:
            #empty the start_datetime  attribute
            await entity.reset_start_datetime()
            await entity.reset_entities()
            await entity.reset_delta()
            # if the scene exist, turn it on
            # TODO check to improve, won't work if you launch one time is the restore state and then after without it.
            #Can not just take restoreAfterStop cause if it is overriden in the service call, restoreAfterStop is not update
            _LOGGER.debug("entity.restore_states %s", await entity.restore_states())
            scene = hass.states.get(SCENE_PLATFORM+"."+RESTORE_SCENE)
            if scene is not None and await entity.restore_states():
                service_data = {}
                service_data["entity_id"] = SCENE_PLATFORM+"."+RESTORE_SCENE
                _LOGGER.debug("Restoring scene after the simulation")
                try:
                    await hass.services.async_call("scene", "turn_on", service_data, blocking=False)
                except Exception as e:
                    _LOGGER.error("Error when restoring the scene after the simulation")
                    pass
            await entity.reset_restore_states()
        if err is not None:
            _LOGGER.debug("Error in presence simulation, exiting")
            raise e

    async def handle_stop_presence_simulation(call, restart=False):
        """Stop the presence simulation"""
        _LOGGER.debug("Stopped presence simulation")
        await stop_presence_simulation(restart=restart)

    async def async_expand_entities(entities):
        """If the entity is a group, return the list of the entities within, otherwise, return the entity"""
        entities_new = []
        for entity in entities:
            #to make it asyncable, not sure it is needed
            await asyncio.sleep(0)
            if hass.states.get(entity) is None:
                _LOGGER.error("Error when trying to identify entity %s, it seems it doesn't exist", entity)
                raise Exception("Entity is not known by HA, see log for more details")
            else:
                if 'entity_id' in  hass.states.get(entity).attributes:
                    #get the list of the associated entities
                    #the entity_id attribute will be filled for groups or light groups
                    group_entities = hass.states.get(entity).attributes["entity_id"]
                    #and call recursively, in case a group contains a group
                    group_entities_expanded = await async_expand_entities(group_entities)
                    _LOGGER.debug("State %s", group_entities_expanded)
                    entities_new += group_entities_expanded
                else:
                    _LOGGER.debug("Entity %s has no attribute entity_id, it is not a group nor a light group", entity)
                    entities_new.append(entity)
        return entities_new

    async def handle_presence_simulation(call, restart=False, entities_after_restart=None, delta_after_restart=None):
        """Start the presence simulation"""
        if call is not None: #if we are here, it is a call of the service, or a restart at the end of a cycle
            if isinstance(call.data.get("entity_id", entities), list):
                overridden_entities = call.data.get("entity_id", entities)
            else:
                overridden_entities = [call.data.get("entity_id", entities)]
            overridden_delta = call.data.get("delta", delta)
            overridden_restore = call.data.get("restore_states", restoreAfterStop)
        else: #if we are it is a call from the toggle service or from the turn_on action of the switch entity
              # or this is a restart and the simulation was launched after a restart of HA
            if entities_after_restart is not None:
                overridden_entities = entities_after_restart
            else:
                overridden_entities = entities
            if delta_after_restart is not None:
                overridden_delta = delta_after_restart
            else:
                overridden_delta = delta
            overridden_restore = restoreAfterStop

        #get the switch entity
        entity = hass.data[DOMAIN][SWITCH_PLATFORM][SWITCH]
        _LOGGER.debug("Is already running ? %s", entity.state)
        if is_running():
            _LOGGER.warning("Presence simulation already running. Doing nothing")
            return
        running = True
        #turn on the switch. Not calling turn_on() to avoid calling the start service again
        entity.internal_turn_on()
        _LOGGER.debug("setting restore states %s", overridden_restore)
        await entity.set_restore_states(overridden_restore)
        _LOGGER.debug("Presence simulation started")

        current_date = datetime.now(timezone.utc)
        #compute the start date that will be used in the query to get the historic of the entities
        minus_delta = current_date + timedelta(-overridden_delta)
        #expand the entitiies, meaning replace the groups with the entities in it
        try:
            expanded_entities = await async_expand_entities(overridden_entities)
        except Exception as e:
            _LOGGER.error("Error during identifing entities")
            running = False
            entity.internal_turn_off()
            return

        if not restart:
            #set attribute on the switch
            try:
                await entity.set_start_datetime(datetime.now(hass.config.time_zone))
            except Exception as e:
                try:
                    await entity.set_start_datetime(datetime.now(pytz.timezone(hass.config.time_zone)))
                except Exception as e:
                    _LOGGER.warning("Start datetime could not be set to HA timezone: ", e)
                    await entity.set_start_datetime(datetime.now())
            if overridden_restore:
                service_data = {}
                service_data["scene_id"] = RESTORE_SCENE
                service_data["snapshot_entities"] = expanded_entities
                _LOGGER.debug("Saving scene before launching the simulation")
                try:
                    await hass.services.async_call("scene", "create", service_data, blocking=True)
                except Exception as e:
                    _LOGGER.error("Scene could not be created, continue without the restore functionality: %s", e)

        await entity.set_entities(expanded_entities)
        await entity.set_delta(overridden_delta)
        _LOGGER.debug("Getting the historic from %s for %s", minus_delta, expanded_entities)
        dic = get_significant_states(hass=hass, start_time=minus_delta, entity_ids=expanded_entities, significant_changes_only=False)
        _LOGGER.debug("history: %s", dic)
        for entity_id in dic:
            _LOGGER.debug('Entity %s', entity_id)
            #launch an async task by entity_id
            hass.async_create_task(simulate_single_entity(entity_id, dic[entity_id]))

        #launch an async task that will restart the simulation after the delay has passed
        hass.async_create_task(restart_presence_simulation(call, entities_after_restart=entities_after_restart, delta_after_restart=delta_after_restart))
        _LOGGER.debug("All async tasks launched")

    async def handle_toggle_presence_simulation(call):
        """Toggle the presence simulation"""
        if is_running():
            await handle_stop_presence_simulation(call, restart=False)
        else:
            await handle_presence_simulation(call, restart=False)


    async def restart_presence_simulation(call, entities_after_restart=None, delta_after_restart=None):
        """Make sure that once _delta_ days is passed, relaunch the presence simulation for another _delta_ days"""
        if call is not None: #if we are here, it is a call of the service, or a restart at the end of a cycle
            overridden_delta = call.data.get("delta", delta)
        else:
            if delta_after_restart is None:
                overridden_delta = delta
            else:
                overridden_delta = delta_after_restart
        _LOGGER.debug("Presence simulation will be relaunched in %i days", overridden_delta)
        #compute the moment the presence simulation will have to be restarted
        start_plus_delta = datetime.now(timezone.utc) + timedelta(overridden_delta)
        while is_running():
            #sleep until the 'delay' is passed
            await asyncio.sleep(interval)
            now = datetime.now(timezone.utc)
            if now > start_plus_delta:
                break

        if is_running():
            _LOGGER.debug("%s has passed, presence simulation is relaunched", overridden_delta)
            #Call to stop needed to avoid the start to do nothing since already running
            await handle_stop_presence_simulation(call, restart=True)
            await handle_presence_simulation(call, restart=True, entities_after_restart=entities_after_restart, delta_after_restart=delta_after_restart)

    async def simulate_single_entity(entity_id, hist):
        """This method will replay the historic of one entity received in parameter"""
        _LOGGER.debug("Simulate one entity: %s", entity_id)
        for state in hist: #hypothsis: states are ordered chronologically
            _LOGGER.debug("State %s", state.as_dict())
            _LOGGER.debug("Switch of %s foreseen at %s", entity_id, state.last_updated+timedelta(delta))
            #get the switch entity
            entity = hass.data[DOMAIN][SWITCH_PLATFORM][SWITCH]
            await entity.async_add_next_event(state.last_updated+timedelta(delta), entity_id, state.state)

            #a while with sleeps of _interval_ seconds is used here instead of a big sleep to check regulary the is_running() parameter
            #and therefore stop the task as soon as the service has been stopped
            while is_running():
                minus_delta = datetime.now(timezone.utc) + timedelta(-delta)
                if state.last_updated <= minus_delta:
                    break
                #sleep as long as the event is not in the past
                await asyncio.sleep(interval)
            if not is_running():
                return # exit if state is false
            #call service to turn on/off the light
            await update_entity(entity_id, state)
            #and remove this event from the attribute list of the switch entity
            await entity.async_remove_event(entity_id)

    async def update_entity(entity_id, state):
        """ Switch the entity """
        # use service scene.apply ?? https://www.home-assistant.io/integrations/scene/
        """
        service_data = {}
        service_data[entity_id]["state"] = state.state
        if "brightness" in state.attributes:
            service_data[entity_id]["bigthness"] = state.attributes["brigthness"]
        if "rgb_color" in state.attributes:
            service_data[entity_id]["rgb_color"] = state.attributes["rgb_color"]
        if "current_position" in state.attributes:
            service_data[entity_id]["position"] = state.attributes["position"]
        if "current_tilt_position" in state.attributes:
            service_data[entity_id]["tilt_position"] = state.attributes["tilt_position"]
        service_data = {"entities": service_data}
        await hass.services.async_call("scene", "apply", service_data, blocking=False)
        """
        # get the domain of the entity
        domain = entity_id.split('.')[0]
        #prepare the data of the services
        service_data = {"entity_id": entity_id}
        if domain == "light":
            #if it is a light, checking the brigthness & color
            _LOGGER.debug("Switching light %s to %s", entity_id, state.state)
            if "brightness" in state.attributes:
                _LOGGER.debug("Got attribute brightness: %s", state.attributes["brightness"])
                service_data["brightness"] = state.attributes["brightness"]
            if "rgb_color" in state.attributes:
                service_data["rgb_color"] = state.attributes["rgb_color"]
            if state.state == "on" or state.state == "off":
                await hass.services.async_call("light", "turn_"+state.state, service_data, blocking=False)
            else:
                _LOGGER.debug("State in neither on nor off (is %s), do nothing", state.state)

        elif domain == "cover":
            #if it is a cover, checking the position
            _LOGGER.debug("Switching Cover %s to %s", entity_id, state.state)
            if "current_tilt_position" in state.attributes:
                #Blocking open/close service if the tilt need to be called at the end
                blocking = True
            else:
                blocking = False
            if state.state == "closed":
                _LOGGER.debug("Closing cover %s", entity_id)
                await hass.services.async_call("cover", "close_cover", service_data, blocking=blocking)
            elif state.state == "open":
                if "current_position" in state.attributes:
                    service_data["position"] = state.attributes["current_position"]
                    _LOGGER.debug("Changing cover %s position to %s", entity_id, state.attributes["current_position"])
                    await hass.services.async_call("cover", "set_cover_position", service_data, blocking=blocking)
                    del service_data["position"]
                else: #no position info, just open it
                    _LOGGER.debug("Opening cover %s", entity_id)
                    await hass.services.async_call("cover", "open_cover", service_data, blocking=blocking)
            if state.state in ["closed", "open"]: #nothing to do if closing or opening. Wait for the status to be 'stabilized'
                if "current_tilt_position" in state.attributes:
                    service_data["tilt_position"] = state.attributes["current_tilt_position"]
                    _LOGGER.debug("Changing cover %s tilt position to %s", entity_id, state.attributes["current_tilt_position"])
                    await hass.services.async_call("cover", "set_cover_tilt_position", service_data, blocking=False)
                    del service_data["tilt_position"]
        else:
            _LOGGER.debug("Switching entity %s to %s", entity_id, state.state)
            if state.state == "on" or state.state == "off":
                await hass.services.async_call("homeassistant", "turn_"+state.state, service_data, blocking=False)
            else:
                _LOGGER.debug("State in neither on nor off (is %s), do nothing", state.state)

    def is_running():
        """Returns true if the simulation is running"""
        entity = hass.data[DOMAIN][SWITCH_PLATFORM][SWITCH]
        return entity.is_on

    async def restore_state(call):
        """Restore states."""
        _LOGGER.debug("Restoring states after HA start")
        """ retrieve the last status after last shutdown and restore it """
        entity = hass.data[DOMAIN][SWITCH_PLATFORM][SWITCH]
        session = hass.data[DATA_INSTANCE].get_session()
        result = session.query(States.state, States.attributes).filter(States.entity_id == SWITCH_PLATFORM+"."+SWITCH).order_by(States.last_changed.desc()).limit(1)
        if result.count() > 0 and result[0][0] == "on":
          _LOGGER.debug("Simulation was on before last shutdown, restarting it")
          previous_attribute = json.loads(result[0][1])
          _LOGGER.debug("attributes entity_id: %s", previous_attribute["entity_id"])
          if 'delta' in previous_attribute:
            delta_after_restart=previous_attribute['delta']
          else:
            delta
          # do not try to restore the previous state after the restart cause the scene has been lost during the restart
          #if 'restore_states' in previous_attribute:
          #  await entity.set_restore_states(previous_attribute['restore_states'])
          await handle_presence_simulation(call=None, entities_after_restart=previous_attribute["entity_id"], delta_after_restart=delta_after_restart)

    hass.services.async_register(DOMAIN, "start", handle_presence_simulation)
    hass.services.async_register(DOMAIN, "stop", handle_stop_presence_simulation)
    hass.services.async_register(DOMAIN, "toggle", handle_toggle_presence_simulation)
    hass.bus.async_listen_once(EVENT_HOMEASSISTANT_START, restore_state)

    return True

async def update_listener(hass, entry):
    """Update listener after an update in the UI"""
    _LOGGER.debug("Updating listener");
    # The OptionsFlow saves data to options.
    if len(entry.options) > 0:
        entry.data = entry.options
        entry.options = {}
        await async_mysetup(hass, [entry.data["entities"]], entry.data["delta"], entry.data["interval"], entry.data["restore"])
