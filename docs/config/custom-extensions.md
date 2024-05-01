# Custom Extensions

Home Assistant has a lot of integrations, but sometimes it's not enough. Fortunately, Home Assistant provides a way to add external integrations.

Below you will find integrations and Lovelace cards [developed by me](#developed-by-me) and [by other smart-home enthusiasts](#third-party).

I use [HACS](//hacs.xyz) for managing my third-party integrations and cards.

## Developed by Me

Sometimes even extensions provided by HACS are not enough, so I had to develop some extensions by myself.

### Lovelace Cards

#### [`vacuum-card`](https://github.com/denysdovhan/vacuum-card)

By default, Home Assistant does not provide any card for controlling vacuum cleaners. This card displays the state and allows you to control your robot.

![vacuum-card](https://user-images.githubusercontent.com/3459374/81119202-fa60b500-8f32-11ea-9b23-325efa93d7ab.gif){: loading=lazy, width=50% }

#### [`purifier-card`](https://github.com/denysdovhan/purifier-card)

As for vacuums, Home Assistant doesn't provide any card for controlling air purifiers either. This card displays the state and allows to control your air purifier.

![purifier-card](https://user-images.githubusercontent.com/3459374/94728037-48ee7000-0368-11eb-8637-c8bbc5ffaf99.gif){: loading=lazy, width=50% }

## Third party

Here's a list of extensions developed by other developers.

### Lovelace Cards

- [`mini-media-player`](https://github.com/kalkih/mini-media-player) — The default one looks not so elegant and has way fewer options to display.
- [`mini-graph-card`](https://github.com/kalkih/mini-graph-card) — This one has a ton of different options. The killer feature for me: the ability to animate and display multiple graphs.
- [`mini-humidifier`](https://github.com/artem-sedykh/mini-humidifier) — Simple and minimalistic. Default humidifier card allows displaying humidifiers only from `humidifier` domain, whereas my humidifier is available under `fan` domain. I don't actually like this card and plan to make my own to match the design of vacuum and purifier cards.
- [`lovelace-xiaomi-vacuum-map-card`](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) — This card enables you to specify a target or start a zoned cleanup using a live or static map, just like in Xiaomi Home app. Additionally you can define a list of zones and choose the ones to be cleaned.
- [`state-switch`](https://github.com/thomasloven/lovelace-state-switch) — This card is like a usual conditional card, but allows to make conditions based on the current user. I used this only to display appropriate Spotify player in Lovelace.
- [`bar-card`](https://github.com/custom-cards/bar-card) — This card is design to display progress bars.
- [`transmission-card`](https://github.com/amaximus/transmission-card) — This card is for displaying controls over Transmission torrent client.

### Integrations

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
