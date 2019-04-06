DROP DATABASE IF EXISTS immunization_db;
CREATE DATABASE immunization_db;

USE immunization_db;

#['index', 'county', 'school_year', 'number_reported', 'number_completed', 'pop_2016']
DROP TABLE IF EXISTS wa_immunizations
CREATE TABLE wa_immunizations (
  id INT AUTO_INCREMENT,
  county VARCHAR(20) NOT NULL,
  school_year VARCHAR(20) NOT NULL,
  number_reported INT,
  number_completed INT,
  pop_2016 DOUBLE,
  PRIMARY KEY(id)
);