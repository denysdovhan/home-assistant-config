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

running these addons

<!-- start-addons -->

- [Advanced SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) v17.2.0 – A supercharged SSH & Web Terminal access to your Home Assistant instance
- [File editor](https://github.com/home-assistant/addons/tree/master/configurator) v5.8.0 – Simple browser-based file editor for Home Assistant
- [ESPHome](https://esphome.io/) v2024.3.2 – ESPHome add-on for intelligently managing all your ESP8266/ESP32 devices
- [PS5 MQTT](https://github.com/FunkeyFlo/ps5-mqtt/tree/main/add-ons/ps5-mqtt) v1.3.3 – Control Sony PlayStation 5 devices via MQTT
- [AirCast](https://github.com/hassio-addons/addon-aircast) v4.2.1 – AirPlay capabilities for your Chromecast devices.
- [Home Assistant Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) v0.112.1 – Automatically manage backups between Home Assistant and Google Drive
- [Samba share](https://github.com/home-assistant/addons/tree/master/samba) v12.3.1 – Expose Home Assistant folders with SMB/CIFS
- [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) v6.4.0 – An Open Source MQTT broker
- [Zigbee2MQTT](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt) v1.36.1-1 – Use your ZigBee devices without the vendor's bridge or gateway
<!-- end-addons -->

## Automation

<!-- start-automations -->

1. [🚨 Alarm](#-alarm) (2 automation)
1. [🔔 Alert](#-alert) (11 automation)
1. [🌡️ Climate](#-climate) (8 automation)
1. [⚡️ Energy](#-energy) (1 automation)
1. [💡 Light](#-light) (6 automation)
1. [🎵 Media](#-media) (3 automation)
1. [🚦 Mode](#-mode) (4 automation)
1. [🔘 Presence](#-presence) (2 automation)
1. [🖥️ System](#-system) (3 automation)
1. [🧹 Vacuum](#-vacuum) (8 automation)
1. [💦 Water](#-water) (1 automation)

Total number of automations: **49**️

### 🚨 Alarm

- [Notification for Triggered](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L76) – Make an announcement when Alarm is getting triggered
- [Triggering Alarm](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L53)

### 🔔 Alert

- [Air Siren in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L2) – Air Alert announcement when we are in Kyiv. Sends critical notifications and announces on speakers.
- [Bad Air Quality](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L402) – Notify when the air quality is bad
- [Car Washing](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L517) – Notify when it’s okay or not okay to wash a car
- [HACS Releases](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L272) – Notify when new HACS components are released
- [Home Assistant Release](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L241) – Notify Denys about new Home Assistant releases
- [Home Assistant Start](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L309) – Notify Denys when Home Assistant starts
- [Humidifier No Water](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L491) – Notify when humidifier's water tank is empty
- [Monthly Energy Usage](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L640) – Switch energy tariff and notify about the consumption
- [Snow/Winter Tires](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L567) – Notify when it's time to change car tires
- [System Peaks ](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L329) – Alerts for high server usage, overloading, overheating, disk space
- [Water is Heated](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1854) – When we ask to let us know when the boiler has done heating, it should notify about that.

### 🌡️ Climate

- [Preheat Balcony for a Workday](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L934) – When Denys wakes up, ask if he is going to work on balcony, start heating and notify when temperature is comfortable.
- [Suggest turning on AC when it's hot](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#LNone) – When temperature raises over certain level, send an actionable notification for turning on ACs
- [Switch Heaters during Heating Season](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L769) – Turn on/off heaters when Heating Season in on
- [Sync Bedroom TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L760)
- [Sync Living Room TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L751)
- [Turn off Balcony Heater](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L882) – Turn off Balcony Heater when the working display or desk lamp are off for some time
- [Turn on Balcony Heater](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L842) – Turn on Balcony Heater when it's cold and Desk Lamp or Working Display are turned on
- [Turn on Humidifier only during sleep time](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1980)

### ⚡️ Energy

- [Electricity Meter](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L680) – Switch tarrifs for energy utility meter

### 💡 Light

- [Presence Simulation in Away Mode](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1320) – Toggle Presence Simulation during Night in Away Mode
- [Toggle Desk Lamp with Working Display](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1235) – Sync Desk lamp with Working Display
- [Turn off Corridor Light When Door is Closed](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1159) – Turn off Corridor Light when Front Door closes. If the light is still on, then send a notification with an action to turn off the light.
- [Turn on Corridor Light when Door is open](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1136) – Turn on Corridor Light when Front Door opens and then turn it off after a few minutes
- [Turn on lights on Sunset](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1028) – Turn on lights when sun goes below the horizon
- [Turn on lights on low illuminance](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1077) – Turn on lights on low illuminance

### 🎵 Media

- [Turn off Samsung TV when PlayStation turns off](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L96) – Turn off Samsung TV when PS5 goes to sleep mode
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L2149) – Turn on Apple TV when Samsung TV turns on and PS5 is off
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L2149) – Turn on Apple TV when Samsung TV turns on and PS5 is off

### 🚦 Mode

- [Away Flow](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1286) – Toggle Away mode depending on the Away input boolean
- [Away on Leaving City](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1296) – Toggle Away mode depending on proximity to the Kyiv city
- [Do Not Disturb Activation](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1251) – Adjust devices to Do Not Disturb mode
- [Do Not Disturb on Focus](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1268) – Switch Do Not Disturb while camera, mic or focus are on

### 🔘 Presence

- [Everyone is Arriving](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1348) – Turn on things when people are arriving
- [Everyone is Leaving](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1428) – Turn off things when people are leaving

### 🖥️ System

- [Magic Cube Actions](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L119)
- [Power Outage Recovery](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1922)
- [Run chores in /config folder](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L2220) – Run scripts for generating README, commiting regular updated, etc

### 🧹 Vacuum

- [Ask Regular Cleaning](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1500) – Regular vacuum cleaning every two days
- [Ask for Maintenance](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1639) – Send vacuum near trash bin and ask for maintenance
- [Clean Counting](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L2203) – Count cleanings via counter
- [Error Alert](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1611) – Notify when error with vacuum occured
- [Finish Alert](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1578) – Notify when vacuum finished cleaning and we are not home.
- [Replacements Alert](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1703) – Notify when vacuum parts need to be replaced
- [Stop cleaning when we return home](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1560) – Send vacuum home when somebody comes home
- [iOS Actions](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L1783) – Handle iOS actions for vacuum cleaner

### 💦 Water

- [Keep Water Heater turned On](https://github.com/denysdovhan/home-assistant-config/blob/525e83c111a9fdd360b0cd4b99b0cdfd517509e6/automations.yaml#L2176) – When Water Heater was accidentally turned off, automatically turn in on
<!-- end-automations -->

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
