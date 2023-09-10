-- Creates database joji_db
CREATE DATABASE IF NOT EXISTS joji_db;
USE joji_db;
CREATE USER 'joji_dev'@'localhost' IDENTIFIED BY 'joji_dev_pwd';
GRANT ALL PRIVILEGES ON joji_db.* TO 'joji_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'joji_dev'@'localhost';
