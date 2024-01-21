#!/usr/bin/python3

import datetime
import logging.config
import time
from os import path

from temperature import assess

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

logging.config.fileConfig(log_file_path)
logger = logging.getLogger('main')

logger.debug("Starting")
run_for_ever = True
upload_temps = True
update_interval = 3600 #sleeping for 1 hour

while run_for_ever:
    try:            
        if upload_temps:
            from mySql import delete_old
            delete_old()
        assess()
        time.sleep(update_interval)
    except Exception as e:
        logger.exception(e)