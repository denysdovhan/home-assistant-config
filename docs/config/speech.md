# Speech

I do most of the interactions with my smart home using my voice. This page describes my voice control setup.

## Home Speakers

None of the existing smart speakers supports the Ukrainian language (my native and primary language). I used English (US) for my devices.

My current smart speaker setup consists of two HomePod Minis. I've migrate to Apple speakers from Google ones, because of a better sound and tighter integration with Apple devices, specifically:

- [Intercom feature](https://support.apple.com/uk-ua/guide/homepod/apdc2e0b5480/homepod) is great. When I leave my home I can send a quick voice message for anyone who stay at home.
- HomeKit works locally, without Internet access. I also means that voice requests work faster.
- Sound is significantly better that on Google speakers. Listening to music is much enjoyable, the bass is more punchy.
- [Find My feature](https://support.apple.com/find-my) is also great. I can ask "Where is my phone?" and the phone will ring.
- Handoff is nice, though it doesn't work well in Ukraine.

There's also a downside of using HomePods: I still can't sync audio for Home Assistant voice announcements between speakers.

<!-- prettier-ignore -->
??? note "Previous setup with Google speakers"
    I have two Google smart speakers. I've decided to go with Google because Google Assistant is smart enough and well-integrated with different accessories.

    We use these speakers all the time, mostly asking to turn devices, activate scenes, start or stop vacuum, set timers or reminders. Besides, lack of Ukrainian language support, I'm pretty happy with these speakers. Sometimes I need to repeat my command twice for the speaker to pick up, but I consider it acceptable.

    === "Google Home Mini"

        I got this one as a gift for New Year 2020.

        ![IMG_0194](https://user-images.githubusercontent.com/3459374/109870391-b59ccc00-7c72-11eb-8aeb-e1dd411eac0d.JPG){: width=50% }

    === "Google Nest Mini"

        This one I got as a gift for my birthday.

        ![IMG_5508](https://user-images.githubusercontent.com/3459374/109870407-ba618000-7c72-11eb-9071-6c1f197d4bef.jpeg){: width=50% }

## Text to Speech

I wanted to receive voice announcements for my smart home in Ukrainian. Fortunately, [Google Translate TTS](https://www.home-assistant.io/integrations/google_translate/) supports voice generation for the Ukrainian language.

```yaml
tts:
  - platform: google_translate
    service_name: google_say
    language: uk # Ukrainian
```

This will generate phrases and send them to any speaker to play.

### Announcements

I built a nice announcements script for myself. I use it like this:

```yaml
service: script.announcement
data:
  # Speak on smart speakers
  speak: true
  # Send notifications on devices
  notify: true
  # Title for notification
  title: 'Миття авто 🚘☀️'
  # Opening phrases
  openings:
    - 'Найближчими днями очікується хороша погода.'
    - 'Хороша погода найближчі 7 днів.'
    - 'Прогнозується хороша погода!'
  # Main phrases
  messages:
    - 'Доречно помити машину.'
    - 'Варто поїхати на автомийку.'
    - 'Вдалий час, щоб помити авто.'
  # Additional data for notifications
  # Categories or page to open on notification opening
  notify_data:
    url: /lovelace/car
```

This script will generate a unique announcement using random phrases from `openings` and `messages`.

The generated phrase will be spoken on smart speakers and sent as a notification to the phones. I can avoid speaking or notifying via `speak` and `notify` flags accordingly.

`notify_data` helps to pass notification categories for actionable notifications or `url` to open when I click on this notification.

## Do Not Disturb Flow

It would be annoying to get a speech announcement in the middle of the night or a working meeting. That's why I built **Do Not Disturb** mode.

**Do Not Disturb** is just automation that:

- Sets the volume of smarts speakers
- Turns on/off silence modes for fans
- Turns on/off led indicators
- Stops/starts voice announcements

… based on the current time of day (sleeping or activity time) and a switch, I can toggle whenever I want.
