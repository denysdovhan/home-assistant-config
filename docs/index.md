# Welcome to my Home Assistant Config!

=== "Home"

    ![Home](https://github.com/denysdovhan/smart-home/assets/3459374/6085c456-0842-4313-934b-44245888c59f)

=== "Living Room"

    ![Living Room](https://github.com/denysdovhan/home-assistant-config/assets/3459374/65ed0e5a-e736-4e00-8d03-5a6b245b36d3){: loading=lazy }

=== "Bedroom"

    ![Bedroom](https://github.com/denysdovhan/home-assistant-config/assets/3459374/10993656-8fb3-403f-bf5d-a88ef3466aa9){: loading=lazy }

=== "Balcony"

    ![Balcony](https://github.com/denysdovhan/home-assistant-config/assets/3459374/ce707134-27ee-4bc2-a9fd-f3476c38bc4e){: loading=lazy }

=== "System"

    ![System](https://github.com/denysdovhan/home-assistant-config/assets/3459374/0cb9d64b-bb0f-4faf-8b7e-88852ecbd03b){: loading=lazy }

[![GitHub Workflow Status][github-img]][github-url]
[![Last Commit][last-commit-img]][github-url]
[![Commit Activity][commit-activity-img]][github-url]
[![License][license-img]][license-url]
[![GitHub Stars][stars-img]][github-url]
[![Twitter Followers][twitter-img]][twitter-url]

This is my personal Home Assistant configuration, awakening my home with automations. I hope this will help you inspire to start your home automation journey.

<!-- prettier-ignore -->
!!!attention "Beware of changes"
    I constantly improve my home. It evolves as I add new devices and services. It's changing as my daily routines are changing.

    Please, keep in mind **this documentation might be outdated** in covering some details. However, I'll try my best to keep this updated.

The best way to discover new ideas and inspire is by [reading the code][github-url], copying-pasting parts of my configuration and adjusting it to your needs.

Read this documentation to see the bigger picture:

[Hardware](./hardware){: .md-button }
[Home Assistant](./config){: .md-button }
[Inspiration](./resources){: .md-button }

Documentation for the rest of the stuff that I run on my smart home server can be found here:

[Smart Home](https://denysdovhan.com/smart-home){: .md-button }

## What's inside?

My home setup for those who are too lazy to read everything:

- [Home Assistant](https://home-assistant.io) OS run as a virtual machine on [Beelink Mini S12 Pro](https://www.aliexpress.com/item/1005005200158913.html) as a home server.
- [Home Assistant](https://home-assistant.io) for home automations.
- [Mosquitto](https://mosquitto.org/) and [zigbee2mqtt](https://www.zigbee2mqtt.io/) for Zigbee devices.
- Reverse proxy using [Nginx Proxy Manager](https://nginxproxymanager.com/) with [CloudFlare](https://www.cloudflare.com/).

## Motivation

I write this documentation for two main reasons:

1. **To keep track of growing my smart home.** To maintain an understanding of how things are working.
2. **To help other enthusiasts inspire.** People often ask about my smart home setup. Now I can give them a link to this documentation, instead of explaining everything once again.

## Limitations

I'm renting my apartment. My landlord handles fixing stuff in my home, covering all the expenses. The only downside is that I can't change anything in my home.

I can't disassemble anything and use custom switches or sockets. It means I can change only easily accessible parts, like bulbs.

## Future Plans

I have a [public Notion board][notion-board] with ideas and tasks for my smart home. You can follow and comment my plans there.

[See future plans][notion-board]{: .md-button }

## License

[MIT][license-url] © [Denys Dovhan][denysdovhan]

<!-- References -->

[notion-board]: https://www.notion.so/denysdovhan/f09ea06da5db4cfa84d3ca50417b93b2?v=5fccab53c2fd4ac188ee0b92c2ca1cb9
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
