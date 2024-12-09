#!/usr/bin/env python
import RPi.GPIO as GPIO
import argparse
from pms5003 import PMS5003

pms5003 = PMS5003(device="/dev/ttyS0", baudrate=9600)

parser = argparse.ArgumentParser()

# default values are WHO guidelines for PM2.5 and PM10 exposure https://www.who.int/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines
parser.add_argument('--verbose', '-v', action='store_true', help="Enable verbose output")
parser.add_argument('--pm25-ub', '-pm25-ub', default=12, type=int, help="Specify the PM2.5 upper bound threshold")
parser.add_argument('--pm25-lb', '-pm25-lb', default=5, type=int, help="Specify the PM2.5 lower bound threshold")
parser.add_argument('--pm10-ub', '-pm10-ub', default=45, type=int, help="Specify the PM10 upper bound threshold")
parser.add_argument('--pm10-lb', '-pm10-lb', default=15, type=int, help="Specify the PM10 lower bound threshold")

# Parse the arguments
args = parser.parse_args()


try:
  # power strip/relay setup
  GPIO.setmode(GPIO.BCM)
  
  GPIO.setup(17, GPIO.OUT)
  enabled = False
  while True:
      #read PM2.5 and PM10 particle measurements from PMS5003
      data = pms5003.read()
      pm25 = data.pm_ug_per_m3(2.5)
      pm10 = data.pm_ug_per_m3(10)
      if args.verbose:
        print(f"PM2.5 ug/m3 (combustion particles, organic compounds, metals): {pm25}")
        print(f"PM10 ug/m3  (dust, pollen, mould spores): {pm10}")
      if not enabled and (pm25 > args.pm25_ub or pm10 > args.pm10_ub):
          print("Turning air filter on...")
          GPIO.output(17, GPIO.HIGH)
          enabled = True
      elif enabled and pm25 < args.pm25_lb and pm10 < args.pm10_lb:
          print("Turning air filter off...")
          GPIO.output(17, GPIO.LOW)
          enabled = False

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
