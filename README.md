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

1. [🔔 Alert](#-alert) (10 automation)
1. [🌡️ Climate](#-climate) (8 automation)
1. [🌆 Curtains](#-curtains) (3 automation)
1. [💡 Light](#-light) (16 automation)
1. [🎵 Media](#-media) (3 automation)
1. [🚦 Mode](#-mode) (10 automation)
1. [🔘 Presence](#-presence) (2 automation)
1. [🖥️ System](#-system) (11 automation)
1. [🧹 Vacuum](#-vacuum) (7 automation)
1. [💦 Water](#-water) (2 automation)

Total number of automations: **72**️

### 🔔 Alert

- [Air Siren in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L63) – Air Alert announcement when we are in Kyiv. Sends critical notifications and announces on speakers.
- [Bad Air Quality](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L258) – Notify when the air quality is bad
- [Danger in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L130) – Danger of missile/drone strike in Kyiv RIGHT NOW. Critical alert to hide immediately.
- [Denys left the Office](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L295) – Notify when Denys is leaving the office
- [Electricity Outage](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L325) – Notify everyone when there is no electricity at home.
- [Electricity Outages report from Ukrenergo](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2454) – Send a notification with a summary of Electricity Outages report from Ukrenergo
- [Electricity will turn on soon](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L449) – Notify 1 hours in advance before the electricity turns on
- [Imminent Attack by Strategic Bombers](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L236) – Send a notification when Tu-95 strategic bombers take off from Russian airfields. This means attack by cruise missiles is imminent. Prepare a hideout.
- [No Electricity Soon](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L419) – Notify 30 minutes in advance before the electricity turns off
- [Notify about EcoFlow discharge level](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1456) – Send notification when EcoFlow is draining battery.

### 🌡️ Climate

- [Calibrate Bedroom TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1397) – Calibrate TRV temperature with external sensor.
- [Calibrate Cabinet Left TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1409) – Calibrate TRV temperature with external sensor.
- [Calibrate Cabinet Right TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1421) – Calibrate TRV temperature with external sensor.
- [Calibrate Living Room TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1385) – Calibrate TRV temperature with external sensor.
- [Suggest turning on AC when it's hot](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#LNone) – When temperature raises over certain level, send an actionable notification for turning on ACs
- [Toggle dehumidifiers when we sleep](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2181) – Turn off Bathroom and Laundry dehumidifiers when we sleep and turn them on in the morning.
- [Turn on fan when someone is on the toilet](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L955) – When someone sits in the toilet, then turn on the fan. Turn off fan when person leaves.
- [Turn on heaters during heating season](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L479) – Turn on/off heaters when weather is getting cold/warm

### 🌆 Curtains

- [Open Bedroom Curtains](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2627) – Gradually open Bedroom Curtains on workdays and weekends
- [Stop opening Bedroom Curtains when we don't want to](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#LNone) – Sometimes we want to prevent Bedroom Curtains from opening. Just close them when they are opening.
- [Tighten Curtains hooks](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1433) – Sometimes hooks on curtains are getting loose. This automation unlock and locks hooks on curtain robots

### 💡 Light

- [Motion-activated lights in Bedroom](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2019) – Turn on Lights in Bedroom based on presence and current activated light mode.
- [Motion-activated lights in Cabinet](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1956) – Turn on Lights in Cabinet based on presence and current activated light mode.
- [Presence Simulation in Away Mode](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1734) – Toggle Presence Simulation during Night in Away Mode
- [Suggest activating Night Lights](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2077) – At the deep evening, send a notification suggesting to activate Night Lights mode.
- [Turn off Balcony Christmas Lights at 23:00](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2682) – Turn off Balcony Christmas Lights at 23:00 to not disturb neighbors.
- [Turn off Bathroom lights](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1622) – When no one is in Bathroom, but the lights are still on, then turn them off.
- [Turn off Bedroom lights](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2053) – Turn off lights in Bedroom when motion sensor doesn't detect any motion for long period of time.
- [Turn off Cabinet lights](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1995) – Turn off lights in Cabinet when motion sensor doesn't detect any motion for long period of time.
- [Turn off Corridor Light without presence](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2596) – Turn off Corridor Light without presence in Corridor
- [Turn off Laundry light when door is closed](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2480) – Turn off Laundry light when Laundry Door is closed and the light is still on. Useful when the light was turned on manually, when door was opened.
- [Turn off Wardrobe lights without presence](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2657) – When no one is in Wardrobe, but the lights are still on, then turn them off.
- [Turn on Bathroom Ceiling Light](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1827) – When it's bright in the living room, turn on Bathroom Ceiling Light to match brightness in Living Room.
- [Turn on Bathroom Lightstrip](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1764) – Turn on Bathroom Lightstrip when someone walk in.
- [Turn on Corridor Light when Door is open](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1547) – Turn on Corridor Light when Front Door opens and then turn it off after a few minutes
- [Turn on Front Door Lamp when Electricity is off](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2501) – Front Door Lamp is a good guiding light in the dark. This automation turns on this lamp when Electricity is off and turns it off, when Electricity is on.
- [Turn on Laundry Light](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2273) – Turn on lights in Laundry when door is opened. Wait for door to close and turn off the light.

### 🎵 Media

- [Enable Transmission Turtle Mode when some watches Plex](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2562) – Limit download speed, when someone watches Plex to avoid HDD saturation and playback interruptions.
- [Turn off Samsung TV when PlayStation turns off](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L675) – Turn off Samsung TV when PS5 goes to sleep mode
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L699) – Turn on Apple TV when Samsung TV turns on and PS5 is off

### 🚦 Mode

- [Adjust Lights and Curtains in the evening](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1849) – When it's getting dark, or sun sets, or indoor illuminance is too low, then activate Evening Lights and close curtains
- [Away Flow](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1562) – Toggle Away mode depending on the Away input boolean
- [Away on Leaving City](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1572) – Toggle Away mode depending on proximity to the Kyiv city
- [Do Not Disturb on Focus](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1368) – Switch Do Not Disturb while camera, mic or focus are on
- [Evening Lights Activation](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1926) – The activation flow for a Evening Lights mode. Enables turns on corresponding lights and motion-activated lights.
- [Low Power Mode](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L397) – Minimise electricity consumption during the outage, when on reserve power supply.
- [Master Input runs Arriving/Leaving Home](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2244) – Run Arriving/Leaving Home flows when Master Input is toggled
- [Night Lights Activation](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1941) – The activation flow for a Evening Lights mode. Enables turns on corresponding lights and motion-activated lights.
- [Sleeping Lights Activation](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2166) – The activation flow for a Sleeping Lights mode. Enables turns on corresponding lights.
- [Turn off modes when all lights turn off](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2218) – Turn off all light modes when all lights are off in the night, meaning we are set to sleep.

### 🔘 Presence

- [Everyone is Leaving](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1008)
- [Someone is Arriving](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1666) – Adjust home when someone arrives home. Run Arriving home, greet people.

### 🖥️ System

- [Charging Wall Tablet](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L29) – Handles charging for Wall Tablet, keeping battery level between 20-80%
- [Home Assistant Start](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L733) – Notify Denys when Home Assistant starts
- [Notify about high CPU usage](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L821) – Send alert when HA has a high CPU usage
- [Notify about high RAM usage](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L785) – Notify when RAM usage is high for some time.
- [Notify when Media disk is full](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L852) – Notify when Media drive is 95% full for some time.
- [Notify when System disk is full](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L755) – Send a notification when system disk is 90% full.
- [Parse Ukrenergo Telegram with AI](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2368) – Parse data from [Ukrenergo](https://t.me/s/Ukrenergo) chanel with AI. Send notification about electricity outages updates. Update variables for other automations.
- [Run chores in config folder](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L880) – Run scripts for generating README, commiting regular updated, etc
- [Turn off fridge when EcoFlow is below 50%](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1646) – Turn off fridge when EcoFlow is discharged below 50%, but there still no electricity. Save electricity additional ~100Wh.
- [Update Electricity Outages schedule](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2413) – When Ukrenergo Response is updated with a related date, update electricity outages start/end datetime.
- [Wake up Wall Tablet](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1) – When someone walks the corridor, wake up the wall mounted tablet

### 🧹 Vacuum

- [Ask Regular Cleaning](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1311) – Regular vacuum cleaning every two days
- [Ask for Maintenance](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1243) – Send vacuum near trash bin and ask for maintenance
- [Clean Counting](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1069) – Count cleanings with counter. Needed for maintaining the robot and making request to clean home.
- [Notify about errors](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L925) – Notify when error with vacuum occured
- [Notify when finished cleaning](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L892) – Notify when vacuum finished cleaning and we are not home.
- [Replacements Alert](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1163) – Notify when vacuum parts need to be replaced
- [iOS Actions](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L1085) – Handle iOS actions for vacuum cleaner

### 💦 Water

- [Close Water Valve when leak is detected](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2310) – When water leak is detected, close the Water Valve and make a critical announcement.
- [Keep Water Boiler on](https://github.com/denysdovhan/home-assistant-config/blob/9ff2a365ae41e27ddb5c0d6074cc071df4f6adf8/automations.yaml#L2536) – Turn on boiler when it's off, when it should be on
<!-- end-automations -->

## Custom Components

Here is a list of all custom components I use:

<!-- start-custom-components -->

- [Battery Notes](https://andrew-codechimp.github.io/HA-Battery-Notes/) `v2.8.3`
- [Check Weather](https://github.com/denysdovhan/ha-check-weather) `v1.3.0`
- [Ecoflow-Cloud](https://github.com/tolwi/hassio-ecoflow-cloud) `v1.2.0`
- [HACS](https://hacs.xyz/docs/use/) `v2.0.5`
- [Hik-Connect](https://github.com/tomasbedrich/home-assistant-hikconnect) `v2.4.0`
- [Home Connect Alt](https://github.com/ekutner/home-connect-hass) `v1.1.12`
- [Inverse 👻](https://spook.boo) `v3.1.0`
- [LUN Misto Air](https://github.com/denysdovhan/ha-lun-misto-air) `v0.2.1`
- [Multiscrape](https://github.com/danieldotnl/ha-multiscrape) `v8.0.2`
- [Places](https://github.com/custom-components/places) `vv2.8.2`
- [Powercalc](https://docs.powercalc.nl) `vv1.17.6`
- [Presence Simulation](https://github.com/slashback100/presence_simulation) `v4.12`
- [Spook](https://spook.boo) `v3.1.0`
- [Vento Eco Vent v 2.0](https://www.home-assistant.io/integrations/ecovent_v2) `v1.0.4`
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
