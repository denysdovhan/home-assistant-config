# War Safety

In 2022, [Russia launched a full-scale invasion of Ukraine](https://en.wikipedia.org/wiki/Russo-Ukrainian_War), waging a genocidal war against my country. Ukraine is being hit by all types of weapons (except nuclear) daily. Home Assistant helps me stay safe and notifies me about incoming threats.

We hear the siren a few times a day. Life would completely stop if we went to the shelter every time the siren goes off. So, people adapt.

In Ukraine, we tend to differentiate the levels of danger. When the siren goes off, practically everyone starts checking their phones: "What is going on?"

We have [various applications](https://alerts.in.ua/) and [Telegram channels](https://t.me/s/war_monitor) for monitoring the type of danger, missile paths, and understanding whether we are in direct danger or can continue with our lives for another minute.

This is what war in the 21st century looks like: you can practically monitor a missile or a drone that is trying to kill you right from your phone. This is like a Black Mirror episode in real life. 😅

There are different kinds of air alarms with varying levels of danger:

- **MiG-31K take off** – This can happen multiple times during the day. The [MiG-31K](https://en.wikipedia.org/wiki/Mikoyan_MiG-31) can carry a very dangerous [Kh-47M2 Kinzhal hypersonic missile](https://en.wikipedia.org/wiki/Kh-47M2_Kinzhal). Although it happens rarely, you can't predict when the missile is attached and when it is not, so most people tolerate this level of danger.
- **Suicide drones attack** – Usually carried out by [Iranian Shahed 136 drones](https://en.wikipedia.org/wiki/HESA_Shahed_136). Most of them get shot down, but they are still dangerous and scary. We call them "mopeds" or "lawn-mowers" because of the sound of their engine.
- **Ballistic missile attack** – This can happen multiple times a day. Ballistic missiles, like the [9K720 Iskander](https://en.wikipedia.org/wiki/9K720_Iskander), are extremely fast (2 km/s). You have only up to 10 minutes to hide somewhere. Usually, the fastest way is to hide behind two walls (corridor or a bathroom).
- **Cruise missile attack** – Cruise missiles, like the [Kalibr](<https://en.wikipedia.org/wiki/Kalibr_(missile_family)>), are relatively slow and fly like a plane. Nevertheless, they can fly a long distance and easily reach any point in the country.

Of course, the most dangerous type of attack is a combined one. This means all of the above are raining down on Ukrainian cities simultaneously. These usually happen overnight at 4:00 in the morning. The drones and cruise missiles are used to exhaust air defenses, followed by ballistic and/or hypersonic strikes.

# Monitoring Air Alerts

Home Assistant has a built-in [Ukraine Alarm](https://www.home-assistant.io/integrations/ukraine_alarm/) integration. It monitors the nation-wide system of air alarms and toggles safety sensors in HA.

When there is any type of danger, I send a critical notification and announce the message on my smart speakers.

Of course, the air siren goes off on the streets, roaring across the city, so everyone hears the danger is approaching. But I made an automation to send a critical notification and speak at home speakers, so I certainly wake up to check what is going on.

```yaml
id: air_siren_kyiv
alias: 'Alert: Air Siren in Kyiv'
description:
  Air Alert announcement when we are in Kyiv. Sends critical notifications
  and announces on speakers.
trigger:
  - platform: state
    entity_id: binary_sensor.alerts_kyiv_air
    to: 'on'
    from: 'off'
    variables:
      title: Air Alert goes off!
  - platform: state
    entity_id: binary_sensor.alerts_kyiv_air
    to: 'off'
    from: 'on'
    variables:
      title: It is safe now!
condition:
  - alias: Someone is in Kyiv
    condition: state
    entity_id: sensor.family_in_kyiv
    state: 'on'
action:
  - service: script.announcement
    data:
      title: '{{ title }}'
      force_speak: true # Speaks even in DND mode
      notify_data:
        group: air-alerts
        push:
          sound:
            name: default
            critical: 1
            volume: 0.75
```

# Scraping Monitoring Channels

I already mentioned we have various Telegram channels for monitoring the situation during an attack. Those channels provide live updates on dangers, flight paths, and the type of attack.

So often I found myself constantly checking my phone to understand whether I am in direct danger or can sleep for a few hours. _I know it sounds crazy, and normal people would go straight to the nearby shelter, but this is life in Ukraine. You don't have to follow my reckless example. If you are in Ukraine, GO TO THE SHELTER!_

I decided to automate it. Instead of reading these channels myself, I delegate this task to HA.

I use the [HA Multiscrape](https://github.com/danieldotnl/ha-multiscrape) custom integration for that. You may ask, "why do you need a custom component when [HA has a built-in scraping component](https://www.home-assistant.io/integrations/scrape/)?" Yes, it does, but I need multiple sensors from a single scrape, and I need to work with lists of data. The built-in component has some limitations with that.

## Monitoring Imminent Danger

Cruise missiles are usually carried and launched by [Tu-95 bombers](https://en.wikipedia.org/wiki/Tupolev_Tu-95).

They fly to the missile launch sites for about 3 hours, launch their missiles, then it takes about 1-2 hours for missiles to fly to Kyiv. So there's some time to prepare a hideout (in my case, it's the bathroom), gather documents, and sleep for a few hours before the "show" begins.

Usually, it happens in the evening and means tonight will be a massive missile attack.

I have a sensor that checks the Telegram channels, scrapes the list of messages every 5 seconds, and checks if the latest message contains a specific set of words, like _"take off" **and** "plane" **and** "tu-95"_. It also stores the latest message as an attribute.

```yaml
multiscrape:
  - name: War Monitor
    resource: https://t.me/s/war_monitor
    scan_interval: 5
    list_separator: '|||'
    binary_sensor:
      - unique_id: imminent_attack_in_war_monitor
        name: Imminent Attack in War Monitor
        icon: mdi:airplane-clock
        device_class: safety
        select_list: '.js-message_text'
        value_template: >-
          {% set message = value.split("|||") | last | lower %}
          {{ "зліт" in message and "бортів" in message and "ту-95" in message }}
        attributes:
          - name: latest_message
            select_list: '.js-message_text'
            value_template: "{{ value.split('|||') | last }}"
```

So when the sensor turns on, it means the bombers are airborne and it's time to get ready. A notification is sent:

```yaml
alias: 'Alert: Imminent Attack by Strategic Bombers'
description:
  Send a notification when Tu-95 strategic bombers take off from Russian
  airfields. This means an attack by cruise missiles is imminent. Prepare a hideout.
trigger:
  - platform: state
    entity_id:
      - binary_sensor.imminent_attack_in_war_monitor
      - binary_sensor.imminent_attack_in_operinform
    from: 'off'
    to: 'on'
action:
  - service: script.announcement
    data:
      service: notify.all
      speak: false
      notify: true
      title: 'Bombers take off 🛫'
      messages:
        - '{{ trigger.to_state.attributes.latest_message }}'
```

## Direct Danger Alert

This is the most interesting sensor, which notifies me right when there's a direct threat to my location.

When an attack happens at night, you need to decide:

- Are you going to the shelter to get a sleepless night somewhere in a basement or in the subway?
- Or are you going to stay in bed as long as possible to get some sleep, because you need to go to work tomorrow?

Every normal person would go to the shelter. But when you live in these conditions for some time, you try to calculate the risk:

- You need to get proper sleep to be able to work.
- The air defenses are titans; they do their job excellently. Flying threats are getting shot down regularly.
- In Kyiv, the risk of a direct hit or hit by debris is relatively tolerable: I guess like being hit by a car (this estimate is completely unscientific!).
- If you are unlucky to catch a direct hit – you are dead anyway. There's very little chance to survive that.
- If the missile/drone gets shot down nearby, the shockwave will blow your windows.

So what do you do? It's up to you, but most of the time, I decide to sleep in bed. When things get hot, I hide in a bathroom so that when something blows up nearby, [I will be behind two walls](https://visitukraine.today/blog/990/list-of-things-to-put-in-an-emergency-suitcase-and-basic-rules-that-will-save-lives-during-missile-strikes) from glass shards and shockwaves.

I have a sensor that watches for specific keywords like _"Kyiv"_ or a neighborhood name, for _"warning" **or** "be in a safe place" **or** "fast target"_.

```yaml
multiscrape:
  - name: War Monitor
    resource: https://t.me/s/war_monitor
    scan_interval: 5
    list_separator: '|||'
    binary_sensor:
      - unique_id: danger_in_war_monitor
        name: Danger in War Monitor
        icon: mdi:rocket-launch
        device_class: safety
        select_list: '.js-message_text'
        value_template: >-
          {% set message = value.split("|||") | last | lower %}
          {% set in_kyiv = "київ" in message or "святошин" in message %}
          {% set danger_now = "уважно" in message
              or "швидкісна ціль" in message
              or "подалі від зовнішніх стін" in message
              or "безпечних місцях" in message
          %}
          {{ danger_now and in_kyiv }}
        attributes:
          - name: latest_message
            select_list: '.js-message_text'
            value_template: "{{ value.split('|||') | last }}"
```

When this sensor turns on, it means there's a direct danger to me and I should hide immediately. I send a critical notification, speak a danger message on speakers, so I can quickly wake up and go to the hideout.

```yaml
alias: 'Alert: Danger in Kyiv'
description: Danger of missile/drone strike in Kyiv RIGHT NOW. Critical alert to
  hide immediately.
trigger:
  - platform: state
    entity_id:
      - binary_sensor.danger_in_war_monitor
      - binary_sensor.danger_in_operinform
    from: 'off'
    to: 'on'
action:
  - alias: Send a critical notification
    service: script.announcement
    data:
      service: notify.all
      speak: false
      notify: true
      title: Direct Danger ⚠️
      messages:
        - '{{ trigger.to_state.attributes.latest_message }}'
      notify_data:
        group: air-alerts
        push:
          sound:
            name: default
            critical: 1
            volume: 1
  - variables:
      messages:
        - Увага! Пряма загроза удару!
        - Увага загроза удару по Києву!
        - Увага! Негайно перейдіть до сховку!
        - Увага! Негайно сховайтесь!
        - Увага! Пряма загроза!
        - Увага! Негайно сховайтесь!
        - Увага! Атака на Київ!
  - service: media_player.volume_set
    entity_id:
    data:
      volume_level: 0.6
    target:
      device_id: media_player.bedroom_homepod
  - alias: Speak in Bedroom
    service: script.announcement
    data:
      speak: true
      speaker: media_player.bedroom_homepod
      notify: false
      force_speak: true
      messages: '{{ messages }}'
  - delay:
      hours: 2
```
