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

1. [🚨 Alarm](#-alarm) (2 automation)
1. [🔔 Alert](#-alert) (10 automation)
1. [🌡️ Climate](#-climate) (8 automation)
1. [💡 Light](#-light) (6 automation)
1. [🎵 Media](#-media) (3 automation)
1. [🚦 Mode](#-mode) (4 automation)
1. [🔘 Presence](#-presence) (2 automation)
1. [🖥️ System](#-system) (10 automation)
1. [🧹 Vacuum](#-vacuum) (8 automation)
1. [💦 Water](#-water) (2 automation)

Total number of automations: **55**️

### 🚨 Alarm

- [Notification for Triggered](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L75) – Make an announcement when Alarm is getting triggered
- [Triggering Alarm](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L52)

### 🔔 Alert

- [Air Siren in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1) – Air Alert announcement when we are in Kyiv. Sends critical notifications and announces on speakers.
- [Bad Air Quality](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L359) – Notify when the air quality is bad
- [Car Washing](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L419) – Notify when it’s okay or not okay to wash a car
- [Danger in Kyiv](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2166) – Danger of missile/drone strike in Kyiv RIGHT NOW. Critical alert to hide immediately.
- [Denys left the Office](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2034) – Notify when Denys is leaving the office
- [Electricity Outage Notification](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2274) – Notify everyone when there is no electricity at home.
- [Humidifier No Water](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L393) – Notify when humidifier's water tank is empty
- [Imminent Attack by Strategic Bombers](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2251) – Send a notification when Tu-95 strategic bombers take off from Russian airfields. This means attack by cruise missiles is imminent. Prepare a hideout.
- [Low Battery Notification](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2331) – Notify when battery is low on devices, so we could buy a replacements.
- [Snow/Winter Tires](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L469) – Notify when it's time to change car tires

### 🌡️ Climate

- [Preheat Balcony for a Workday](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L725) – When Denys wakes up, ask if he is going to work on balcony, start heating and notify when temperature is comfortable.
- [Suggest turning on AC when it's hot](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#LNone) – When temperature raises over certain level, send an actionable notification for turning on ACs
- [Switch Heaters during Heating Season](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L560) – Turn on/off heaters when Heating Season in on
- [Sync Bedroom TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L551)
- [Sync Living Room TRV temperature](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L542)
- [Turn off Balcony Heater](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L673) – Turn off Balcony Heater when the working display or desk lamp are off for some time
- [Turn on Balcony Heater](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L633) – Turn on Balcony Heater when it's cold and Desk Lamp or Working Display are turned on
- [Turn on Humidifier only during sleep time](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1774)

### 💡 Light

- [Presence Simulation in Away Mode](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1111) – Toggle Presence Simulation during Night in Away Mode
- [Toggle Desk Lamp with Working Display](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1026) – Sync Desk lamp with Working Display
- [Turn off Corridor Light When Door is Closed](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L950) – Turn off Corridor Light when Front Door closes. If the light is still on, then send a notification with an action to turn off the light.
- [Turn on Corridor Light when Door is open](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L927) – Turn on Corridor Light when Front Door opens and then turn it off after a few minutes
- [Turn on lights on Sunset](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L819) – Turn on lights when sun goes below the horizon
- [Turn on lights on low illuminance](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L868) – Turn on lights on low illuminance

### 🎵 Media

- [Turn off Samsung TV when PlayStation turns off](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L95) – Turn off Samsung TV when PS5 goes to sleep mode
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1943) – Turn on Apple TV when Samsung TV turns on and PS5 is off
- [Turn on Apple TV when Samsung TV turns on](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1943) – Turn on Apple TV when Samsung TV turns on and PS5 is off

### 🚦 Mode

- [Away Flow](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1077) – Toggle Away mode depending on the Away input boolean
- [Away on Leaving City](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1087) – Toggle Away mode depending on proximity to the Kyiv city
- [Do Not Disturb Activation](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1042) – Adjust devices to Do Not Disturb mode
- [Do Not Disturb on Focus](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1059) – Switch Do Not Disturb while camera, mic or focus are on

### 🔘 Presence

- [Everyone is Arriving](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1139) – Turn on things when people are arriving
- [Everyone is Leaving](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1219) – Turn off things when people are leaving

### 🖥️ System

- [Home Assistant Release](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L244) – Notify Denys about new Home Assistant releases
- [Home Assistant Start](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L313) – Notify Denys when Home Assistant starts
- [Magic Cube Actions](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L122)
- [Notify about HACS updates](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L275) – Notify when new HACS components are released
- [Notify about high CPU usage](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2068) – Send alert when HA has a high CPU usage
- [Notify about high RAM usage](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2099) – Notify when RAM usage is high for some time.
- [Notify when Media disk is full](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L333) – Notify when Media drive is 90% full for some time.
- [Notify when System disk is full](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2136) – Send a notification when system disk is 90% full.
- [Power Outage Recovery](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1717)
- [Run chores in config folder](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2022) – Run scripts for generating README, commiting regular updated, etc

### 🧹 Vacuum

- [Ask Regular Cleaning](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1291) – Regular vacuum cleaning every two days
- [Ask for Maintenance](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1430) – Send vacuum near trash bin and ask for maintenance
- [Clean Counting](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L2005) – Count cleanings via counter
- [Error Alert](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1402) – Notify when error with vacuum occured
- [Finish Alert](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1369) – Notify when vacuum finished cleaning and we are not home.
- [Replacements Alert](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1498) – Notify when vacuum parts need to be replaced
- [Stop cleaning when we return home](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1351) – Send vacuum home when somebody comes home
- [iOS Actions](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1578) – Handle iOS actions for vacuum cleaner

### 💦 Water

- [Keep Water Heater turned On](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1978) – When Water Heater was accidentally turned off, automatically turn in on
- [Notify when water is heated](https://github.com/denysdovhan/home-assistant-config/blob/a4c0c5d8fe9289ebde2830efa7734e31f6929ba7/automations.yaml#L1649) – When we ask to let us know when the boiler has done heating, it should notify about that.
<!-- end-automations -->

## Addons

These addons provide additional functionality for my Home Assistant instance.

<!-- start-addons -->

- [Advanced SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) v17.3.0 – A supercharged SSH & Web Terminal access to your Home Assistant instance
- [File editor](https://github.com/home-assistant/addons/tree/master/configurator) v5.8.0 – Simple browser-based file editor for Home Assistant
- [ESPHome](https://esphome.io/) v2024.5.2 – ESPHome add-on for intelligently managing all your ESP8266/ESP32 devices
- [PS5 MQTT](https://github.com/FunkeyFlo/ps5-mqtt/tree/main/add-ons/ps5-mqtt) v1.3.3 – Control Sony PlayStation 5 devices via MQTT
- [AirCast](https://github.com/hassio-addons/addon-aircast) v4.2.1 – AirPlay capabilities for your Chromecast devices.
- [Home Assistant Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) v0.112.1 – Automatically manage backups between Home Assistant and Google Drive
- [Samba share](https://github.com/home-assistant/addons/tree/master/samba) v12.3.1 – Expose Home Assistant folders with SMB/CIFS
- [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) v6.4.0 – An Open Source MQTT broker
- [Zigbee2MQTT](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt) v1.37.1-1 – Use your ZigBee devices without the vendor's bridge or gateway
<!-- end-addons -->

<!-- References -->

[ha]: https://www.home-assistant.io/
[asuswrt]: https://www.home-assistant.io/integrations/asuswrt
[mobile_app]: https://www.home-assistant.io/integrations/mobile_app/
