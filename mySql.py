import logging
from configparser import ConfigParser
from os import path

import pymysql

logger = logging.getLogger('mySql')
sqlArchiveLimit = 365


def read_db_config(filename='config.ini', section='mysql'):
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(path.join(path.dirname(path.abspath(__file__)), filename))

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


def insert(date, temperature, humidity):
    db_config = read_db_config()
    db = pymysql.connect(**db_config)
    cursor = db.cursor()
    sql = "INSERT INTO atticClimateTable ( \
        DATE, \
        TEMPERATURE, \
        HUMIDITY \
    ) VALUES ( '%s', '%s', '%s')" % \
          (date, temperature, humidity)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        logger.error("Failed to insert record from table: {}".format(e))
        db.rollback()
    finally:
        cursor.close()
        db.close()


def delete_old():
    db_config = read_db_config()
    db = pymysql.connect(**db_config)
    cursor = db.cursor()
    del_stmt = "DELETE FROM atticClimateTable WHERE DATE < NOW() - interval %s DAY;"
    find_old = "SELECT * FROM atticClimateTable WHERE DATE < NOW() - interval %s DAY;"
    adr = (sqlArchiveLimit,)
    try:
        cursor.execute(find_old, adr)
        records = cursor.fetchall()
        if len(records) > 0:
            cursor.execute(del_stmt, adr)
            db.commit()
            logger.debug(cursor.rowcount, " records deleted")
        else:
            logger.debug("No old records exsist")
    except Exception as e:
        logger.error("Failed to delete record from table: {}".format(e))
        db.rollback()
    finally:
        cursor.close()
        db.close()