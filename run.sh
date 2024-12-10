#!/bin/bash

# This script will run monitor_air.py
# Upper and lower bounds for PM2.5 and PM10 i.e. the thresholds for turning air filter on and off
# Default values of WHO guidelines for PM2.5 and PM10 exposure 
# https://www.who.int/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines
pm25_ub=12
pm25_lb=5
pm10_ub=45
pm10_lb=15


while [ "$1" != "" ]; do
    param=${1%%=*}
    value=${1#*=}
    case $param in
        --pm25-ub)
            pm25_ub=$value
            ;;
        --pm25-lb)
            pm25_lb=$value
            ;;
        --pm10-ub)
            pm10_ub=$value
            ;;
        --pm10-lb)
            pm10_lb=$value
            ;;
        *)
            echo "Unknown argument $param"
            exit 1
            ;;
    esac
    shift
done


# Activate the virtual environment
source "$HOME/.virtualenvs/pimoroni/bin/activate"

python3 ./monitor_air/monitor_air.py --pm25-ub=$pm25_ub --pm25-lb=$pm25_lb --pm10-ub=$pm10_ub --pm10-lb=$pm10_lb


if [ $? -eq 0 ]; then
    echo "Air monitoring script ran successfully with PM2.5 upper bound=$pm25_ub, PM2.5 lower bound=$pm25_lb, PM10 upper bound=$pm10_ub, PM10 lower bound=$pm10_lb"
else
    echo "Air monitoring script encountered an error during execution."
fi