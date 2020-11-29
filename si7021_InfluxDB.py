import time
import board
import busio
import adafruit_si7021
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

# You can generate a Token from the "Tokens Tab" in the UI
token = "<Your Token Goes Here>"
org = "<Your Organization Goes Here>"
bucket = "<Your Data Bucket Goes Here>"

# Variables
temperature = 0.0
relative_humidity = 0.0

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

while True:
    temperature = sensor.temperature
    relative_humidity = sensor.relative_humidity

    sequence = ["weather,node=node1 temperature={}".format(temperature),
                "weather,node=node1 relative_humidity={}".format(relative_humidity),
                "system,node=node1 battery_voltage=4.200000"]
    write_api.write(bucket, org, sequence)

    print("\nTemperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    time.sleep(60) 