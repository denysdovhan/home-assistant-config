# Configuration

I use [Home Assistant][ha] as my primary smart home software. It allows me to tied down every separate ecosystem, every device, and every service together.

This is a very powerful tool, allowing to built complex and smart automation based on multiple triggers and conditions, performing different actions.

So far, I'm happy with [Home Assistant][ha] and strongly recommend trying it if you are a smart home enthusiast.

## Prior Art

I began my smart home journey with an [Aqara Hub](https://www.aliexpress.com/item/32910909157.html) and a few bulbs.

In the beginning, I was hoping to consolidate my smart home over HomeKit, because I'd already had a few Apple devices. Shortly after, I run into multiple limitations. After a year of using Aqara setup, I decided to switch to the more universal and powerful solution — [Home Assistant][ha].

Now I easily pass my devices to the HomeKit as well as to the Google Home app.

## How I make my automations

<!-- prettier-ignore -->
!!! tip
    I highly suggest reading a blog post called [Perfect Home Automation](https://www.home-assistant.io/blog/2016/01/19/perfect-home-automation/) written by Home Assistant creator Paulus Schoutsen.

    This article contains valid points about developing home automation. This will help you develop the right mindset while building your smart home.

There are a few rules I use while building my smart home:

- **You should not adapt to technologies.** Things should _just work_. You shouldn't break your own daily routines in order to adapt to your home. Home automation should blend with your current workflow, not replace it.
- **You are not the only user of your home automation.** Even when you live alone, you may have guests. Think about how they're going to use your home.
- **Limit the impact of failures.** Smart homes are complex: eventually, things will go wrong. Make sure things will have a limited impact when they fail. Ideally, devices should fall back to a pre-smart home experience.
- **Automations must be seamless.** Nobody controls lights from the phone except for showing off. This means that everything you automate has to work flawlessly. Even when automation works perfectly 90% of the time, the rest 10% will ruin the whole positive experience.

That's what I keep in mind. This helps a lot.

## Automations

Here you can discover all of the automations powering my home. The list is automatically and regularly updated.

<!-- start-automations -->

1. [🔔 Alert](#-alert) (9 automation)
1. [🌡️ Climate](#-climate) (7 automation)
1. [🌆 Curtains](#-curtains) (3 automation)
1. [💡 Light](#-light) (12 automation)
1. [🎵 Media](#-media) (2 automation)
1. [🚦 Mode](#-mode) (6 automation)
1. [🔘 Presence](#-presence) (3 automation)
1. [🖥️ System](#-system) (10 automation)
1. [🧹 Vacuum](#-vacuum) (8 automation)
1. [⚙️ WIP](#-wip) (1 automation)

Total number of automations: **61**️

### 🔔 Alert

- [Air Siren in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L57) – Air Alert announcement when we are in Kyiv. Sends critical notifications and announces on speakers.
- [Bad Air Quality](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L243) – Notify when the air quality is bad
- [Danger in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L122) – Danger of missile/drone strike in Kyiv RIGHT NOW. Critical alert to hide immediately.
- [Denys left the Office](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L277) – Notify when Denys is leaving the office
- [Electricity Outage](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L306) – Notify everyone when there is no electricity at home.
- [Electricity will turn on soon](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L511) – Notify 1 hours in advance before the electricity turns on
- [Imminent Attack by Strategic Bombers](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L221) – Send a notification when Tu-95 strategic bombers take off from Russian airfields. This means attack by cruise missiles is imminent. Prepare a hideout.
- [No Electricity Soon](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L481) – Notify 30 minutes in advance before the electricity turns off
- [Notify about EcoFlow discharge level](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1612) – Send notification when EcoFlow is draining battery.

### 🌡️ Climate

- [Calibrate Bedroom TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1540) – Calibrate TRV temperature with external sensor.
- [Calibrate Cabinet Left TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1549) – Calibrate TRV temperature with external sensor.
- [Calibrate Cabinet Right TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1558) – Calibrate TRV temperature with external sensor.
- [Calibrate Living Room TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1531) – Calibrate TRV temperature with external sensor.
- [Suggest turning on AC when it's hot](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#LNone) – When temperature raises over certain level, send an actionable notification for turning on ACs
- [Turn on Bathroom fan when humidity is rising](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2505) – Turn on Bathroom fan when humidity is rapidly rising. Turn it off when humidity was decreasing for some time.
- [Turn on heaters during heating season](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L541) – Turn on/off heaters when weather is getting cold/warm

### 🌆 Curtains

- [Close curtains in the evening](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2066)
- [Open Bedroom Curtains in the morning](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L378)
- [Tighten Curtains hooks](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1567) – Sometimes hooks on curtains are getting loose. This automation unlock and locks hooks on curtain robots

### 💡 Light

- [Activate Evening Lights in the evening](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2194) – When it's getting dark, or sun sets, or indoor illuminance is too low, then activate Evening Lights.
- [Motion-activated lights in Bedroom](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2352) – Turn on Lights in Bedroom based on presence and current activated light mode.
- [Motion-activated lights in Cabinet](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2292) – Turn on Lights in Cabinet based on presence and current activated light mode.
- [Presence Simulation in Away Mode](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1976) – Toggle Presence Simulation during Night in Away Mode
- [Suggest to activate Night Lights](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2412) – At the deep evening, send a notification suggesting to activate Night Lights mode.
- [Turn off Bathroom lights](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1857) – When no one is in Bathroom, but the lights are still on, then turn them off.
- [Turn off Bedroom lights](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2388) – Turn off lights in Bedroom when motion sensor doesn't detect any motion for long period of time.
- [Turn off Cabinet lights](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2328) – Turn off lights in Cabinet when motion sensor doesn't detect any motion for long period of time.
- [Turn off Corridor Light When Door is Closed](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1731) – Turn off Corridor Light when Front Door closes. If the light is still on, then send a notification with an action to turn off the light.
- [Turn on Bathroom Ceiling Light](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2095) – When it's bright in the living room, turn on Bathroom Ceiling Light to match brightness in Living Room.
- [Turn on Bathroom Lightstrip](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2006) – Turn on Bathroom Lightstrip when someone walk in.
- [Turn on Corridor Light when Door is open](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1703) – Turn on Corridor Light when Front Door opens and then turn it off after a few minutes

### 🎵 Media

- [Turn off Samsung TV when PlayStation turns off](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L756) – Turn off Samsung TV when PS5 goes to sleep mode
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L780) – Turn on Apple TV when Samsung TV turns on and PS5 is off

### 🚦 Mode

- [Away Flow](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1809) – Toggle Away mode depending on the Away input boolean
- [Away on Leaving City](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1819) – Toggle Away mode depending on proximity to the Kyiv city
- [Do Not Disturb on Focus](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1514) – Switch Do Not Disturb while camera, mic or focus are on
- [Evening Lights Activation](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2250) – The activation flow for a Evening Lights mode. Enables turns on corresponding lights and motion-activated lights.
- [Low Power Mode](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L459) – Minimise electricity consumption during the outage, when on reserve power supply.
- [Night Lights Activation](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2271) – The activation flow for a Evening Lights mode. Enables turns on corresponding lights and motion-activated lights.

### 🔘 Presence

- [Everyone is Leaving](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1103)
- [Someone is Arriving](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1898) – Adjust home when someone arrives home:

* Close curtains when it's dark
* Greet people with unique phrase played on speakers

- [Turn on fan when someone is on the toilet](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1036) – When someone sits in the toilet, then turn on the fan. Turn off fan when person leaves.

### 🖥️ System

- [Charging Wall Tablet](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L23) – Handles charging for Wall Tablet, keeping battery level between 20-80%
- [Fetch reports from Ukrenergo](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2120) – Parse data from [Ukrenergo](https://t.me/s/Ukrenergo) chanel with AI. Send notification about electricity outages updates. Update variables for other automations.
- [Home Assistant Start](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L814) – Notify Denys when Home Assistant starts
- [Notify about high CPU usage](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L902) – Send alert when HA has a high CPU usage
- [Notify about high RAM usage](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L866) – Notify when RAM usage is high for some time.
- [Notify when Media disk is full](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L933) – Notify when Media drive is 95% full for some time.
- [Notify when System disk is full](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L836) – Send a notification when system disk is 90% full.
- [Run chores in config folder](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L961) – Run scripts for generating README, commiting regular updated, etc
- [Turn off fridge when EcoFlow is below 50%](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1878) – Turn off fridge when EcoFlow is discharged below 50%, but there still no electricity. Save electricity additional ~100Wh.
- [Wake up Wall Tablet](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1) – When someone walks the corridor, wake up the wall mounted tablet

### 🧹 Vacuum

- [Ask Regular Cleaning](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1457) – Regular vacuum cleaning every two days
- [Ask for Maintenance](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1389) – Send vacuum near trash bin and ask for maintenance
- [Clean Counting](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1215) – Count cleanings with counter. Needed for maintaining the robot and making request to clean home.
- [Notify about errors](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1006) – Notify when error with vacuum occured
- [Notify when finished cleaning](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L973) – Notify when vacuum finished cleaning and we are not home.
- [Replacements Alert](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1309) – Notify when vacuum parts need to be replaced
- [Stop cleaning when we return home](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1084) – Send vacuum home when somebody comes home
- [iOS Actions](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L1231) – Handle iOS actions for vacuum cleaner

### ⚙️ WIP

- [Open Living Room Curtains in the morning.](https://github.com/denysdovhan/home-assistant-config/blob/e721533aca75b44f1110e09a348419de9d25031d/automations.yaml#L2473)
<!-- end-automations -->

## Addons

These addons provide additional functionality for my Home Assistant instance.

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

<!-- References -->

[ha]: https://www.home-assistant.io/
[asuswrt]: https://www.home-assistant.io/integrations/asuswrt
[mobile_app]: https://www.home-assistant.io/integrations/mobile_app/
