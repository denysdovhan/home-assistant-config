# Dashboards

Below you're going to find my dashboards. I use those to display information and control accessories in my smart home.

<!-- prettier-ignore -->
!!! warning
    I constantly update my smart home setup and tweaking UI to match my needs. Please, beware that the look of these dashboards on screenshots might differ from how they actually look right now.

    Please, [visit the repo](https://github.com/denysdovhan/smart-home/) to see the current state of these dashboards.

I use [`mini-media-player`](https://github.com/kalkih/mini-media-player) card for the media players and [`mini-graph-card`](https://github.com/kalkih/mini-graph-card) for the graphs.

## Home

This dashboard displays the information about my home in general.

- **Room buttons** navigate to the room dashboards on the press, and turn off all lights in the room on hold.
- **Scenes** controls of the scenes are located at the beginning of the dashboard to be accessible on the phone right away.
- **Media** block helps to control my smart speakers and Spotify.
- **Conditions** contain information about the weather, indoor temperature, humidity, and pressure, UV-index outdoors, and AQI indoor as well as outdoor (from the nearby AQI station).
- **Live Camera** shows a livestream of what is going on at home.
- **Status** display the information about our location and travel history for the last hours.

![Home Overview](https://github.com/denysdovhan/smart-home/assets/3459374/6085c456-0842-4313-934b-44245888c59f)

Room buttons navigate to subviews for each of the room, displaying controls for lights, speakers, showing room conditions.

=== "Living Room"

    ![Living Room](https://github.com/denysdovhan/home-assistant-config/assets/3459374/65ed0e5a-e736-4e00-8d03-5a6b245b36d3)

=== "Bedroom"

    ![Bedroom](https://github.com/denysdovhan/home-assistant-config/assets/3459374/10993656-8fb3-403f-bf5d-a88ef3466aa9)

=== "Balcony"

    ![Balcony](https://github.com/denysdovhan/home-assistant-config/assets/3459374/ce707134-27ee-4bc2-a9fd-f3476c38bc4e)

=== "Bathroom"

    ![Bathroom](https://github.com/denysdovhan/home-assistant-config/assets/3459374/7a187703-5678-444b-bb11-a0b7b06f65e4)

## Vacuum

This dashboard is for controlling a vacuum cleaner robot. **Vacuum card** for controlling a vacuum cleaner and scrips for quick access to the vacuum, which is hidden under the bed. I developed my own [`vacuum-card`](https://github.com/denysdovhan/vacuum-card) for vacuum management.

![Vacuum](https://github.com/denysdovhan/home-assistant-config/assets/3459374/5eaa469d-39d4-485a-acdf-77695da4d5aa)

## City

This dashboard is created for monitoring city conditions.

- **Air Quality** displays AQI in my neighbourhood and Kyiv average, PM2.5 concentration indoor/outdoor and AQI map.
- **Traffic** displays realtime traffic map, congestion and traveltime to/from city center.

![City Statistics](https://github.com/denysdovhan/home-assistant-config/assets/3459374/0b895a55-a7ab-42df-8478-c0be400b03db)

## System

This dashboard lets me overview the state of my smart home SystemHealthRegistration

- **Internet and System** section displays the Internet speed, ping, and connected devices. Below there are a group of sensor for CPU, RAM, Swap and Disk usage of my Raspberry Pi.
- **PiHole** let me monitor the DNS ad-blocking rates.

![System](https://github.com/denysdovhan/home-assistant-config/assets/3459374/0cb9d64b-bb0f-4faf-8b7e-88852ecbd03b)

<!-- prettier-ignore -->
??? note "State of UI at 2022"

    ## Home

    ![Home](https://user-images.githubusercontent.com/3459374/152371766-1d2a1e17-34d3-4fe6-9e6d-aded02f14de1.png){: loading=lazy }

    ## Living Room

    ![Living Room](https://user-images.githubusercontent.com/3459374/152372151-be201bd1-cef9-4ce5-a59d-fd1b534934dc.png){: loading=lazy }

    ## Bedroom

    ![Bedroom](https://user-images.githubusercontent.com/3459374/152372530-703121d2-2a96-4acc-a664-65109447ab93.png){: loading=lazy }

    ## Balcony

    ![Balcony](https://user-images.githubusercontent.com/3459374/152372756-a14bbc12-cd40-4549-b93b-6205d8356ce9.png){: loading=lazy }

    ## Vacuum

    ![Vacuum](https://user-images.githubusercontent.com/3459374/152373217-a5ebc40c-3d62-4575-8cbc-736ca1641c8c.png){: loading=lazy }

    ## Car

    This dashboard lets me control my Toyota vehicle.

    - **Alarm controls** let my arm/disarm my smart alarm, start/stop the engine, trigger horn.
    - **History map** display the 24-hour path history of the vehicle.
    - **States** are displaying the sensor states of the hood, doors, trunk, engine and interior temperature, connection quality.

    <!-- prettier-ignore -->
    !!! info
        You may see that most of the controls and sensors are unavailable on the screenshots. That's because I keep my car in the underground parking, where the GSM connection is poor.

        Though, there's no need to worry, since the parking is secured with many security systems.

    ![Car](https://user-images.githubusercontent.com/3459374/152373434-9334d8a3-f715-4ea1-8e09-6d9038473bbe.png){: loading=lazy }

    ## City

    This dashboard is created for monitoring city conditions.

    - **Air Quality** displays AQI in my neighbourhood and Kyiv average, PM2.5 concentration indoor/outdoor and AQI map.
    - **Traffic** displays realtime traffic map, congestion and traveltime to/from city center.

    ![City](https://user-images.githubusercontent.com/3459374/152373679-5555a14a-8a1d-4015-8a71-e9d821cf30cb.png)

    ## Observation

    This dashboard displays status of my plants, position of the sun, etc.

    ![Observation](https://user-images.githubusercontent.com/3459374/152374474-e6e0c9f4-949d-4471-8820-e5e6cf59a928.png){: loading=lazy }

    ## Cameras

    This dashboard lets me watch the live streams from Kyiv (where I live) and from Chernivtsi (where I've grown up). Unfortunately, there is a very small number of publicly accessible live cameras in Kyiv. Most of them are unstable and have very poor quality.

    ![Cameras](https://user-images.githubusercontent.com/3459374/115126127-92856c00-9fd5-11eb-93a3-0c7621cd2d53.png){: loading=lazy }

    ## System

    This dashboard lets me overview the state of my smart home SystemHealthRegistration

    - **Internet and System** section displays the Internet speed, ping, and connected devices. Below there are a group of sensor for CPU, RAM, Swap and Disk usage of my Raspberry Pi.
    - **Adguard Home** let me monitor the DNS ad-blocking rates.

    ![System](https://user-images.githubusercontent.com/3459374/152374825-4e564a75-7c8d-4001-b71a-00dcd5291e73.png){: loading=lazy }
