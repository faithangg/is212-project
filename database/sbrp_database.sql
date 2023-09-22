SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `sbrp`
--
CREATE DATABASE IF NOT EXISTS `sbrp` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `sbrp`;

DROP TABLE IF EXISTS `staff_skill`;
DROP TABLE IF EXISTS `role_skill`;
DROP TABLE IF EXISTS `role_listing`;
DROP TABLE IF EXISTS `login_details`;
DROP TABLE IF EXISTS `job_application`;
DROP TABLE IF EXISTS `role`;
DROP TABLE IF EXISTS `category`;
DROP TABLE IF EXISTS `staff`;   
DROP TABLE IF EXISTS `skills`;   


DROP TABLE IF EXISTS `access_rights`;
CREATE TABLE IF NOT EXISTS `access_rights`(
    access_right integer NOT NULL,
    user_role varchar(20) NOT NULL,
    CONSTRAINT access_rights_pkey PRIMARY KEY (access_right)
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO access_rights (access_right, user_role) VALUES
(1, 'HR'),
(2, 'Staff');


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
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO staff (staff_id, staff_fname, staff_lname, dept, email, access_rights) VALUES
(1, 'John', 'Doe', 'HR', 'john.doe@example.com', 2),
(2, 'Jane', 'Smith', 'IT', 'jane.smith@example.com', 1), -- Changed to 1
(3, 'Bob', 'Johnson', 'Finance', 'bob.johnson@example.com', 1); -- Changed to 1

DROP TABLE IF EXISTS `role`;
CREATE TABLE IF NOT EXISTS `role` (
    role_name varchar(20) NOT NULL,
    role_desc longtext NOT NULL,
    CONSTRAINT role_pkey PRIMARY KEY (role_name)
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO role (role_name, role_desc) VALUES
('HR Manager', 'Human Resources Manager role'),
('Software Engineer', 'Software Engineering role'),
('Financial Analyst', 'Financial Analysis role'),
('Network Administrator', 'Network Administration role');


DROP TABLE IF EXISTS `skills`;
CREATE TABLE IF NOT EXISTS `skills` (
    skill_name varchar(50) NOT NULL,
    CONSTRAINT skills_pkey PRIMARY KEY (skill_name)
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO skills (skill_name) VALUES
('Python'),
('SQL'),
('Finance'),
('Statistical Analysis'),
('Excel'),
('Data Visualization'),
('Networking'),
('Cybersecurity'),
('Operating Systems'),
('Cloud Services'),
('Problem Solving'),
('Troubleshooting');

DROP TABLE IF EXISTS `role_skill`;
CREATE TABLE IF NOT EXISTS `role_skill` (
    role_name varchar(20) NOT NULL,
    skill_name varchar(50) NOT NULL,
    CONSTRAINT role_skill_pkey PRIMARY KEY (role_name, skill_name),
    CONSTRAINT role_skill_fk1 FOREIGN KEY (role_name) REFERENCES role(role_name) ON DELETE CASCADE,
    CONSTRAINT role_skill_fk2 FOREIGN KEY (skill_name) REFERENCES skills(skill_name) ON DELETE CASCADE
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO role_skill (role_name, skill_name) VALUES
('HR Manager', 'Problem Solving'),
('Software Engineer', 'Python'),
('Software Engineer', 'SQL'),
('Financial Analyst', 'Statistical Analysis'),
('Financial Analyst', 'Excel'),
('Financial Analyst', 'Data Visualization'),
('Financial Analyst', 'SQL'),
('Network Administrator', 'Networking'),
('Network Administrator', 'Cybersecurity'),
('Network Administrator', 'Operating Systems'),
('Network Administrator', 'Cloud Services'),
('Network Administrator', 'Troubleshooting');

DROP TABLE IF EXISTS `staff_skill`;
CREATE TABLE IF NOT EXISTS `staff_skill` (
    staff_id integer NOT NULL,
    skill_name varchar(50) NOT NULL,
    CONSTRAINT staff_skill_pkey PRIMARY KEY (staff_id, skill_name),
    CONSTRAINT staff_skill_fk1 FOREIGN KEY (skill_name) REFERENCES skills(skill_name) ON DELETE CASCADE,
    CONSTRAINT staff_skill_fk2 FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO staff_skill (staff_id, skill_name) VALUES
(1, 'Python'),
(2, 'SQL'),
(3, 'Finance');


DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
    category varchar(120) NOT NULL,
    category_desc varchar(100) NOT NULL,
    CONSTRAINT category_pkey PRIMARY KEY (category)
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO category (category, category_desc) VALUES
('Administration and Support', 'Provides office support to either an individual or team and is vital for the smooth-running of a business'),
('Business Development', 'Identify long-term methods to increase value through the development of relationships, markets and customers'),
('Corporate Social Responsibilities', "Acts as a company's 'conscience', championing and developing the ethical, environmentally-friendly, and community-minded side of a business"),
('Customer services', 'Involved in customer service, support, success, and experience'),
('Design and Technical Service', 'Involves developing creative, tech-based solutions to existing problems'),
('Information Technology', 'Involves the implementation, support, maintenance, repair or protection of data or computer systems'),
('Engineering', 'Jobs that use science and mathematics to solve a variety of problems'),
('Finance', "Kobs where a company's funds and profitability are the primary focus"),
('Legal', 'Practicing the law'),
('Manufacturing and production', 'Involves the creation of new products either from raw materials or by assembling different components'),
('Marketing and advertising', "Responsible for planning, creating, and executing marketing campaigns to expand their company's reach and potential customer"),
('Sales and Communication', 'Customer service experience and sales skills');

DROP TABLE IF EXISTS `role_listing`;
CREATE TABLE IF NOT EXISTS `role_listing` (
    listing_id integer NOT NULL AUTO_INCREMENT,
    role_name varchar(20) NOT NULL,
    department varchar(100) NOT NULL,
    category varchar(120) NOT NULL,
    deadline date NOT NULL,
    CONSTRAINT role_listing_pkey PRIMARY KEY (listing_id),
    constraint role_listing_fk1 foreign key (category) references category(category) ON DELETE CASCADE,
    CONSTRAINT role_listing_fk2 FOREIGN KEY (role_name) REFERENCES role(role_name) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO role_listing (listing_id, role_name, department, category, deadline) VALUES
(1, 'HR Manager', 'HR', 'Administration and Support', '2023-09-30'),
(2, 'Software Engineer', 'IT', 'Engineering', '2023-10-15'),
(3, 'Financial Analyst', 'Finance', 'Finance', '2023-08-15'),
(4, 'Network Administrator', 'IT', 'Information Technology', '2024-08-15');

DROP TABLE IF EXISTS `job_application`;
CREATE TABLE IF NOT EXISTS `job_application` (
    application_id integer NOT NULL AUTO_INCREMENT,
    staff_id integer NOT NULL,
    listing_id integer NOT NULL,
    application_date date NOT NULL,
    CONSTRAINT job_application_pkey PRIMARY KEY (application_id),
    constraint job_application_fk1 foreign key (staff_id) references staff(staff_id) ON DELETE CASCADE,
    constraint job_application_fk2 foreign key (listing_id) references role_listing(listing_id) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO job_application (application_id, staff_id, listing_id, application_date) VALUES
(1, 1, 1, '2023-09-20'),
(2, 2, 2, '2023-10-10');


DROP TABLE IF EXISTS `login_details`;
CREATE TABLE IF NOT EXISTS `login_details` (
    staff_id integer NOT NULL,
    staff_password varchar(255) NOT NULL,
    CONSTRAINT login_details_pkey PRIMARY KEY (staff_id),
    constraint login_details_fk1 foreign key (staff_id) references staff(staff_id) ON DELETE CASCADE
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO login_details (staff_id, staff_password) VALUES
(1, 'hashed_password_for_john'),
(2, 'hashed_password_for_jane'),
(3, 'hashed_password_for_bob');


DROP TABLE IF EXISTS `extra`;
CREATE TABLE IF NOT EXISTS `extra` (
    `extra_id` int(11) NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (`extra_id`)
)ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `extra` (`extra_id`)VALUES 
('1');

