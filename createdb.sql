FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS atticClimateDB;

create user 'grafanauser'@'localhost' identified by 'grafanauserPW';

grant all privileges on atticClimateDB.* to 'grafanauser'@'localhost';

FLUSH PRIVILEGES;

USE atticClimateDB;

CREATE TABLE IF NOT EXISTS atticClimateTable (
    DATE DATETIME,
    HUMITITY FLOAT,
    TEMPERATURE FLOAT
);