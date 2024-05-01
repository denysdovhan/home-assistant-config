# Health Checks

Things will break, this is a matter of time. The electricity outage, crashes, interference, etc.

You just must be prepared.

## Home Assistant Instance

I use [HealthChecks.io](https://healthchecks.io) service no notify me when my Home Assistant instance is down (critical crash, an Internet connection is lost, etc).

![HealthChecks Panel](https://user-images.githubusercontent.com/3459374/109878460-00234600-7c7d-11eb-9ea6-eda004d8ede1.png)

This service is dead-simple: it expects you to send requests at the specified time. As long as requests are received, everything is considered to be normal.

When HealthChecks doesn't receive a request at the specified time, it will send me alerts via SMS.

<!-- prettier-ignore -->
!!! question "Why SMS?"
    Because Home Assistant is offline and can't send me a notification via Internet, so SMS is the only reliable option.

I've made a `rest_command` to send a request to HealthChecks:

```yaml
rest_command:
  healthcheck:
    url: !secret healthcheck_ping
```

Automation to send a request every minute:

```yaml
- id: healthcheck
  alias: Healthcheck Connection
  description: Send a ping to Healthcheck every minute
  mode: single
  trigger:
    platform: time_pattern
    minutes: /1
  action:
    - service: rest_command.healthcheck
```

## Unavailable Devices

Sometimes, my devices go offline when Home Assistant is updating or restarting for a long time.

I made a sensor that checks the number of devices for `unavailable`, `unknown`, or `none` states. This sensor also includes their `entity_id`s and `friendly_names` to use in automation.

```yaml
- platform: template
  sensors:
    unavailable_devices:
      friendly_name: Unavailable Devices
      value_template: >-
        {% set domains = [states.light, states.media_player, states.fan] %}
        {% set states = ['unavailable', 'unknown', 'none'] %}
        {{ expand(domains) | selectattr('state', 'in', states) | list | length }}
      attribute_templates:
        entities: >-
          {% set domains = [states.light, states.media_player, states.fan] %}
          {% set states = ['unavailable', 'unknown', 'none'] %}
          {{ expand(domains) | selectattr('state', 'in', states) | map(attribute='entity_id') | list }}
        entities_names: >-
          {% set domains = [states.light, states.media_player, states.fan] %}
          {% set states = ['unavailable', 'unknown', 'none'] %}
          {{ expand(domains) | selectattr('state', 'in', states) | map(attribute='name') | list }}
```

This is automation that sends an alert every time there's more that 0 unavailable devices.

```yaml
- id: unavailable_devices_notifications
  alias: Unavailable Devices Alert
  trigger:
    platform: numeric_state
    entity_id: sensor.unavailable_devices
    above: 0
    for:
      minutes: 1
  action:
    # Notify yourself about these devices
```
