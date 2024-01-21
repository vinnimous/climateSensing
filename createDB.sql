FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS atticClimateDB;

CREATE USER IF NOT EXISTS 'grafanauser'@'localhost' identified BY 'grafanauserPW';

GRANT all privileges ON atticClimateDB.* TO 'grafanauser'@'localhost';

FLUSH PRIVILEGES;

USE atticClimateDB;

CREATE TABLE IF NOT EXISTS atticClimateTable (
    DATE DATETIME,
    HUMIDITY FLOAT,
    TEMPERATURE FLOAT
);