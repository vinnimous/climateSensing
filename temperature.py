import datetime
import logging
import time

import adafruit_dht
import board

logger = logging.getLogger('temperature')

def assess():
    check_temp()
    temp_status()

def check_temp():
    global temperature, humidity
    dht = adafruit_dht.DHT22(board.D2, use_pulseio=False)

    try:
        temperature = dht.temperature* (9 / 5) + 32
        humidity = dht.humidity
    except Exception as e:
        logger.error("Failed to detect temperature: {}".format(e))


def temp_status():
    from main import upload_temps
    if upload_temps:
        from mySql import insert
        try:
            insert(datetime.datetime.now(), temperature, humidity)
        except Exception as e:
            logger.error("Failed to insert temperature data: {}".format(e))
    logger.debug("Current time: {} Temperature: {} Humidity: {}  ".
                 format(datetime.datetime.now(), temperature, humidity))