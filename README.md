[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua/)

# Denys Dovhan's Home Assistant Config

![Home](https://user-images.githubusercontent.com/3459374/152371766-1d2a1e17-34d3-4fe6-9e6d-aded02f14de1.png)

[![GitHub Workflow Status][github-img]][github-url]
[![Last Commit][last-commit-img]][github-url]
[![Commit Activity][commit-activity-img]][github-url]
[![License][license-img]][license-url]
[![GitHub Stars][stars-img]][github-url]
[![Twitter Followers][twitter-img]][twitter-url]

This is my personal Home Assistant configuration, awakening my home with automations. I hope this will help you inspire on the way to built your own smart home.

[**Read the documentation**](https://denysdovhan.com/smart-home)

I also have a [public Notion board](https://www.notion.so/denysdovhan/f09ea06da5db4cfa84d3ca50417b93b2?v=5fccab53c2fd4ac188ee0b92c2ca1cb9) with ideas and tasks for my smart home. You can follow and comment my plans there.

## Addons

I run Home Assistant OS with these addons:

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

## Automation

My home is awakened by these automations. You can browse them by categories. Links will guide you to the specific automation in `automations.yaml` file.

<!-- start-automations -->

1. [🚨 Alarm](#-alarm) (2 automation)
1. [🔔 Alert](#-alert) (9 automation)
1. [🌡️ Climate](#-climate) (8 automation)
1. [💡 Light](#-light) (6 automation)
1. [🎵 Media](#-media) (3 automation)
1. [🚦 Mode](#-mode) (4 automation)
1. [🔘 Presence](#-presence) (2 automation)
1. [🖥️ System](#-system) (7 automation)
1. [🧹 Vacuum](#-vacuum) (8 automation)
1. [💦 Water](#-water) (2 automation)

Total number of automations: **51**️

### 🚨 Alarm

- [Notification for Triggered](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L75) – Make an announcement when Alarm is getting triggered
- [Triggering Alarm](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L52)

### 🔔 Alert

- [Air Siren in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1) – Air Alert announcement when we are in Kyiv. Sends critical notifications and announces on speakers.
- [Bad Air Quality](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L354) – Notify when the air quality is bad
- [Car Washing](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L469) – Notify when it’s okay or not okay to wash a car
- [Denys is leaving the office](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2073) – Notify when Denys is leaving the office
- [HACS Releases](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L271) – Notify when new HACS components are released
- [Home Assistant Release](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L240) – Notify Denys about new Home Assistant releases
- [Home Assistant Start](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L308) – Notify Denys when Home Assistant starts
- [Humidifier No Water](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L443) – Notify when humidifier's water tank is empty
- [Snow/Winter Tires](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L519) – Notify when it's time to change car tires

### 🌡️ Climate

- [Preheat Balcony for a Workday](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L775) – When Denys wakes up, ask if he is going to work on balcony, start heating and notify when temperature is comfortable.
- [Suggest turning on AC when it's hot](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#LNone) – When temperature raises over certain level, send an actionable notification for turning on ACs
- [Switch Heaters during Heating Season](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L610) – Turn on/off heaters when Heating Season in on
- [Sync Bedroom TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L601)
- [Sync Living Room TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L592)
- [Turn off Balcony Heater](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L723) – Turn off Balcony Heater when the working display or desk lamp are off for some time
- [Turn on Balcony Heater](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L683) – Turn on Balcony Heater when it's cold and Desk Lamp or Working Display are turned on
- [Turn on Humidifier only during sleep time](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1821)

### 💡 Light

- [Presence Simulation in Away Mode](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1161) – Toggle Presence Simulation during Night in Away Mode
- [Toggle Desk Lamp with Working Display](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1076) – Sync Desk lamp with Working Display
- [Turn off Corridor Light When Door is Closed](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1000) – Turn off Corridor Light when Front Door closes. If the light is still on, then send a notification with an action to turn off the light.
- [Turn on Corridor Light when Door is open](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L977) – Turn on Corridor Light when Front Door opens and then turn it off after a few minutes
- [Turn on lights on Sunset](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L869) – Turn on lights when sun goes below the horizon
- [Turn on lights on low illuminance](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L918) – Turn on lights on low illuminance

### 🎵 Media

- [Turn off Samsung TV when PlayStation turns off](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L95) – Turn off Samsung TV when PS5 goes to sleep mode
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1990) – Turn on Apple TV when Samsung TV turns on and PS5 is off
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1990) – Turn on Apple TV when Samsung TV turns on and PS5 is off

### 🚦 Mode

- [Away Flow](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1127) – Toggle Away mode depending on the Away input boolean
- [Away on Leaving City](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1137) – Toggle Away mode depending on proximity to the Kyiv city
- [Do Not Disturb Activation](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1092) – Adjust devices to Do Not Disturb mode
- [Do Not Disturb on Focus](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1109) – Switch Do Not Disturb while camera, mic or focus are on

### 🔘 Presence

- [Everyone is Arriving](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1189) – Turn on things when people are arriving
- [Everyone is Leaving](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1269) – Turn off things when people are leaving

### 🖥️ System

- [Magic Cube Actions](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L118)
- [Notify about high CPU usage](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2108) – Send alert when HA has a high CPU usage
- [Notify about high RAM usage](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2139) – Notify when RAM usage is high for some time.
- [Notify when Media disk is full](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L328) – Notify when Media drive is 90% full for some time.
- [Notify when System disk is full](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2176) – Send a notification when system disk is 90% full.
- [Power Outage Recovery](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1763)
- [Run chores in config folder](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2061) – Run scripts for generating README, commiting regular updated, etc

### 🧹 Vacuum

- [Ask Regular Cleaning](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1341) – Regular vacuum cleaning every two days
- [Ask for Maintenance](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1480) – Send vacuum near trash bin and ask for maintenance
- [Clean Counting](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2044) – Count cleanings via counter
- [Error Alert](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1452) – Notify when error with vacuum occured
- [Finish Alert](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1419) – Notify when vacuum finished cleaning and we are not home.
- [Replacements Alert](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1544) – Notify when vacuum parts need to be replaced
- [Stop cleaning when we return home](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1401) – Send vacuum home when somebody comes home
- [iOS Actions](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1624) – Handle iOS actions for vacuum cleaner

### 💦 Water

- [Keep Water Heater turned On](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L2017) – When Water Heater was accidentally turned off, automatically turn in on
- [Notify when water is heated](https://github.com/denysdovhan/home-assistant-config/blob/a607f4151f0e739b78f5f908d8aaa354bd7760db/automations.yaml#L1695) – When we ask to let us know when the boiler has done heating, it should notify about that.
<!-- end-automations -->

## Custom Components

Here is a list of all custom components I use:

<!-- start-custom-components -->

- [Adaptive Lighting](https://github.com/basnijholt/adaptive-lighting#readme) v1.21.1
- [Car Wash](https://github.com/Limych/ha-car_wash) v1.5.5
- [HACS](https://hacs.xyz/docs/configuration/start) v1.34.0
- [Multiscrape scraping component](https://github.com/danieldotnl/ha-multiscrape) v7.0.0
- [Nova Poshta](https://github.com/krasnoukhov/homeassistant-nova-poshta) v1.1.0
- [Powercalc](https://github.com/bramstroker/homeassistant-powercalc) vv1.11.7
- [Presence Simulation](https://github.com/slashback100/presence_simulation) v4.5
- [Proxmox VE](https://github.com/dougiteixeira/proxmoxve) v3.4.1
- [Snowtire Sensor](https://github.com/Limych/ha-snowtire) v1.4.6
- [Thermal Comfort](https://github.com/dolezsa/thermal_comfort/blob/master/README.md) v2.2.2
- [Watchman](https://github.com/dummylabs/thewatchman) v0.5.1
<!-- end-custom-components -->

Custom components are managed by [HACS](https://hacs.xyz/).

## License

[MIT][license-url] © [Denys Dovhan][denysdovhan]

<!-- References -->

[github-url]: https://github.com/denysdovhan/home-assistant-config
[github-img]: https://img.shields.io/github/actions/workflow/status/denysdovhan/home-assistant-config/homeassistant.yml?style=flat-square
[last-commit-img]: https://img.shields.io/github/last-commit/denysdovhan/home-assistant-config?style=flat-square
[commit-activity-img]: https://img.shields.io/github/commit-activity/m/denysdovhan/home-assistant-config?style=flat-square
[license-url]: https://github.com/denysdovhan/home-assistant-config/blob/master/LICENSE
[license-img]: https://img.shields.io/github/license/denysdovhan/home-assistant-config?style=flat-square
[twitter-url]: https://twitter.com/denysdovhan
[twitter-img]: https://img.shields.io/twitter/follow/denysdovhan?label=Follow
[stars-img]: https://img.shields.io/github/stars/denysdovhan/home-assistant-config?style=social
[denysdovhan]: https://denysdovhan.com
