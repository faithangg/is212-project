SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `sbrp`
--
CREATE DATABASE IF NOT EXISTS `sbrp` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `sbrp`;


DROP TABLE IF EXISTS `access_rights`;
CREATE TABLE IF NOT EXISTS `access_rights`(
    access_right integer NOT NULL,
    user_role varchar(20) NOT NULL,
    CONSTRAINT access_rights_pkey PRIMARY KEY (access_right)
);


DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
    staff_id integer NOT NULL,
    staff_fname varchar(50) NOT NULL,
    staff_lname varchar(50) NOT NULL,
    dept varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    access_rights integer NOT NULL,
    CONSTRAINT staff_pkey PRIMARY KEY (staff_id),
    constraint staff_fk1 foreign key (access_rights) references access_rights(access_right) ON DELETE CASCADE
);

DROP TABLE IF EXISTS `role`;
CREATE TABLE IF NOT EXISTS `role` (
    role_name varchar(20) NOT NULL,
    role_desc longtext NOT NULL,
    CONSTRAINT role_pkey PRIMARY KEY (role_name)
);

CREATE TABLE IF NOT EXISTS `skills` (
    skill_name varchar(50) NOT NULL,
    skill_description varchar(255), -- Optional column to store descriptions of each skill
    CONSTRAINT skills_pkey PRIMARY KEY (skill_name)
);

CREATE TABLE IF NOT EXISTS `role_skill` (
    role_name varchar(20) NOT NULL,
    skill_name varchar(50) NOT NULL,
    CONSTRAINT role_skill_pkey PRIMARY KEY (role_name, skill_name),
    CONSTRAINT role_skill_fk1 FOREIGN KEY (role_name) REFERENCES role(role_name) ON DELETE CASCADE,
    CONSTRAINT role_skill_fk2 FOREIGN KEY (skill_name) REFERENCES skills(skill_name) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `staff_skill` (
    staff_id integer NOT NULL,
    skill_name varchar(50) NOT NULL,
    CONSTRAINT staff_skill_pkey PRIMARY KEY (staff_id, skill_name),
    CONSTRAINT staff_skill_fk1 FOREIGN KEY (skill_name) REFERENCES skills(skill_name) ON DELETE CASCADE,
    CONSTRAINT staff_skill_fk2 FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE
);


DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
    category varchar(20) NOT NULL,
    category_desc varchar(100) NOT NULL,
    CONSTRAINT category_pkey PRIMARY KEY (category)
);

DROP TABLE IF EXISTS `role_listing`;
CREATE TABLE IF NOT EXISTS `role_listing` (
    listing_id integer NOT NULL AUTO_INCREMENT,
    role_name varchar(20) NOT NULL,
    department varchar(100) NOT NULL,
    category varchar(20) NOT NULL,
    deadline date NOT NULL,
    CONSTRAINT role_listing_pkey PRIMARY KEY (listing_id),
    constraint role_listing_fk1 foreign key (category) references category(category) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `job_application`;
CREATE TABLE IF NOT EXISTS `job_application` (
    application_id integer NOT NULL AUTO_INCREMENT,
    staff_id integer NOT NULL,
    role_name varchar(20) NOT NULL,
    application_date date NOT NULL,
    CONSTRAINT job_application_pkey PRIMARY KEY (application_id),
    constraint job_application_fk1 foreign key (staff_id) references staff(staff_id) ON DELETE CASCADE,
    constraint job_application_fk2 foreign key (role_name) references role(role_name) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `login_details`;
CREATE TABLE IF NOT EXISTS `login_details` (
    staff_id integer NOT NULL,
    staff_password varchar(255) NOT NULL,
    CONSTRAINT login_details_pkey PRIMARY KEY (staff_id),
    constraint login_details_fk1 foreign key (staff_id) references staff(staff_id) ON DELETE CASCADE
);



