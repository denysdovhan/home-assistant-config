# Vacuum Setup

![Vacuum](https://github.com/denysdovhan/home-assistant-config/assets/3459374/5eaa469d-39d4-485a-acdf-77695da4d5aa)

I have a Roborock S5 Max vacuum robot. It's paired with Home Assistant using built-in [Roborock](https://www.home-assistant.io/integrations/roborock/) integration.

I used a [`vacuum-card`](https://github.com/denysdovhan/purifier-card) I built myself for controlling my vacuum and [`lovelace-xiaomi-vacuum-map-card`](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) for displaying a live map.

You can find the latest state of my vacuum setup here:

[Automations](https://github.com/denysdovhan/home-assistant-config/blob/master/automations/vacuum.yaml){: .md-button }
[Scripts](https://github.com/denysdovhan/home-assistant-config/blob/master/scripts/vacuum.yaml){: .md-button }

## Asking to start cleaning

I have a relatively complex set of automation for my vacuum.

At first, I just used to start my robot every couple of days. It's not a good approach, because it always starts vacuuming right in the middle of a working call.

Over time, I've changed logic to more complex and elegant.

Now my vacuum sends an actionable notification asking to start cleaning, based on multiple conditions:

- Robot is docked.
- It's a working day.
- It's a time during working hours.
- Do Not Disturb mode is off. <!-- FIXME: Add link to Do Not Disturb -->
- It's _time to clean_, meaning: the previous cleaning was too short to clean the whole home, _**or**_ there was no cleaning in a reasonable period.

When I think it's a good time to start cleaning, I press a button in the notification, and the robot starts cleaning.

Additionally, the robot starts cleaning every time we leave our home, and it's _time to clean_.

## Asking to clean itself

I solved this issue by automatically sending it to the trash bin after every 5th cleaning.

The tricky part here is to tell the robot where to go. There is an article that helped me solve this issue: [How I set up room-cleaning automation with Google Home, Home-Assistant and Xiaomi vacuum cleaner](https://hackernoon.com/how-i-set-up-room-cleaning-automation-with-google-home-home-assistant-and-xiaomi-vacuum-cleaner-9149e0267e6d)

Using the method described in the article, I've found the location of my trash bin. In my case, it's:

```js
[24500, 24500];
```

Now I can send the vacuum to this spot in my home, like this:

```yaml
vacuum_maintenance:
  alias: Vacuum Maintenance
  icon: mdi:screwdriver
  sequence:
    - service: vacuum.send_command
      entity_id: vacuum.roborock
      data:
        command: app_goto_target
        params: [24500, 24500] # Coordinates near the trash bin
```

## Cleaning the specific room

I made shortcuts for cleaning rooms separately. Here's a guide how to retrieve valid room number: [Retrieving room numbers](https://www.home-assistant.io/integrations/roborock/#how-can-i-clean-a-specific-room).

Here are mine:

```yaml
vacuum.roborock:
  maps:
    - flag: 0
      name: Kyiv Home
      rooms:
        '16': Living Room
        '17': Bedroom
        '18': Corridor
        '19': Bathroom
        '20': Kitchen
```

Using the first number in these tuples, I can send a vacuum to clean a specific room like this:

```yaml
# Single Room
vacuum_clean_kitchen:
  alias: Vacuum Clean Kitchen
  icon: mdi:silverware-fork-knife
  sequence:
    - service: vacuum.send_command
      data:
        entity_id: vacuum.roborock
        command: app_segment_clean
        params: [20]

# Multiple rooms
vacuum_clean_living_room:
  alias: Vacuum Clean Living Room
  icon: mdi:sofa
  sequence:
    - service: vacuum.send_command
      data:
        entity_id: vacuum.roborock
        command: app_segment_clean
        params: [16, 20]
```
