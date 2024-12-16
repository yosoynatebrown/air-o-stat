# Air-O-Stat

This Python script reads PM2.5 and PM10 particle measurements from a PMS5003 air quality sensor and controls an air filter using a relay module (power strip) connected to a Raspberry Pi. It is configured to turn the air filter on or off based on specified upper and lower bounds for PM2.5 and PM10 levels.

The script sets up the GPIO mode and configures GPIO pin 17 as an output to control the air filter.
It continuously reads data from the PMS5003 sensor.
If the PM2.5 or PM10 levels exceed the specified upper bounds, the air filter is turned on.
If the PM2.5 and PM10 levels fall below the specified lower bounds, the air filter is turned off.

# Features
- Reads PM2.5 and PM10 data from a PMS5003 sensor.
- Controls an air filter via a power strip relay (connected to GPIO pin 17).
- Configurable thresholds for PM2.5 and PM10 with command-line arguments.
- Option to enable verbose output for detailed measurements.
# Prerequisites
- Raspberry Pi with Raspbian or compatible OS.
- PMS5003 air quality sensor.
- Particulate Matter Sensor Breakout (for PMS5003)
- Python 3.
- RPi.GPIO library for GPIO pin control.
- pms5003 Python library for interacting with the sensor.
# Installation
- This is a fork of Pimoroni's PMS5003 Particulate Sensor library, first follow their installation instructions [here.](https://github.com/pimoroni/pms5003-python)
- Ensure Python 3 and pip are installed.
- Install the necessary Python libraries:
`pip install RPi.GPIO pms5003`
# Usage

Command-Line Arguments
```--verbose, -v: Enable verbose output.
--pm25-ub: Set the PM2.5 upper bound threshold (default: 12).
--pm25-lb: Set the PM2.5 lower bound threshold (default: 5).
--pm10-ub: Set the PM10 upper bound threshold (default: 45).
--pm10-lb: Set the PM10 lower bound threshold (default: 15).
```
# Example

Run the script with the default values:
`./run.sh`

Run the script with custom PM2.5 and PM10 thresholds and enable verbose mode:
`./run.sh --pm25-ub=15 --pm25-lb=8 --pm10-ub=50 --pm10-lb=20 --verbose`

When running in verbose mode, the script will print the current PM2.5 and PM10 measurements:
```
PM2.5 ug/m3 (combustion particles, organic compounds, metals): 10.5
PM10 ug/m3  (dust, pollen, mould spores): 30.2
Turning air filter on...
```
