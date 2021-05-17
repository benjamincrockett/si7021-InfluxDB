# si7021-InfluxDB
This project reads a Si7021 temperature and humidity sensor attached to the GPIO pins of a Raspberry Pi 4B and writes the data to an InfluxDB 2 database.

# Hardware
Raspberry Pi 4 4GB or 8GB
Adafruit Si7021 Temperature & Humidity Sensor Breakout Board 
https://www.adafruit.com/product/3251

# Software
Raspberry Pi OS 64-bit beta
    https://www.raspberrypi.org/forums/viewtopic.php?t=275370

InfluxDB v2.0.0-rc.3 
    This is the latest version of InfluxDB v2.0 that is available at this time for an arm64 architecture.
    https://github.com/influxdata/influxdb/releases

Python 3.6 or Later

# Down and Dirty Setup
sudo apt update
sudo apt upgrade
sudo pip3 install influxdb-client 
sudo pip3 install adafruit-circuitpython-si7021

Enable the I2C Pins

Power off the Raspberry Pi 4 and attach the Adafruit Si7021 breakout board to the Raspberry Pi 4.

Power the Raspberry Pi 4 back up, download, and install InfluxDB v2
sudo dpkg -i influxdb_2.0.0-rc.3_arm64.deb

Start InfluxDB using the command 
influxd

Open a web browser and go to localhost:8086

export INFLUX_TOKEN=YourAuthenticationToken
Use INFLUX_TOKEN in place of token in code.
