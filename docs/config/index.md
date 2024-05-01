# Configuration

## Addons

<!-- start-addons -->

- [Advanced SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) v17.2.0 – A supercharged SSH & Web Terminal access to your Home Assistant instance
- [File editor](https://github.com/home-assistant/addons/tree/master/configurator) v5.8.0 – Simple browser-based file editor for Home Assistant
- [ESPHome](https://esphome.io/) v2024.4.0 – ESPHome add-on for intelligently managing all your ESP8266/ESP32 devices
- [PS5 MQTT](https://github.com/FunkeyFlo/ps5-mqtt/tree/main/add-ons/ps5-mqtt) v1.3.3 – Control Sony PlayStation 5 devices via MQTT
- [AirCast](https://github.com/hassio-addons/addon-aircast) v4.2.1 – AirPlay capabilities for your Chromecast devices.
- [Home Assistant Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) v0.112.1 – Automatically manage backups between Home Assistant and Google Drive
- [Samba share](https://github.com/home-assistant/addons/tree/master/samba) v12.3.1 – Expose Home Assistant folders with SMB/CIFS
- [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) v6.4.0 – An Open Source MQTT broker
- [Zigbee2MQTT](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt) v1.36.1-1 – Use your ZigBee devices without the vendor's bridge or gateway
<!-- end-addons -->

## Automations

<!-- start-automations -->

1. [🚨 Alarm](#-alarm) (2 automation)
1. [🔔 Alert](#-alert) (11 automation)
1. [🌡️ Climate](#-climate) (8 automation)
1. [💡 Light](#-light) (6 automation)
1. [🎵 Media](#-media) (3 automation)
1. [🚦 Mode](#-mode) (4 automation)
1. [🔘 Presence](#-presence) (2 automation)
1. [🖥️ System](#-system) (7 automation)
1. [🧹 Vacuum](#-vacuum) (8 automation)
1. [💦 Water](#-water) (2 automation)

Total number of automations: **53**️

### 🚨 Alarm

- [Notification for Triggered](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L75) – Make an announcement when Alarm is getting triggered
- [Triggering Alarm](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L52)

### 🔔 Alert

- [Air Siren in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1) – Air Alert announcement when we are in Kyiv. Sends critical notifications and announces on speakers.
- [Bad Air Quality](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L364) – Notify when the air quality is bad
- [Car Washing](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L424) – Notify when it’s okay or not okay to wash a car
- [Danger in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2168) – Danger of missile/drone strike in Kyiv RIGHT NOW. Critical alert to hide immediately.
- [Denys is leaving the office](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2036) – Notify when Denys is leaving the office
- [HACS Releases](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L275) – Notify when new HACS components are released
- [Home Assistant Release](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L244) – Notify Denys about new Home Assistant releases
- [Home Assistant Start](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L318) – Notify Denys when Home Assistant starts
- [Humidifier No Water](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L398) – Notify when humidifier's water tank is empty
- [Imminent Attack by Strategic Bombers](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2250) – Send a notification when Tu-95 strategic bombers take off from Russian airfields. This means attack by cruise missiles is imminent. Prepare a hideout.
- [Snow/Winter Tires](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L474) – Notify when it's time to change car tires

### 🌡️ Climate

- [Preheat Balcony for a Workday](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L730) – When Denys wakes up, ask if he is going to work on balcony, start heating and notify when temperature is comfortable.
- [Suggest turning on AC when it's hot](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#LNone) – When temperature raises over certain level, send an actionable notification for turning on ACs
- [Switch Heaters during Heating Season](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L565) – Turn on/off heaters when Heating Season in on
- [Sync Bedroom TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L556)
- [Sync Living Room TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L547)
- [Turn off Balcony Heater](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L678) – Turn off Balcony Heater when the working display or desk lamp are off for some time
- [Turn on Balcony Heater](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L638) – Turn on Balcony Heater when it's cold and Desk Lamp or Working Display are turned on
- [Turn on Humidifier only during sleep time](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1776)

### 💡 Light

- [Presence Simulation in Away Mode](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1116) – Toggle Presence Simulation during Night in Away Mode
- [Toggle Desk Lamp with Working Display](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1031) – Sync Desk lamp with Working Display
- [Turn off Corridor Light When Door is Closed](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L955) – Turn off Corridor Light when Front Door closes. If the light is still on, then send a notification with an action to turn off the light.
- [Turn on Corridor Light when Door is open](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L932) – Turn on Corridor Light when Front Door opens and then turn it off after a few minutes
- [Turn on lights on Sunset](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L824) – Turn on lights when sun goes below the horizon
- [Turn on lights on low illuminance](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L873) – Turn on lights on low illuminance

### 🎵 Media

- [Turn off Samsung TV when PlayStation turns off](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L95) – Turn off Samsung TV when PS5 goes to sleep mode
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1945) – Turn on Apple TV when Samsung TV turns on and PS5 is off
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1945) – Turn on Apple TV when Samsung TV turns on and PS5 is off

### 🚦 Mode

- [Away Flow](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1082) – Toggle Away mode depending on the Away input boolean
- [Away on Leaving City](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1092) – Toggle Away mode depending on proximity to the Kyiv city
- [Do Not Disturb Activation](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1047) – Adjust devices to Do Not Disturb mode
- [Do Not Disturb on Focus](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1064) – Switch Do Not Disturb while camera, mic or focus are on

### 🔘 Presence

- [Everyone is Arriving](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1144) – Turn on things when people are arriving
- [Everyone is Leaving](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1224) – Turn off things when people are leaving

### 🖥️ System

- [Magic Cube Actions](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L122)
- [Notify about high CPU usage](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2070) – Send alert when HA has a high CPU usage
- [Notify about high RAM usage](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2101) – Notify when RAM usage is high for some time.
- [Notify when Media disk is full](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L338) – Notify when Media drive is 90% full for some time.
- [Notify when System disk is full](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2138) – Send a notification when system disk is 90% full.
- [Power Outage Recovery](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1718)
- [Run chores in config folder](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2024) – Run scripts for generating README, commiting regular updated, etc

### 🧹 Vacuum

- [Ask Regular Cleaning](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1296) – Regular vacuum cleaning every two days
- [Ask for Maintenance](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1435) – Send vacuum near trash bin and ask for maintenance
- [Clean Counting](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2007) – Count cleanings via counter
- [Error Alert](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1407) – Notify when error with vacuum occured
- [Finish Alert](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1374) – Notify when vacuum finished cleaning and we are not home.
- [Replacements Alert](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1499) – Notify when vacuum parts need to be replaced
- [Stop cleaning when we return home](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1356) – Send vacuum home when somebody comes home
- [iOS Actions](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1579) – Handle iOS actions for vacuum cleaner

### 💦 Water

- [Keep Water Heater turned On](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1980) – When Water Heater was accidentally turned off, automatically turn in on
- [Notify when water is heated](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1650) – When we ask to let us know when the boiler has done heating, it should notify about that.
<!-- end-automations -->