# Monitoring

Things will break, this is a matter of time. The electricity outage, crashes, interference, etc.

You just must be prepared.

## Home Assistant Instance

I use [UptimeRobot](https://uptimerobot.com/) service no notify me when my Home Assistant instance is down (critical crash, an Internet connection is lost, etc).

![UptimeRobot Panel](https://github.com/denysdovhan/home-assistant-config/assets/3459374/477ef2a0-f337-48de-9e03-d6f81a6558a9)

This service checks whether the page is available online. When it's not, it send an email and a push-notification to my phone.

## Low Batteries and Unavailable Devices

I use [a blueprint](https://community.home-assistant.io/t/low-battery-notifications-actions/653754) to get notifications for low batteries and unavailable devices:

It has a lot of features, but I primarily just pass the list of exceptions and send a notification as a custom action.
