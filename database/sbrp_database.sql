SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `sbrp`
--
CREATE DATABASE IF NOT EXISTS `sbrp` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `sbrp`;

-- Drop existing tables (optional but good for clean slate)
DROP TABLE IF EXISTS `job_application`;
DROP TABLE IF EXISTS `staff_skill`;
DROP TABLE IF EXISTS `role_skill`;
DROP TABLE IF EXISTS `login_details`;
DROP TABLE IF EXISTS `role_listing`;
DROP TABLE IF EXISTS `skills`;
DROP TABLE IF EXISTS `role`;
DROP TABLE IF EXISTS `staff`;   
DROP TABLE IF EXISTS `category`;
DROP TABLE IF EXISTS `access_rights`;


-- Table structure for table `access_rights`
CREATE TABLE IF NOT EXISTS `access_rights`(
    access_id integer NOT NULL,
    access_control_name varchar(20) NOT NULL,
    CONSTRAINT access_rights_pkey PRIMARY KEY (access_id)
)  ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `access_rights`
INSERT INTO access_rights (access_id, access_control_name) VALUES
(1,'Admin'),
(2,'User'),
(3,'Manager'),
(4,'HR');


-- Table structure for table `staff`
CREATE TABLE IF NOT EXISTS `staff` (
    staff_id integer NOT NULL,
    staff_fname varchar(50) NOT NULL,
    staff_lname varchar(50) NOT NULL,
    dept varchar(50) NOT NULL,
    country varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    role integer NOT NULL,
    CONSTRAINT staff_pkey PRIMARY KEY (staff_id),
    constraint staff_fk1 foreign key (role) references access_rights(access_id) ON DELETE CASCADE
)  ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `staff` (10 entries)
INSERT INTO staff (staff_id, staff_fname, staff_lname, dept, country, email, role) VALUES
(130001,'John','Sim','Chairman','Singapore','john.sim@allinone.com.sg',1),
(130002,'Jack','Sim','CEO','Singapore','jack.sim@allinone.com.sg',1),
(140001,'Derek','Tan','Sales','Singapore','Derek.Tan@allinone.com.sg',3),
(140002,'Susan','Goh','Sales','Singapore','Susan.Goh@allinone.com.sg',2),
(140003,'Janice','Chan','Sales','Singapore','Janice.Chan@allinone.com.sg',2),
(140004,'Mary','Teo','Sales','Singapore','Mary.Teo@allinone.com.sg',2),
(140008,'Jaclyn','Lee','Sales','Singapore','Jaclyn.Lee@allinone.com.sg',3),
(150008,'Eric','Loh','Solutioning','Singapore','Eric.Loh@allinone.com.sg',3), -- Solutioning Manager
(160008,'Sally','Loh','HR','Singapore','Sally.Loh@allinone.com.sg',4), -- HR Staff
(170166,'David','Yap','Finance','Singapore','David.Yap@allinone.com.sg',3); -- Finance Manager


-- Table structure for table `role`
CREATE TABLE IF NOT EXISTS `role` (
    role_name varchar(50) NOT NULL,
    role_desc longtext NOT NULL,
    CONSTRAINT role_pkey PRIMARY KEY (role_name)
)  ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `role` (First 5)
INSERT INTO role (role_name, role_desc) VALUES
('Account Manager','The Account Manager acts as a key point of contact between All-In-One and its clients.<br>Responsibilities include managing client portfolios, ensuring client satisfaction, identifying new business opportunities within existing accounts, and achieving sales targets.<br>Requires strong communication, negotiation, and relationship-building skills.'),
('Admin Executive','The Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries.<br>Main duties include managing office stock, preparing regular reports (e.g., expenses and office budgets), and organizing company records.<br>May also involve handling basic HR tasks and coordinating office activities.'),
('Call Centre','The Call Centre Executive is responsible for providing assistance and support to customers over the phone, email, or chat.<br>Duties include handling inquiries, resolving complaints, processing orders, and providing information about products and services.<br>Requires excellent communication skills, patience, and problem-solving abilities.'),
('Consultancy Director','The Director defines and articulates the organisation\'s consultancy strategy and framework to meet the needs of the clients.<br>Oversees a team of consultants, manages high-level client relationships, drives business development, and ensures the quality delivery of consulting engagements.<br>Requires extensive industry experience, leadership skills, and strategic thinking.'),
('Consultant','The Consultant is responsible for providing technical expertise and guidance during the sales process and project implementation.<br>Works closely with clients to understand their needs, designs solutions, conducts product demonstrations, and supports the technical aspects of proposals.<br>Requires strong technical knowledge in relevant areas (e.g., IT infrastructure, software development) and good presentation skills.'),
('Finance Analyst', 'The Finance Analyst is responsible for financial planning, analysis, and reporting to support organizational decision-making.<br>Duties include analyzing financial data, creating financial models, forecasting future performance, preparing reports for management, and ensuring compliance with financial regulations.<br>Requires strong analytical skills, proficiency in financial software, and attention to detail.'), 
('Solutioning Architect', 'The Solutioning Architect designs end-to-end technical solutions based on client requirements.<br>Responsibilities include translating business needs into technical specifications, evaluating technology options, creating architecture blueprints, and ensuring the proposed solution is feasible, scalable, and secure.<br>Requires deep technical expertise across multiple domains and strong problem-solving skills.');


-- Table structure for table `skills`
CREATE TABLE IF NOT EXISTS `skills` (
    skill_name varchar(50) NOT NULL,
    skill_desc varchar(500) NOT NULL,
    CONSTRAINT skills_pkey PRIMARY KEY (skill_name)
)  ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `skills` (First 5)
INSERT INTO skills (skill_name, skill_desc) VALUES
('Account Management','Manage, maintain and grow the sales and relationships...'),
('Accounting and Tax Systems','Implement accounting or tax software systems...'),
('Accounting Standards','Apply financial reporting framework...'),
('Applications Development','Develop applications based on the design specifications...'),
('Applications Integration','Integrate data or functions from one application program...'),
('Customer Relationship Management', 'Manage customer relationships using CRM systems...'),
('Financial Planning', 'Plan and forecast financial performance...'),
('Solutions Architecture', 'Design and document technical solutions to meet business needs...');


-- Table structure for table `role_skill`
CREATE TABLE IF NOT EXISTS `role_skill` (
    role_name varchar(50) NOT NULL,
    skill_name varchar(50) NOT NULL,
    CONSTRAINT role_skill_pkey PRIMARY KEY (role_name, skill_name),
    CONSTRAINT role_skill_fk1 FOREIGN KEY (role_name) REFERENCES role(role_name) ON DELETE CASCADE,
    CONSTRAINT role_skill_fk2 FOREIGN KEY (skill_name) REFERENCES skills(skill_name) ON DELETE CASCADE
)  ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `role_skill` (limited)
INSERT INTO role_skill (role_name, skill_name) VALUES
('Account Manager','Account Management'),
('Consultancy Director','Account Management'),
('Consultant','Account Management'),
('Consultant','Applications Integration'),
('Consultant', 'Applications Development'),
('Call Centre', 'Customer Relationship Management'),
('Finance Analyst', 'Accounting Standards'),
('Finance Analyst', 'Financial Planning'),
('Solutioning Architect', 'Applications Development'),
('Solutioning Architect', 'Solutions Architecture');


-- Table structure for table `staff_skill`
CREATE TABLE IF NOT EXISTS `staff_skill` (
    staff_id integer NOT NULL,
    skill_name varchar(50) NOT NULL,
    CONSTRAINT staff_skill_pkey PRIMARY KEY (staff_id, skill_name),
    CONSTRAINT staff_skill_fk1 FOREIGN KEY (skill_name) REFERENCES skills(skill_name) ON DELETE CASCADE,
    CONSTRAINT staff_skill_fk2 FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE
)  ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `staff_skill` (limited)
INSERT INTO staff_skill (staff_id, skill_name) VALUES
(140001,'Account Management'), -- Derek
(140002,'Accounting Standards'), -- Susan
(140003,'Account Management'), -- Janice
(140004,'Account Management'), -- Mary
(170166,'Accounting and Tax Systems'), -- David
(140002, 'Customer Relationship Management'), -- Added Skill for Susan
(140003, 'Applications Development'), -- Added Skill for Janice
(170166, 'Financial Planning'), -- Added Skill for David Yap
(160008, 'Account Management'), -- Added Skill for Sally Loh (HR)
(160008, 'Applications Development'), -- Added Skill for Sally Loh (HR)
(160008, 'Applications Integration'); -- Added Skill for Sally Loh (HR)


-- Table structure for table `category`
CREATE TABLE IF NOT EXISTS `category` (
    category varchar(50) NOT NULL,
    category_desc varchar(100) NOT NULL,
    CONSTRAINT category_pkey PRIMARY KEY (category)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `category`
INSERT INTO `category` (`category`, `category_desc`) VALUES
('Core', 'Core skills Management'),
('Finance', 'Finance skills Management'),
('Information Technology', 'IT skills Management'),
('Sales', 'Sales skills Management');


-- Table structure for table `role_listing`
CREATE TABLE IF NOT EXISTS `role_listing` (
    listing_id integer NOT NULL AUTO_INCREMENT,
    role_name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    department varchar(50) NOT NULL,
    deadline date NOT NULL,
    CONSTRAINT role_listing_pkey PRIMARY KEY (listing_id),
    CONSTRAINT role_listing_fk1 FOREIGN KEY (role_name) REFERENCES role(role_name) ON DELETE CASCADE,
    CONSTRAINT role_listing_fk2 FOREIGN KEY (category) REFERENCES category(category) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- Dumping data for table `role_listing` (3 listings, Updated Deadlines)
INSERT INTO role_listing (role_name, category, department, deadline) VALUES
('Account Manager','Sales','Sales','2025-12-31'),
('Admin Executive','Core','HR','2025-12-31'),
('Consultant','Information Technology','Consultancy','2025-12-31'),
('Call Centre','Sales','Sales','2025-11-30'),
('Finance Analyst','Finance','Finance','2026-01-15'),
('Consultant','Information Technology','Solutioning','2025-10-31'),
('Solutioning Architect','Information Technology','Solutioning','2026-02-28');


-- Table structure for table `job_application`
CREATE TABLE IF NOT EXISTS `job_application` (
    application_id integer NOT NULL AUTO_INCREMENT,
    staff_id integer NOT NULL,
    listing_id integer NOT NULL,
    application_date date NOT NULL,
    cover_letter longtext NULL,
    application_status varchar(20) NOT NULL DEFAULT 'Pending',
    CONSTRAINT job_application_pkey PRIMARY KEY (application_id),
    CONSTRAINT job_application_fk1 FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    CONSTRAINT job_application_fk2 FOREIGN KEY (listing_id) REFERENCES role_listing(listing_id) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- Dumping data for table `job_application` (Limited)
-- Assuming listing_id 1 = Account Manager, listing_id 3 = Consultant
INSERT INTO `job_application` (`staff_id`, `listing_id`, `application_date`, `cover_letter`, `application_status`) VALUES
(140002, 1, '2023-10-15', 'I am interested in the Account Manager role.', 'Pending'), -- Susan applying for Acct Mgr
(140003, 3, '2023-10-16', 'Applying for Consultant role.', 'Pending'); -- Janice applying for Consultant


-- Table structure for table `login_details`
CREATE TABLE IF NOT EXISTS `login_details` (
    login_id varchar(50) NOT NULL,
    staff_id integer NOT NULL,
    staff_password varchar(255) NOT NULL,
    CONSTRAINT login_details_pkey PRIMARY KEY (login_id),
    CONSTRAINT login_details_fk1 FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `login_details` (Matching 10 staff, corrected password)
INSERT INTO `login_details` (`login_id`, `staff_id`, `staff_password`) VALUES
('john.sim', 130001, 'password'),
('jack.sim', 130002, 'password'),
('derek.tan', 140001, 'password'),
('susan.goh', 140002, 'password'),
('janice.chan', 140003, 'password'),
('mary.teo', 140004, 'password'),
('jaclyn.lee', 140008, 'password'),
('eric.loh', 150008, 'password'),
('sally.loh', 160008, 'password'),
('david.yap', 170166, 'password');

COMMIT;
