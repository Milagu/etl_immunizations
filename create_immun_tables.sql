mysql -uroot -p -h127.0.0.1 sakila

create database etl_project;

use etl_project;



---------------------------------------------------
-- states table
---------------------------------------------------

create table states
(
   state_pk_id    smallint(5) unsigned not null auto_increment
  ,state_nm       varchar(30)
  ,state_abbr     varchar(2)
  ,primary key    (state_pk_id)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8;

---------------------------------------------------
-- counties table
---------------------------------------------------

CREATE TABLE `etl_project`.`counties` (
  `counties_pk_id` SMALLINT(5) NOT NULL AUTO_INCREMENT,
  `state_id` SMALLINT(5) UNSIGNED NULL,
  `county_nm` VARCHAR(50) NULL,
  PRIMARY KEY (`counties_pk_id`),
  CONSTRAINT `state_id`
    FOREIGN KEY (`state_id`)
    REFERENCES `etl_project`.`states` (`state_pk_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


---------------------------------------------------
-- county_populations table
---------------------------------------------------

CREATE TABLE `etl_project`.`county_populations` (
  `county_pop_pk_id` SMALLINT(5) NOT NULL AUTO_INCREMENT,
  `county_id` SMALLINT(5) NULL,
  `year_de` VARCHAR(4) NULL,
  `population_nr` MEDIUMINT(10) NULL,
  PRIMARY KEY (`county_pop_pk_id`),
  CONSTRAINT `fk_county_id`
    FOREIGN KEY (`county_pop_pk_id`)
    REFERENCES `etl_project`.`counties` (`counties_pk_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

---------------------------------------------------
-- schools table
---------------------------------------------------

CREATE TABLE `etl_project`.`schools` (
  `school_pk_id` SMALLINT(5) NOT NULL AUTO_INCREMENT,
  `school_nm` VARCHAR(100) NULL,
  `county_id` SMALLINT(5) NULL,
  PRIMARY KEY (`school_pk_id`),
  INDEX `fk_schools_county_id_idx` (`county_id` ASC),
  CONSTRAINT `fk_schools_county_id`
    FOREIGN KEY (`county_id`)
    REFERENCES `etl_project`.`counties` (`counties_pk_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
