[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua/)

# Denys Dovhan's Home Assistant Config

![Home](https://github.com/denysdovhan/smart-home/assets/3459374/6085c456-0842-4313-934b-44245888c59f)

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

- [Advanced SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) `v18.0.0` – A supercharged SSH & Web Terminal access to your Home Assistant instance
- [File editor](https://github.com/home-assistant/addons/tree/master/configurator) `v5.8.0` – Simple browser-based file editor for Home Assistant
- [ESPHome](https://esphome.io/) `v2024.7.0` – ESPHome add-on for intelligently managing all your ESP8266/ESP32 devices
- [PS5 MQTT](https://github.com/FunkeyFlo/ps5-mqtt/tree/main/add-ons/ps5-mqtt) `v1.3.3` – Control Sony PlayStation 5 devices via MQTT
- [AirCast](https://github.com/hassio-addons/addon-aircast) `v4.2.1` – AirPlay capabilities for your Chromecast devices.
- [Home Assistant Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) `v0.112.1` – Automatically manage backups between Home Assistant and Google Drive
- [Samba share](https://github.com/home-assistant/addons/tree/master/samba) `v12.3.1` – Expose Home Assistant folders with SMB/CIFS
- [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) `v6.4.1` – An Open Source MQTT broker
- [Zigbee2MQTT](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt) `v1.39.0-1` – Use your ZigBee devices without the vendor's bridge or gateway
- [Cloudflared](https://github.com/brenner-tobias/addon-cloudflared/) `v5.1.15` – Use a Cloudflare Tunnel to remotely connect to Home Assistant without opening any ports
<!-- end-addons -->

## Automation

My home is awakened by these automations. The list is automatically and regularly updated. You can browse them by categories. Links will guide you to the specific automation in `automations.yaml` file.

<!-- start-automations -->

1. [🔔 Alert](#-alert) (9 automation)
1. [🌡️ Climate](#-climate) (8 automation)
1. [🌆 Curtains](#-curtains) (3 automation)
1. [💡 Light](#-light) (11 automation)
1. [🎵 Media](#-media) (2 automation)
1. [🚦 Mode](#-mode) (10 automation)
1. [🔘 Presence](#-presence) (2 automation)
1. [🖥️ System](#-system) (11 automation)
1. [🧹 Vacuum](#-vacuum) (7 automation)

Total number of automations: **63**️

### 🔔 Alert

- [Air Siren in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L57) – Air Alert announcement when we are in Kyiv. Sends critical notifications and announces on speakers.
- [Bad Air Quality](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L250) – Notify when the air quality is bad
- [Danger in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L122) – Danger of missile/drone strike in Kyiv RIGHT NOW. Critical alert to hide immediately.
- [Denys left the Office](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L284) – Notify when Denys is leaving the office
- [Electricity Outage](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L313) – Notify everyone when there is no electricity at home.
- [Electricity will turn on soon](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L533) – Notify 1 hours in advance before the electricity turns on
- [Imminent Attack by Strategic Bombers](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L228) – Send a notification when Tu-95 strategic bombers take off from Russian airfields. This means attack by cruise missiles is imminent. Prepare a hideout.
- [No Electricity Soon](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L503) – Notify 30 minutes in advance before the electricity turns off
- [Notify about EcoFlow discharge level](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1575) – Send notification when EcoFlow is draining battery.

### 🌡️ Climate

- [Calibrate Bedroom TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1494) – Calibrate TRV temperature with external sensor.
- [Calibrate Cabinet Left TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1506) – Calibrate TRV temperature with external sensor.
- [Calibrate Cabinet Right TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1518) – Calibrate TRV temperature with external sensor.
- [Calibrate Living Room TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1482) – Calibrate TRV temperature with external sensor.
- [Suggest turning on AC when it's hot](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#LNone) – When temperature raises over certain level, send an actionable notification for turning on ACs
- [Toggle dehumidifiers when we sleep](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2477) – Turn off Bathroom and Laundry dehumidifiers when we sleep and turn them on in the morning.
- [Turn on fan when someone is on the toilet](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1058) – When someone sits in the toilet, then turn on the fan. Turn off fan when person leaves.
- [Turn on heaters during heating season](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L563) – Turn on/off heaters when weather is getting cold/warm

### 🌆 Curtains

- [Open Bedroom Curtains in the morning](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L385) – Slowly open Bedroom Curtains.
- [Stop opening Bedroom Curtains when we don't want to](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#LNone) – Sometimes we want to prevent Bedroom Curtains from opening. Just close them when they are opening.
- [Tighten Curtains hooks](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1530) – Sometimes hooks on curtains are getting loose. This automation unlock and locks hooks on curtain robots

### 💡 Light

- [Motion-activated lights in Bedroom](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2314) – Turn on Lights in Bedroom based on presence and current activated light mode.
- [Motion-activated lights in Cabinet](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2249) – Turn on Lights in Cabinet based on presence and current activated light mode.
- [Presence Simulation in Away Mode](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1952) – Toggle Presence Simulation during Night in Away Mode
- [Suggest activating Night Lights](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2374) – At the deep evening, send a notification suggesting to activate Night Lights mode.
- [Turn off Bathroom lights](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1821) – When no one is in Bathroom, but the lights are still on, then turn them off.
- [Turn off Bedroom lights](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2350) – Turn off lights in Bedroom when motion sensor doesn't detect any motion for long period of time.
- [Turn off Cabinet lights](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2290) – Turn off lights in Cabinet when motion sensor doesn't detect any motion for long period of time.
- [Turn off Corridor Light When Door is Closed](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1694) – Turn off Corridor Light when Front Door closes. If the light is still on, then send a notification with an action to turn off the light.
- [Turn on Bathroom Ceiling Light](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2042) – When it's bright in the living room, turn on Bathroom Ceiling Light to match brightness in Living Room.
- [Turn on Bathroom Lightstrip](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1982) – Turn on Bathroom Lightstrip when someone walk in.
- [Turn on Corridor Light when Door is open](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1666) – Turn on Corridor Light when Front Door opens and then turn it off after a few minutes

### 🎵 Media

- [Turn off Samsung TV when PlayStation turns off](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L778) – Turn off Samsung TV when PS5 goes to sleep mode
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L802) – Turn on Apple TV when Samsung TV turns on and PS5 is off

### 🚦 Mode

- [Adjust Lights and Curtains in the evening](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2144) – When it's getting dark, or sun sets, or indoor illuminance is too low, then activate Evening Lights and close curtains
- [Away Flow](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1772) – Toggle Away mode depending on the Away input boolean
- [Away on Leaving City](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1782) – Toggle Away mode depending on proximity to the Kyiv city
- [Do Not Disturb on Focus](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1465) – Switch Do Not Disturb while camera, mic or focus are on
- [Evening Lights Activation](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2219) – The activation flow for a Evening Lights mode. Enables turns on corresponding lights and motion-activated lights.
- [Low Power Mode](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L481) – Minimise electricity consumption during the outage, when on reserve power supply.
- [Master Light Activation](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2555)
- [Night Lights Activation](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2234) – The activation flow for a Evening Lights mode. Enables turns on corresponding lights and motion-activated lights.
- [Sleeping Lights Activation](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2462) – The activation flow for a Sleeping Lights mode. Enables turns on corresponding lights.
- [Turn off modes when all lights turn off](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2514) – Turn off all light modes when all lights are off in the night, meaning we are set to sleep.

### 🔘 Presence

- [Everyone is Leaving](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1108)
- [Someone is Arriving](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1862) – Adjust home when someone arrives home:

* Close curtains when it's dark
* Greet people with unique phrase played on speakers

### 🖥️ System

- [Charging Wall Tablet](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L23) – Handles charging for Wall Tablet, keeping battery level between 20-80%
- [Fetch reports from Ukrenergo](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2067) – Parse data from [Ukrenergo](https://t.me/s/Ukrenergo) chanel with AI. Send notification about electricity outages updates. Update variables for other automations.
- [Home Assistant Start](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L836) – Notify Denys when Home Assistant starts
- [Notify about high CPU usage](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L924) – Send alert when HA has a high CPU usage
- [Notify about high RAM usage](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L888) – Notify when RAM usage is high for some time.
- [Notify when Media disk is full](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L955) – Notify when Media drive is 95% full for some time.
- [Notify when System disk is full](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L858) – Send a notification when system disk is 90% full.
- [Run chores in config folder](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L983) – Run scripts for generating README, commiting regular updated, etc
- [Toggle virtual Master Switch when Master Light Button is pressed](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2540) – Toggle state of Master Switch input boolean when the Master Light button is pressed
- [Turn off fridge when EcoFlow is below 50%](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1842) – Turn off fridge when EcoFlow is discharged below 50%, but there still no electricity. Save electricity additional ~100Wh.
- [Wake up Wall Tablet](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1) – When someone walks the corridor, wake up the wall mounted tablet

### 🧹 Vacuum

- [Ask Regular Cleaning](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1408) – Regular vacuum cleaning every two days
- [Ask for Maintenance](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1340) – Send vacuum near trash bin and ask for maintenance
- [Clean Counting](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1166) – Count cleanings with counter. Needed for maintaining the robot and making request to clean home.
- [Notify about errors](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1028) – Notify when error with vacuum occured
- [Notify when finished cleaning](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L995) – Notify when vacuum finished cleaning and we are not home.
- [Replacements Alert](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1260) – Notify when vacuum parts need to be replaced
- [iOS Actions](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1182) – Handle iOS actions for vacuum cleaner
<!-- end-automations -->

## Custom Components

Here is a list of all custom components I use:

<!-- start-custom-components -->

- [Check Weather](https://github.com/denysdovhan/ha-check-weather) `v1.3.0`
- [Chime TTS](https://nimroddolev.github.io/chime_tts) `vv1.1.5`
- [Ecoflow-Cloud](https://github.com/tolwi/hassio-ecoflow-cloud) `v1.2.0`
- [HACS](https://hacs.xyz/docs/configuration/start) `v2.0.1`
- [Hik-Connect](https://github.com/tomasbedrich/home-assistant-hikconnect) `v2.4.0`
- [Home Connect Alt](https://github.com/ekutner/home-connect-hass) `v1.1.9`
- [Inverse 👻](https://spook.boo) `v3.1.0`
- [LUN Misto Air](https://github.com/denysdovhan/ha-lun-misto-air) `v0.2.1`
- [Multiscrape](https://github.com/danieldotnl/ha-multiscrape) `v8.0.2`
- [Powercalc](https://docs.powercalc.nl) `vv1.15.2`
- [Presence Simulation](https://github.com/slashback100/presence_simulation) `v4.10`
- [Spook](https://spook.boo) `v3.1.0`
- [Vento Eco Vent v 2.0](https://www.home-assistant.io/integrations/ecovent_v2) `v1.0.1`
- [WebRTC Camera](https://github.com/AlexxIT/WebRTC) `vv3.6.0`
- [Yasno Outages](https://github.com/denysdovhan/ha-yasno-outages) `v0.3.6`
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
