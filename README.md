
# MOTIONLIVE – IoT Security Monitoring System

## Project Overview

MOTIONLIVE is an IoT-based security monitoring system developed using Raspberry Pi 4 and a PIR motion sensor.

The system detects human movement and activates an LED indicator and buzzer alarm when motion is detected. It also sends motion detection data to the ThingSpeak cloud platform for remote monitoring.

## Project Objectives

- Detect human movement using a PIR sensor.
- Activate an LED alert when movement is detected.
- Trigger a buzzer alarm when motion is detected.
- Send motion status data to ThingSpeak.
- Display monitoring results through a cloud dashboard.

## Hardware Components

- Raspberry Pi 4 Model B (1GB)
- PIR Motion Sensor
- Red LED
- Buzzer
- 220-ohm Resistor
- Breadboard
- Jumper Wires
- 5V 3A USB-C Adapter
- Micro SD Card

## Software and Technologies

- Python
- Raspberry Pi OS
- ThingSpeak Cloud
- PuTTY
- TigerVNC

## System Features

1. Motion Detection
2. LED Alert Indicator
3. Buzzer Alarm System
4. Real-Time Cloud Monitoring
5. Automated System Operation
6. Data Visualization Dashboard
7. Wi-Fi Connectivity

## Project Structure

```text
motionlive-iot-security-system/
├── src/
│   └── motionlive.py
├── screenshots/
├── diagrams/
├── report/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Install the required Python library:

```bash
pip install -r requirements.txt
```

## Configuration

Set your ThingSpeak Write API Key as an environment variable:

```bash
export THINGSPEAK_WRITE_API_KEY="YOUR_API_KEY"
```

Never publish your actual API key.

## Running the Project

Run the Python program on a compatible Raspberry Pi:

```bash
python3 src/motionlive.py
```

## Project Information

- Project Name: MOTIONLIVE
- Course: SDT 2133 – IoT Application & Software
- Programme: Diploma in Software Engineering
- Institution: German-Malaysian Institute (GMI)
- Academic Period: January 2026

## Future Improvements

- Integrate a camera module.
- Add multiple PIR sensors.
- Develop a mobile application.
- Improve remote notification features.
