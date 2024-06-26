# Hardware

This is the list of the hardware that is present in my smart home.

You can read more about what I host on my smart-home here:

[Smart Home Documentation](https://denysdovhan.com/smart-home){ .md-button }

## Homelab Server

My homelab server is running on [Beelink Mini S12 Pro](https://www.aliexpress.com/item/1005005200158913.html) with Intel 12th Gen 4-Cores N100 (up to 3.4GHz), 16GB of RAM and 500GB of SSD memory.

It can easily run multiple VMs or LXCs, transcode a few 4K streams, while staying quite and consuming only 8.2 watts at idle and 22.5 watts on max load. It's also very small – a little larger than Apple TV box. This combination of characteristics makes it a perfects smart home server.

=== "Beelink Mini S12 Pro"

    ![Beelink Mini S12 Pro](https://github.com/denysdovhan/home-assistant-config/assets/3459374/c687d08c-10c1-453c-b5b6-74c4e8cf8600)

=== "Packaging"

    ![Packaging](https://github.com/denysdovhan/home-assistant-config/assets/3459374/51dfc5c6-f7bf-4218-8bf0-8cc4ffe9c951)

I use [Seagate Barracuda 2TB 5400rpm 128MB](https://www.amazon.com/Seagate-BarraCuda-Internal-2-5-Inch-ST2000LM015/dp/B01LX13P71?th=1) as a hard driver for media files. 2TB is not much, but there's no much room withing the mini PC casing. I'll work on a better NAS solution in the future. Here's how it looks when open:

![Opened mini PC with HDD within](https://github.com/denysdovhan/home-assistant-config/assets/3459374/975dfa43-878d-4dec-8987-6f981a6bc814)

### Installation

A few words on how Home Assistant is run on my homelab server.

Home Assistant OS is run as a VM on a [Proxmox VE](https://www.proxmox.com/en/). My hardware is too powerful to run _only_ Home Assistant. Proxmox allows me to host multiple servers as LXCs and VMs on a single physical machine.

There are multiple guides on [how to install HA in Proxmox](https://www.youtube.com/results?search_query=home+assistant+proxmox+install).

Over time I tried practically all of the ways to run Home Assistant: I used it as OS on Raspberry Pi → I used to run in as Supervised on Debian → I ran it as a Container in Docker on Ubuntu Server → Now I'am back to OS, but in Virtual Environment.

## WiFi Network

You're going to have a lot of devices in your network when you have a smart home. It's critical to choose a good router to handle multiple devices and heavy traffic.

### Wireless Router

The second most important thing in my smart home is a WiFi router.

I've spent a lot of time choosing _the right router_. My main requirements for the router were:

- **Dual-band: 2.4GHz and 5GHz** — Primarily, I use two networks in my home: 2.4GHz for smart devices and 5GHz for personal devices like phones and laptops. 5GHz uses shorter radio waves, and that provides faster speeds.
- [**MU-MIMO**](https://en.wikipedia.org/wiki/Multi-user_MIMO) — This is a technology that enables simultaneous communication to multiple devices, improving overall speed and enabling network multitasking. It is critical when you have lots of connected devices and want each of them to work with the highest speed.
- [**802.11ac**](https://en.wikipedia.org/wiki/IEEE_802.11ac-2013) — this is a so-called WiFi5 standard. It allows increased speeds and improved scalability. I have a gigabyte connection at my home and wanted to benefit from it.

I chose [ASUS RT-AC1750U](https://www.asus.com/Networking-IoT-Servers/WiFi-Routers/ASUS-WiFi-Routers/RT-AC1750U/) router for my home. It matches every condition above and has nice additional features. Also, I've noticed that routers by ASUS are quite respected among other smart-home enthusiasts.

I'm happy with my decision so far. This router gives the constant 600-900 Mbit/s speed, which is enough to download a 10GB file in less than 2 minutes.

Previously, I've also tried Xiaomi Router and wasn't happy about it. Xiaomi Router has UI in Chinese and worked unreliably overall.

Here are my current ASUS and former Xiaomi routers:

![My current ASUS and former Xiaomi routers](https://user-images.githubusercontent.com/3459374/109073645-56cdd480-76ff-11eb-86ac-0f659381becf.jpeg)

### Devices

Below you will find a list of my devices connected to the local network. Most of them, except for Apple TV, have static IP addresses.

| Device                                       | IP                 | HA Integration                |
| -------------------------------------------- | :----------------- | ----------------------------- |
| [Apple TV 4K][apple-tv]                      | `192.168.50.x`\*   | [Apple TV][ha-apple-tv]       |
| [Koogeek P1EU Smart Plug][koogeek-p1]        | `192.168.50.9`     | [HomeKit Controller][homekit] |
| [Koogeek P1EU Smart Plug][koogeek-p1]        | `192.168.50.10`    | [HomeKit Controller][homekit] |
| [Koogeek P1EU Smart Plug][koogeek-p1]        | `192.168.50.11`    | [HomeKit Controller][homekit] |
| [Samsung 55" Q67R 4K Smart QLED TV][tv]      | `192.168.50.93`    | [ha-samsungtv-tizen]\*\*      |
| [Raspberry Pi][pi]                           | `192.168.50.113`\* | –                             |
| [Yeelight LED Bulb 1S (Color)][yeelight-1s]  | `192.168.50.128`   | [Yeelight][yeelight]          |
| [Yeelight LED Bulb 1S (Color)][yeelight-1s]  | `192.168.50.129`   | [Yeelight][yeelight]          |
| [Xiaomi Bulb White and Color][yeelight-bulb] | `192.168.50.130`   | [Yeelight][yeelight]          |
| [Xiaomi Desk Lamp Pro][desk-lamp]            | `192.168.50.131`   | [Yeelight][yeelight]          |
| [PlayStation 4 Pro][ps4]                     | `192.168.50.185`\* | [Sony PlayStation 4][ha-ps4]  |
| [Roborock S5 Max][roborock]                  | `192.168.50.186`   | [Xiaomi Miio][xiaomi-miio]    |
| [Deerma Humidifier (mjjsq)][humidifier]      | `192.168.50.187`   | [xiaomi_airpurifier]\*\*      |
| [Xiaomi Air Purifier 3H][air-purifier]       | `192.168.50.188`   | [Xiaomi Miio][xiaomi-miio]    |
| [Bedroom HomePod Mini][homepod-mini]         | `192.168.50.x`     | [Apple TV][ha-apple-tv]       |
| [Living Room HomePod Mini][homepod-mini]     | `192.168.50.x`     | [Apple TV][ha-apple-tv]       |
| [living-room-ac](#esp-devices)               | `192.168.50.x`     | [ESPHome][esphome]            |
| [bedroom-ac](#esp-devices)                   | `192.168.50.x`     | [ESPHome][esphome]            |

\* — means the device is connected via Ethernet instead of WiFi to ensure a more reliable connection.

\*\* — means the device is integrated via custom integration.

### ESP-devices

I use two ESP8266 devices based on [iot-uni-dongle](https://github.com/dudanov/iot-uni-dongle) for controlling my Midea ACs.

![IMG_8682](https://user-images.githubusercontent.com/3459374/134776312-a3f4eb00-fd78-46bf-8e9c-74c8a124bfa6.jpeg)

<!-- Devices -->

[apple-tv]: https://www.apple.com/apple-tv-4k/
[koogeek-p1]: https://www.koogeek.com/p-p1eu.html
[tv]: https://www.samsung.com/ua/tvs/qled-tv/q67r-55-inch-qled-4k-smart-tv-qe55q67rauxua/
[pi]: https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
[yeelight-1s]: https://www.yeelight.com/en_US/product/lemon2-color
[yeelight-bulb]: https://www.aliexpress.com/item/1005001870039407.html
[desk-lamp]: https://www.aliexpress.com/item/33045143366.html
[ps4]: https://www.playstation.com/en-us/ps4/ps4-pro/
[roborock]: https://us.roborock.com/pages/roborock-s5-max
[humidifier]: https://www.aliexpress.com/item/4000056420604.html
[air-purifier]: https://www.mi.com/global/mi-air-purifier-3H
[homepod-mini]: https://www.apple.com/homepod-mini/

<!-- Integrations -->

[homekit]: https://www.home-assistant.io/integrations/homekit_controller/
[yeelight]: https://www.home-assistant.io/integrations/yeelight/
[ha-ps4]: https://www.home-assistant.io/integrations/ps4/
[cast]: https://www.home-assistant.io/integrations/cast/
[xiaomi-miio]: https://www.home-assistant.io/integrations/xiaomi_miio/
[xiaomi_airpurifier]: https://github.com/syssi/xiaomi_airpurifier
[ha-apple-tv]: https://www.home-assistant.io/integrations/apple_tv/
[ha-samsungtv-tizen]: https://github.com/jaruba/ha-samsungtv-tizen
[esphome]: https://www.home-assistant.io/integrations/esphome/

## Zigbee Network

My Zigbee devices are connected to Home Assistant via [SMARTLIGHT CC2652P Zigbee USB Adapter SLZB-02](https://smartlight.me/smart-home-devices/zigbee-devices/zigbee-coordinator-v4-cc2652p) as a coordinator. Devices are controlled by Home Assistant via: [zigbee2mqtt](https://www.zigbee2mqtt.io/) + [Mosquitto](https://mosquitto.org/) + [MQTT Integration](https://www.home-assistant.io/integrations/mqtt/).

<!-- prettier-ignore -->
!!! note
    Previosly my Zigbee network was working with [CC2531 Sniffer Board](https://www.aliexpress.com/item/4000059514865.html) as a coordinator.
    It was fine with small amount of devices, but as my network grew I started to [get weird behavior](https://github.com/home-assistant/core/issues/52301).
    Additioanlly, I've discovered that [CC2531 is no longer recommended by zigbee2mqtt developers](https://www.zigbee2mqtt.io/guide/adapters/#not-recommended).

<!-- prettier-ignore -->
!!! tip
    I connected my coordinator to the Raspberry Pi through a USB extension cable to avoid interference and improve the connection.
    This approach is suggested by [zigbee2mqtt documentation](https://www.zigbee2mqtt.io/information/FAQ.html#interview-fails).

I used to use Aqara Hub, but it switched to the current approach because of its compatibility. The current approach allows binding together [nearly every possible Zigbee device](https://www.zigbee2mqtt.io/information/supported_devices.html).

### Devices

| Device                                                         | Quantity | Notes                                            |
| :------------------------------------------------------------- | :------: | :----------------------------------------------- |
| [Aqara Smart LED Bulb 9W][aqara-bulb]                          |    5     | Ceiling and Main lights                          |
| [Aqara Motion Sensor][aqara-motion]                            |    2     | Detecting motions in both rooms                  |
| [Aqara Magic Cube Controller][aqara-cube]                      |    1     | Controlling lights, scenes and modes             |
| [Aqara Conditions Sensor][aqara-conditions]                    |    1     | Internal temperature, humidity and pressure data |
| [Aqara Contact Sensor][aqara-contact]                          |    1     | Detection front door opening                     |
| [Aqara Single Switch Module T1 (without neutral)][aqara-relay] |    1     | Switching corridor light                         |
| [MiJia Conditions Sensor][mija-conditions]                     |    1     | Internal temperature and humidity data           |
| [Tuya Smart ZigBee Radiator][tuya-trv]                         |    2     | Adjusting heaters temperature                    |
| [Lonsonho 2-Gang Switch 2 (without neutral)][lonsonho-switch]  |    1     | Switching kitchen lights                         |

<!-- Devices -->

[aqara-bulb]: https://www.aliexpress.com/item/33005500098.html
[aqara-motion]: https://www.aliexpress.com/item/32975225751.html
[aqara-cube]: https://www.aliexpress.com/item/32986728343.html
[aqara-conditions]: https://www.aliexpress.com/item/32990414707.html
[aqara-contact]: https://www.aliexpress.com/item/32991903307.html
[aqara-relay]: https://www.zigbee2mqtt.io/devices/DLKZMK12LM.html
[mija-conditions]: https://www.aliexpress.com/item/32870614227.html
[tuya-trv]: https://a.aliexpress.com/_ApW4sD
[lonsonho-switch]: https://www.aliexpress.com/item/4001178298316.html

## Other Devices

Another important device is a smart car alarm. I used [StarLine AS96 BT GSM GPS](https://starline-sales.eu/Car-Alarms/starline-as96-bt-gsm-gps) which is easily integrated with Home Assistant via built-in [StarLine integration](https://www.home-assistant.io/integrations/starline/).

This alarm allows to start/stop the engine, arm/disarm the alarm, trigger horn remotely via Home Assistant. Primarily, I use this for tracking down my car and checking interior temperature right from Home Assistant.
