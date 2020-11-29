# si7021-InfluxDB
This project reads a Si7021 temperature and humidity sensor attached to the GPIO pins of a Raspberry Pi 4B and writes the data to an InfluxDB 2 database.

# Hardware
Raspberry Pi 4 4GB or 8GB
Adafruit Si7021 Temperature & Humidity Sensor Breakout Board 

# Software
Raspberry Pi OS 64-bit beta
    https://www.raspberrypi.org/forums/viewtopic.php?t=275370

InfluxDB v2.0.0-rc.3 
    This is the latest version of InfluxDB v2.0 that is available for arm64.
    https://github.com/influxdata/influxdb/releases

Python3
    pip3 install influxdb-client 