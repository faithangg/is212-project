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
DROP TABLE IF EXISTS `job_application`;
DROP TABLE IF EXISTS `role_listing`;
DROP TABLE IF EXISTS `login_details`;
DROP TABLE IF EXISTS `role_listing`;
DROP TABLE IF EXISTS `role`;
DROP TABLE IF EXISTS `category`;
DROP TABLE IF EXISTS `staff`;   

DROP TABLE IF EXISTS `access_rights`;
CREATE TABLE IF NOT EXISTS `access_rights`(
    access_id integer NOT NULL,
    access_control_name varchar(20) NOT NULL,
    CONSTRAINT access_rights_pkey PRIMARY KEY (access_id)
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO access_rights (access_id, access_control_name) VALUES
(1,'Admin'),
(2,'User'),
(3,'Manager'),
(4,'HR');


DROP TABLE IF EXISTS `staff`;
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
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO staff (staff_id, staff_fname, staff_lname, dept, country, email, role) VALUES
  (140001, 'Derek', 'Tan', 'Sales', 'Singapore', 'Derek.Tan@allinone.com.sg', 3),
  (140002, 'Susan', 'Goh', 'Sales', 'Singapore', 'Susan.Goh@allinone.com.sg', 4),
  (140004, 'Mary', 'Teo', 'Sales', 'Singapore', 'Mary.Teo@allinone.com.sg', 2),
  (140008, 'Jaclyn', 'Lee', 'Sales', 'Singapore', 'Jaclyn.Lee@allinone.com.sg', 3);

DROP TABLE IF EXISTS `role`;
CREATE TABLE IF NOT EXISTS `role` (
    role_name varchar(50) NOT NULL,
    role_desc longtext NOT NULL,
    CONSTRAINT role_pkey PRIMARY KEY (role_name)
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


INSERT INTO role (role_name, role_desc) VALUES
('Account Manager',"The Account Manager acts as a key point of contact between an organisation and its clients. He/She possesses thorough product knowledge and oversees product and/or service sales. He works with customers to identify their wants and prepares reports by collecting, analysing, and summarising sales information. He contacts existing customers to discuss and give recommendations on how specific products or services can meet their needs. He maintains customer relationships to strategically place new products and drive sales for long-term growth. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for meetings. He is familiar with client relationship management and sales tools. He is knowledgeable of the organisation's products and services, as well as trends, developments and challenges of the industry domain. The Sales Account Manager is a resourceful, people-focused and persistent individual, who takes rejection as a personal challenge to succeed when given opportunity. He appreciates the value of long lasting relationships and prioritises efforts to build trust with existing and potential customers. He exhibits good listening skills and is able to establish rapport with customers and team members alike easily.")
,('Admin Executive',"Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as a Office Administrator or similar administrative role, we'd like to meet you.")
,('Call Centre','Call Centre Executive is responsible for providing assistance to customers by addressing their queries and requests. He/She advises customers on appropriate products and services based on their needs. He is responsible for the preparation of customer documentation. In the case of complex customer requests, he escalates them to senior officers. He is able to abide by safety and/or security standards in the workplace.
<br> The Call Centre Executive  pays strong attention to details to verify and process documentation. He also shows initiative and quick decision-making skills to provide excellent personalised customer services and support. He is comfortable with various stakeholder interactions whilst working in shifts and possesses adequate computer literacy to process customer documentation.')
,('Consultancy Director',"The  Director defines and articulates the organisation's strategy for securing technical wins with prospective clients. He/She focuses on developing key growth  strategies, tactics and action plans required to achieve revenue and/or sales targets. He advises the team on developing prototypes to ensure feasibility of solutions, and oversees the delivery of in-depth presentations and product demonstrations to clients. He solves complex problems and evaluates clients needs with different perspectives. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for technical sales pitches and meetings. He is familiar with client relationship management and sales tools. He possesses deep product and technical knowledge, and is knowledgeable of the trends, developments and challenges of the industry domain. The  Director is target-driven and client centric, and has the ability to foster collaboration between stakeholders. He has a deep understanding of key business industries and knowledge of products and services in the market. He is strongly committed to developing talent and inspires his team members to pursue a common vision.")
,('Consultant',"The Consultant is responsible for providing Sales technical expertise to the sales team and clients during the sales process. He/She delivers presentations and technical demonstrations of the organisation's products to prospective clients. He translates the client's business requirements into technical specifications and requirements, and provides technical inputs for proposals, tenders, bids and any relevant documents. He uses prescribed guidelines or policies to analyse and solve problems. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for technical sales pitches and meetings. He is familiar with client relationship management and sales tools. He possesses deep product and technical knowledge, and is knowledgeable of the trends, developments and challenges of the industry domain. The Sakes Consultant displays effective listening skills and is inquisitive in nature. He possesses deep technical and domain knowledge, pays attention to detail, and has strong analytical and problem-solving capabilities. He has a service-oriented personality and is a team player who works towards developing solutions collaboratively.")
,('Developer',"The Developer leads important projects and possesses capability to make breakthroughs in design, development, testing, debugging and implementing software applications or specialised utility programs in support of end users' needs on platforms. He/She plans and coordinates regular updates and recommends improvements to existing applications. He identifies and resolves issues which have organisation wide and long-term impact. He identifies security risks, creates requirements to capture security issues, and performs initial threat modelling to ensure coding standards meets security requirements. He develops and maintains the software configuration management plan and oversees the building, verification and implementation of software releases. He provides guidance and technical support to the quality testing teams. He works in a team setting and is proficient in programming languages required by the organisation. He is familiar with software development tools and standards, as well as the relevant software platforms on which the solution is deployed on. The Developer is imaginative and creative in exploring a range of application designs and solutions. He is able to engage and support others in the team, readily put forth his ideas in a clear and compelling manner.")
,('Engineering Director',"The Engineering Director is responsible for spearheading the strategic planning, design and implementation of complex engineering solutions to meet customers requirements. He/She drives direction and strategy for the development and execution of engineering projects, and ensures alignment to the organisational strategy, vision and mission. He formulates strategies and frameworks to drive workplace health, safety, risk and environmental management in accordance with local and international regulations. He develops the organisations technology roadmap and drives continuous improvement strategies. In addition, he leverages his deep technical expertise and industry experience to develop technical capabilities and domain expertise for the organisation. He is a professional engineer, specialising in mechanical, electrical, control and instrumentation, civil, structural or geotechnical engineering disciplines.
<br> He is the organisations technical expert who advises senior management and business partners on complex engineering matters. He maintains and builds strong links with the external engineering community and establishes best practises in the implementation of engineering standards and design. He is a strategic and creative thinker, demonstrates exceptional leadership and problem-solving skills, and establishes strategic partnerships.")
,('Finance  Executive',"The Finance Executive supports the finance department in carrying out the responsibilities of the accounting department. He/She is involved in work that is specific to accounts receivable, accounts payable, tax filing, data compilation, billing, payroll or other accounting tasks. In some instances, he may work specifically with accruals, fixed assets accounting or the monthly and yearly finalisation of accounts for audit purposes. The Accounts Executive/Accounts Assistant may also assist with the preparation of trial balance, basic financial statements and simple consolidated financial statements. He may be called on to participate in ad-hoc finance-related projects and systems testing when necessary.")
,('Finance Director',"The Finance Director is the business partner for all the business units in an organisation. He/She serves as the organisations go-to person for all matters related to accounting. He provides technical accounting advice to various stakeholders to maximise organisation's value and minimise risks in accordance with external and internal accounting guidance. The Business Controller/Finance Director demonstrates excellent people skills to facilitate the on-going business relationships and find new business opportunities. He also play a critical role in financial planning and analysis supporting key management decisions which includes involvement in providing operational risk management support to the business and ensuring proper business performance management through profitability and operational analysis. In addition, he is involved in recruitment, performance management, appraisal and identifying training and development needs for the business units in an organisation.")
,('Finance Manager',"The Finance Manager is the lead finance business partner for the organisation and has responsibilities covering all aspects of financial management, performance management, financial accounting, budgeting, corporate reporting etc. He/she has sound technical as well as management skills and be able to lead a team consisting of finance professionals with varied, in-depth or niche technical knowledge and abilities; consolidating their work and ensuring its quality and accuracy, especially for reporting purposes. The Finance Manager is expected to provide sound financial advice and counsel on working capital, financing or the financial position of the organisation by synthesising internal and external data and studying the economic environment. He often has a key role in implementing best practices in order to identify and manage all financial and business risks and to meet the organisation's desired business and fiscal goals. He is expected to have a firm grasp of economic and business trends and to implement work improvement projects that are geared towards quality, compliance and efficiency in finance.")
,('HR Director',"The HR Director is responsible for establishing the overall talent management strategies and frameworks to identify, prepare and position the right talent to drive organisational success. He/She formulates career development frameworks and programmes to provide fulfilling career opportunities to employees in the organisation. He liaises with senior business stakeholders to formulate robust succession plans for business-critical roles in the organisation, ensuring future viability and alignment with business plans and direction. He is responsible for establishing retirement and exit policies and guidelines, and evaluating the business impact of redundancy, retirement and exit decisions. He also guides and advises senior business leaders in the management and communication of sensitive talent decisions. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent management plans.
<br> The HR Director is a forward-thinking and influential leader who is able to integrate knowledge across diverse domains to make robust decisions and address multi-faceted issues effectively. He has the desire to motivate employees and develop talent capabilities both within the team and across the organisation, and demonstrates sensitivity and diplomacy when interacting with stakeholders at various levels.")
,('HR Executive',"HR Team executes planned talent outreach and engagement activities to source for potential candidates and maintains an optimal experience for employees. He/She conducts the initial screening of potential candidates, administers assessments and prepares employment contracts as per guidelines. He tracks the conversion success rate for each sourcing channel and provides administrative and logistical support during onboarding. He administers employee engagement surveys and collates responses and feedback while ensuring confidentiality of information provided.
<br> HR Team Executive enjoys working in a team environment and interacts proactively with various stakeholders. He has a service-oriented mindset and can adapt to various forms of technology within his work space to enhance his work. ")
,('IT Analyst',"IT Analyst performs routine infrastructure operations and maintenance activities. He/She assists with monitoring infrastructure performance. He checks for problems in existing systems and modifies work processes by following defined procedures, processes and quality standards. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays. He works in a team setting and is proficient in infrastructure systems and network-related tools and techniques required by the organisation. He is also familiar with the relevant software platforms on which the database is deployed. The Associate Infrastructure Support Engineer is able to solve issues quickly and effectively as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.")
,('IT Director',"The IT Director drives the vision and strategy for the IT Operations and Support functions. He/She sets the direction for systems and database administration, day-to-day IT support and operations, data centre operations and system and quality assurance through the delivery of services as per business requirements; controls costs and manages vendors. He is responsible for formulating strategies for service level agreements. He ensures compliance with organisation's quality standards, international standards and government regulations. He is a leader with the energy and commitment to drive large teams toward achieving service level excellence. He is familiar with enterprise architecture frameworks, database administration and systems, and application monitoring tools. The Head of Operations and Support has a broad sense of perspective with the ability to influence key internal and external stakeholders. He is strategic in his approach to managing resources and developing capabilities within the team. He is effective in setting direction aligned to the strategic positioning of the business and the IT functions overall. He is able to impress upon the team the need to continuously improve service levels and increase efficiencies.")
,('Junior Engineer',"The Junior Engineerapplies engineering principles and techniques to optimise the equipment and systems within the manufacturing facility. He/She provides technical guidance and direction for the installation of equipment and systems. He develops plans for the maintenance of equipment and systems, and recommends engineering solutions to troubleshoot faults. The Junior Engineerinnovates equipment and systems, and contributes to manufacturing equipment and systems improvement projects by conducting feasibility assessments and tests on new technologies. He is also expected to manage energy resources and utilities by developing solutions to optimise machine availability and energy efficiency. The Junior Engineermust ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview. He develops guidelines and conducts equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. 
<br> The Junior Engineer should possess an enquiring and analytical mind and have a knack for investigating issues, analysing multifaceted engineering problems and developing solutions. He must also be a strong team player who can guide and mentor others, and communicate technical advices and solutions to colleagues beyond the team.")
,('L&D Executuve', "The L&D Executive assists in procuring training programmes and documenting learning needs in the 
organisation, maintaining organisations' learning systems and provides administrative support in conducting learning programmes. He/She manages resources and logistics for delivering learning programmes and collects data from learning evaluation surveys to measure learning programmes effectiveness. He supports the conduct of assessments to identify high-potential talent in the organisation, and documents assessment records and succession plans for critical roles identified. He also responds to employee queries that are related to assessments and learning programmes. He is responsible for maintaining exit and retirement records.
<br> The L&D Executive enjoys working in a team environment and interacts proactively with various stakeholders. He is eager to explore and analyse problems, and is able to communicate information in a clear and concise manner to meet others' needs at the workplace.")
,('Ops Planning Exec',"The Operation Planning Executive upports plant operations by coordinating day-to-day production activities, as well as maintenance and turnaround schedules and activities, for production shift teams, so as to meet production plans and schedules.")
,('Sales Director',"The Sales Director determines sales targets, markets and product offering. He/She focuses on revenue target setting accountability, sales strategy and career development of others, liaising with professional staff and other managers on the medium- to long-term sales planning. He develops, communicates and implements the operational strategy, regularly leads important sales initiatives and has ultimate accountability for the sales function. He oversees the preparation and presentation of technical proposals and ensures that the complete plans are feasible within cost, time, and environmental constraints. He drives product differentiation and optimises the use of resources, evaluates partnership effectiveness, and advises on corrective action. He solves complex problems and adopts new perspectives to drive sales. He works in a fast-paced and dynamic environment, and travels to clients' premises for sales pitches and negotiations. He is familiar with client relationship management and sales tools, as well as sales operations and business practices. He knowledgeable of the trends, developments and challenges of the industry domain. The Sales Director is creative and self-motivated, and is dedicated to growing the business. He contributes his expertise to product development and brainstorming of marketing campaigns, as needed. He is a competent decision maker who exhibits flexibility amidst a rapidly changing environment. He strives to train talent and build successful teams.")
,('Sales Manager',"The Sales Manager is responsible for managing the organisation's sales growth. By analysing client segmentation and competitor landscape, he/she develops sales strategies. He supports lead generation, and conducts business and contract negotiations to increase client acquisition and boost retention. 
<br> Innovative and resourceful, he demonstrates initiative in identifying new opportunities both locally and regionally and converting them into actual sales. He builds good rapport with new and existing clients by pro-actively anticipating clients' needs and identifying business solutions to meet those needs. He networks extensively outside of the office to stay in close contact with the key industry stakeholders.")
,('Senior Engineer','The Senior Engineer applies advanced engineering principles and techniques to troubleshoot complex engineering problems encountered within the manufacturing facility and provides expert technical advice to guide the installation and maintenance of equipment and systems. He/She is expected to lead the technical cross-collaboration with the Process Development/Manufacturing Science and Technology (PD/MSAT) department in order to identify appropriate biopharmaceuticals manufacturing equipment and optimise their functionalities. The Senior Engineer leads manufacturing equipment and systems innovation projects by guiding feasibility assessments and tests on new technologies. He is expected to review and approve solutions and initiatives to optimise machine availability while managing energy and utility use. He sets parameters for equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. The Principal/Engineer must ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview.
<br> The Engineering and Maintenance Principal/Engineer carries the responsibility of the in-house technical expert. He should possess a deep passion for analysing and resolving multifaceted engineering problems and be able to apply advanced critical and analytical thinking skills to deal with immediate situations. He should have a developmental and amiable approach in his interactions working as part of a team while guiding and mentoring others. He must also be able to communicate engineering concepts in a manner that will be understood by others within and beyond the team.')
,('Solutioning Director',"The Solutioning Director defines and articulates the organisation's strategy for securing technical wins with prospective clients. He/She focuses on developing key growth pre-sales strategies, tactics and action plans required to achieve revenue and/or sales targets. He advises the team on developing prototypes to ensure feasibility of solutions, and oversees the delivery of in-depth presentations and product demonstrations to clients. He solves complex problems and evaluates clients needs with different perspectives. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for technical sales pitches and meetings. He is familiar with client relationship management and sales tools. He possesses deep product and technical knowledge, and is knowledgeable of the trends, developments and challenges of the industry domain. The Pre-Sales Director is target-driven and client centric, and has the ability to foster collaboration between stakeholders. He has a deep understanding of key business industries and knowledge of products and services in the market. He is strongly committed to developing talent and inspires his team members to pursue a common vision.")
,('Support Engineer',"The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.");

DROP TABLE IF EXISTS `skills`;
CREATE TABLE IF NOT EXISTS `skills` (
    skill_name varchar(50) NOT NULL,
    skill_desc varchar(500) NOT NULL,
    CONSTRAINT skills_pkey PRIMARY KEY (skill_name)
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO skills (skill_name, skill_desc) VALUES
('Account Management','Manage, maintain and grow the sales and relationships with a specific customer or set of accounts. This includes in-depth customer engagement, relationship-building and provision of quality solutions and service to address customers'' needs efficiently and generate revenue.')
,('Accounting and Tax Systems','Implement accounting or tax software systems in the organisation')
,('Accounting Standards','Apply financial reporting framework prescribed by the relevant governing body to ensure all transactions meet regulatory requirements')
,('Applications Development','Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components.')
,('Applications Integration','Integrate data or functions from one application program with that of another application program - involves development of an integration plan, programming and the identification and utilisation of appropriate middleware to optimise the connectivity and performance of disparate applications across target environments')
,('Applications Support and Enhancement','Provide ongoing technical support and improvements to users of applications. This includes technical guidance and assistance related to the installation and maintenance of applications, fixing and resolution of application problems or disruptions, and response to change requests that will enhance the operations and usage of an application')
,('Audit Compliance','Ensure compliance with corporate policies and guidelines')
,('Audit Frameworks','Develop quality assurance frameworks to meet regulatory requirements')
,('Automated Equipment and Control Configuration','Configure automated equipment and control systems to support biopharmaceuticals and manufacturing processes')
,('Budgeting','Prepare organisational budgets to support short- and long-term business plans through forecasting, allocation and financial policy setting.')
,('Business Acumen','Assess the impact of changes in the business organisation, environment, and industry')
,('Business Development','Develop and implement plans to enhance organisation''s business performance and growth')
,('Business Environment Analysis','Analyse data pertaining to the business landscape and environment, including competitor-analysis, trends and developments in laws and regulations and the impact on the business')
,('Business Needs Analysis','Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business')
,('Business Negotiation','Conduct negotiations to establish win-win outcomes for the organisation')
,('Business Presentation Delivery','Perform required tasks to prepare and present information in various business settings involving preparation, understanding of audience, delivery and tailoring of messages to be conveyed')
,('Business Requirements Mapping','Map business requirements to existing processes to identify gaps or opportunities for possible solutions and evaluate impact of solutions against requirements to propose adjustments as needed')
,('Business Risk Management','Forecast and assess existing and potential IT risks which impact the operation and/or profitability to the business as well as the development and roll out of company-wide strategies and processes to mitigate risk, minimise their impact or effectively manage such business risks')
,('Call Centre Management','Implement and manage call centre operations to address queries and needs of customers')
,('Collaboration','Manage relationships and work collaboratively and effectively with others to achieve goals')
,('Communication','Convey and exchange thoughts, ideas and information effectively through various mediums and approaches')
,('Configuration Tracking','Track systematically and manage changes and revisions in software projects to ensure that all changes are accounted for and to protect assets against unauthorized change, diversion and inappropriate use')
,('Customer Acquisition Management','Develop customer acquisition strategies as well as foster customer relationships to attract new customers')
,('Customer Relationship Management','Initiate and drive activities to enhance customer relationships and brand loyalty for the organisation')
,('Data Analytics','Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence')
,('Database Administration','Perform Installation, coordination and upgrading of databases and database servers, performance monitoring and troubleshooting. This includes monitoring user access to database and optimisation of database performance, planning for backup and recovery, archived data maintenance and reporting')
,('Developing People','Empower others to learn and develop their capabilities to enhance their performance and achieve personal or professional goals')
,('Digital Fluency','Leverage digital technology tools, systems, and software across work processes and activities to solve problems, drive efficiency and facilitate information sharing')
,('Employee Communication Management','Formulate overall employee communication strategies and facilitate conversations to ensure effective and timely dissemination of pertinent information to employees')
,('Employee Engagement Management','Drive employee engagement programmes to facilitate commitment from employees to organisational values, vision and objectives')
,('Finance Business Partnering','Generate finance-related insights to support the business in a strategic manner')
,('Financial Acumen','Exercise financial insight to establish budgets for human resource (HR) activities and monitor HR operations and outcomes against financial plans')
,('Financial Closing','Carry out month-end closing and reconciliation to ensure financial records are maintained properly')
,('Financial Management','Ensure healthy finance to aid business growth and operations')
,('Financial Planning','Evaluate and develop budget in line with organisation�s strategies and plans')
,('Financial Reporting','Prepare general-purpose financial statements and disclosure notes in accordance with applicable financial reporting framework')
,('Financial Statements Analysis','Analyse financial statements in accordance with the applicable frameworks')
,('Financial Transactions','Prepare business documentation and cash balances')
,('Human Resource Advisory','Deliver human resource (HR) advisory and consultancy services to internal and external clients to meet their requirements')
,('Human Resource Practices Implementation','Implement of human resource (HR) practices by integrating local and international requirements, guidelines and best practices')
,('Human Resource Strategy Formulation','Establish human resource (HR) strategies and priorities that are aligned with current and future business needs')
,('Human Resource Systems Management','Establish and manage effective and efficient human resource (HR) management systems')
,('Infrastructure Deployment','Set up, deploy and decommission infrastructure components and associated equipment in accordance to a set plan and established safety and/or quality procedures. This includes the assessment and preparation of appropriate site locations, infrastructure, the development of an installation plan, layout at the site, the testing of on-site systems, infrastructure components, equipment and the correction of issues and/or malfunctions')
,('Infrastructure Support','Provide services to end users by systematically identifying, classifying and troubleshooting technical issues and incidents that disrupt and impact their day-to-day business activities, within a specified timeframe. This also includes implementing an end-to-end problem management process to analyse underlying problems, advising on infrastructure related upgrades and improvements and developing user guides and training materials')
,('Learning and Development Programme Management','Establish and implement learning and development programmes and channels to facilitate employees'' growth and capability building')
,('Learning Needs Analysis','Identify the learning needs of the learners'' workplace, department or division in accordance to the Learning Needs Analysis Framework')
,('Network Administration and Maintenance','Monitor network in order to provide for optimum levels of network performance and minimisation of downtime. This includes detection, isolation, recovery and limitation of the impact of failures on the network as well as provision of support to system users through ongoing maintenance information sharing and training')
,('Onboarding','Facilitate onboarding programmes to enable the integration and engagement of new hires into the organisation')
,('Organisational Design','Develop and facilitate the implementation of organisational design to ensure its effectiveness and alignment with stakeholders'' priorities')
,('People and Performance Management','Establish and implement performance management and remuneration strategies in the organisation to drive business results')
,('Pricing Strategy','Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions')
,('Problem Management','Manage the lifecycle of problems to prevent problems and incidents from occurring, eliminate recurring incidents and minimise impact of unavoidable incidents')
,('Problem Solving','Generate effective and efficient solutions to solve problems and capitalise on new opportunities')
,('Product Management','Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set')
,('Professional and Business Ethics','Foster strong ethical standards and resolve ethical conflicts in accordance with the relevant principles and processes')
,('Project Management','Execute projects by managing stakeholder engagement, resources, budgets and resolving problems')
,('Regulatory Compliance','Comply with policies, procedures, and external regulations')
,('Regulatory Risk Assessment','Analyse the impact of latest global regulatory developments and relevant laws on overall audit and/or engagement strategies')
,('Regulatory Strategy','Align regulatory activities with business strategies')
,('Sales Closure','Perform numerical calculations and execute selling strategies to complete sales of products and services to the satisfaction of customers')
,('Sales Strategy','Develop a sales strategy, plan and targets, considering market potential, industry trends and various internal and external business factors as well as the evaluation and further refinement of the sales strategy')
,('Security Administration','Administer, configure and update of security programmes and mechanisms, including the application of system patches to ensure that enterprise assets are adequately protected against threats. This also includes the authorisation, management and monitoring of access control permissions and/or rights to various IT facilities')
,('Sense Making','Leverage sources of qualitative and quantitative information and data to recognise patterns, spot opportunities, infer insights and inform decisions')
,('Service Level Management','Plan, monitor and manage service provisions for the achievement of agreed service level targets')
,('Skills Framework Adoption','Drive the adoption, integration and implementation of Skills Frameworks and their components in business and human resources activities throughout the organisation')
,('Software Configuration','Configure software products, analytics and modelling solutions, and apply and/or modify scripts and automation tools to integrate and deploy releases to various platforms and operating environments')
,('Software Design','Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with')
,('Software Testing','Assess and test the overall effectiveness and performance of an application, involving the setting up of suitable testing conditions, definition of test cases and/or technical criteria')
,('Solution Architecture','Design or refine a solution blueprint or structure to guide the development of IT solutions in hardware, software, processes or related components, to meet current and future business needs. The solution architecture developed may lead to broad or specific changes to IT services, operating models and processes, and should provide a framework to guide the development and modification of solutions')
,('Solutions Design Thinking','Solutions Design Thinking')
,('SOP Development and Implementation','Develop Standard Operating Procedures (SOPs) and implement procedures to ensure that process operational tasks for all modes of plant operation are performed correctly and consistently in accordance with regulatory and organisational objectives')
,('Stakeholder Management','Manage stakeholder expectations to ensure continuous levels of engagement by identifying and addressing needs, setting service standards and resolving issues in accordance with organisational procedures')
,('Strategy Planning','Develop organisational strategies and policies by analysing the impact of internal and external influencing factors and seeking consultation from relevant stakeholders.')
,('System Integration','Develop and implement a roadmap and specific integration solutions to facilitate integration of various ICT components and optimise inter-operability of systems and their interfaces. This includes the integration of various architectural components such as networks, servers, system platforms and their interfaces')
,('Talent Management','Drive talent management strategies and programmes to identify, develop, review and retain talent to meet the current and future organisational needs')
,('Tax Computation','Compute Goods and Services Tax, and tax liabilities')
,('Tax Implications','Assess tax implication of changes in tax laws')
,('Technology Application','Integrate technologies into operations of the organisation to optimise efficiency and effectiveness of processes')
,('Technology Integration','Integrate new and emerging technology products, services and developments to enhance human resource (HR) operations and service delivery')
,('Technology Road Mapping','Plan short-term and long-term goals with specific technology solutions to help meet those goals in order to make capital out of future market needs')
,('User Interface Design','Design user interfaces for machines and software, incorporating visual, technical and functional elements that facilitate ease of access, understanding and usage. This would involve adding, removing, modifying or enhancing elements to make the user''s interaction with the product as seamless as possible');

DROP TABLE IF EXISTS `role_skill`;
CREATE TABLE IF NOT EXISTS `role_skill` (
    role_name varchar(50) NOT NULL,
    skill_name varchar(50) NOT NULL,
    CONSTRAINT role_skill_pkey PRIMARY KEY (role_name, skill_name),
    CONSTRAINT role_skill_fk1 FOREIGN KEY (role_name) REFERENCES role(role_name) ON DELETE CASCADE,
    CONSTRAINT role_skill_fk2 FOREIGN KEY (skill_name) REFERENCES skills(skill_name) ON DELETE CASCADE
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO role_skill (role_name, skill_name) VALUES
('Account Manager','Account Management')
,('Consultancy Director','Account Management')
,('Consultant','Account Management')
,('Sales Director','Account Management')
,('Solutioning Director','Account Management')
,('Finance  Executive','Accounting and Tax Systems')
,('Finance Director','Accounting and Tax Systems')
,('Finance Manager','Accounting and Tax Systems')
,('Finance  Executive','Accounting Standards')
,('Finance Manager','Accounting Standards')
,('Developer','Applications Development')
,('Developer','Applications Integration')
,('Developer','Applications Support and Enhancement')
,('Finance  Executive','Audit Compliance')
,('Finance Director','Audit Compliance')
,('Finance Manager','Audit Compliance')
,('Finance Manager','Audit Frameworks')
,('Senior Engineer','Automated Equipment and Control Configuration')
,('Account Manager','Budgeting')
,('Consultancy Director','Budgeting')
,('Engineering Director','Budgeting')
,('Sales Director','Budgeting')
,('Sales Manager','Budgeting')
,('Solutioning Director','Budgeting')
,('Finance Manager','Business Acumen')
,('HR Director','Business Acumen')
,('IT Director','Business Acumen')
,('Account Manager','Business Development')
,('Consultancy Director','Business Development')
,('Consultant','Business Development')
,('Sales Director','Business Development')
,('Solutioning Director','Business Development')
,('Developer','Business Environment Analysis')
,('Account Manager','Business Needs Analysis')
,('Consultancy Director','Business Needs Analysis')
,('Consultant','Business Needs Analysis')
,('Developer','Business Needs Analysis')
,('IT Analyst','Business Needs Analysis')
,('Sales Director','Business Needs Analysis')
,('Solutioning Director','Business Needs Analysis')
,('Support Engineer','Business Needs Analysis')
,('Account Manager','Business Negotiation')
,('Sales Director','Business Negotiation')
,('Sales Manager','Business Negotiation')
,('Sales Manager','Business Presentation Delivery')
,('Developer','Business Requirements Mapping')
,('Developer','Business Risk Management')
,('Call Centre','Call Centre Management')
,('Account Manager','Collaboration')
,('Admin Executive','Collaboration')
,('Call Centre','Collaboration')
,('Consultant','Collaboration')
,('Developer','Collaboration')
,('Finance  Executive','Collaboration')
,('Finance Manager','Collaboration')
,('HR Executive','Collaboration')
,('IT Analyst','Collaboration')
,('Junior Engineer','Collaboration')
,('L&D Executuve','Collaboration')
,('Ops Planning Exec','Collaboration')
,('Sales Director','Collaboration')
,('Sales Manager','Collaboration')
,('Senior Engineer','Collaboration')
,('Support Engineer','Collaboration')
,('Account Manager','Communication')
,('Admin Executive','Communication')
,('Call Centre','Communication')
,('Consultancy Director','Communication')
,('Consultant','Communication')
,('Developer','Communication')
,('Engineering Director','Communication')
,('Finance  Executive','Communication')
,('Finance Director','Communication')
,('Finance Manager','Communication')
,('HR Director','Communication')
,('HR Executive','Communication')
,('IT Analyst','Communication')
,('IT Director','Communication')
,('Junior Engineer','Communication')
,('L&D Executuve','Communication')
,('Ops Planning Exec','Communication')
,('Sales Director','Communication')
,('Sales Manager','Communication')
,('Senior Engineer','Communication')
,('Solutioning Director','Communication')
,('Support Engineer','Communication')
,('Developer','Configuration Tracking')
,('Support Engineer','Configuration Tracking')
,('Sales Manager','Customer Acquisition Management')
,('Admin Executive','Customer Relationship Management')
,('Call Centre','Customer Relationship Management')
,('Sales Manager','Customer Relationship Management')
,('Account Manager','Data Analytics')
,('Consultancy Director','Data Analytics')
,('Consultant','Data Analytics')
,('Finance  Executive','Data Analytics')
,('Finance Director','Data Analytics')
,('Finance Manager','Data Analytics')
,('Sales Director','Data Analytics')
,('Solutioning Director','Data Analytics')
,('Developer','Database Administration')
,('HR Director','Developing People')
,('Call Centre','Digital Fluency')
,('HR Executive','Digital Fluency')
,('HR Director','Employee Communication Management')
,('HR Executive','Employee Communication Management')
,('L&D Executuve','Employee Communication Management')
,('HR Executive','Employee Engagement Management')
,('Finance Director','Finance Business Partnering')
,('Finance Manager','Finance Business Partnering')
,('HR Director','Financial Acumen')
,('IT Director','Financial Acumen')
,('Finance  Executive','Financial Closing')
,('Finance  Executive','Financial Management')
,('Finance Director','Financial Management')
,('Finance Manager','Financial Management')
,('Finance Director','Financial Planning')
,('Finance Manager','Financial Planning')
,('Finance  Executive','Financial Reporting')
,('Finance Director','Financial Reporting')
,('Finance Manager','Financial Reporting')
,('Finance Manager','Financial Statements Analysis')
,('Finance  Executive','Financial Transactions')
,('HR Director','Human Resource Advisory')
,('IT Director','Human Resource Advisory')
,('HR Director','Human Resource Practices Implementation')
,('HR Executive','Human Resource Practices Implementation')
,('L&D Executuve','Human Resource Practices Implementation')
,('HR Director','Human Resource Strategy Formulation')
,('IT Director','Human Resource Strategy Formulation')
,('HR Executive','Human Resource Systems Management')
,('IT Director','Human Resource Systems Management')
,('L&D Executuve','Human Resource Systems Management')
,('IT Analyst','Infrastructure Deployment')
,('IT Analyst','Infrastructure Support')
,('Support Engineer','Infrastructure Support')
,('L&D Executuve','Learning and Development Programme Management')
,('L&D Executuve','Learning Needs Analysis')
,('IT Analyst','Network Administration and Maintenance')
,('Support Engineer','Network Administration and Maintenance')
,('HR Executive','Onboarding')
,('HR Director','Organisational Design')
,('Consultancy Director','People and Performance Management')
,('Sales Director','People and Performance Management')
,('Solutioning Director','People and Performance Management')
,('Support Engineer','People and Performance Management')
,('Account Manager','Pricing Strategy')
,('Sales Director','Pricing Strategy')
,('Consultancy Director','Problem Management')
,('Consultant','Problem Management')
,('Developer','Problem Management')
,('Solutioning Director','Problem Management')
,('Support Engineer','Problem Management')
,('Account Manager','Problem Solving')
,('Admin Executive','Problem Solving')
,('Call Centre','Problem Solving')
,('Consultancy Director','Problem Solving')
,('Consultant','Problem Solving')
,('Developer','Problem Solving')
,('Engineering Director','Problem Solving')
,('Finance  Executive','Problem Solving')
,('IT Analyst','Problem Solving')
,('Junior Engineer','Problem Solving')
,('L&D Executuve','Problem Solving')
,('Ops Planning Exec','Problem Solving')
,('Sales Director','Problem Solving')
,('Sales Manager','Problem Solving')
,('Senior Engineer','Problem Solving')
,('Solutioning Director','Problem Solving')
,('Support Engineer','Problem Solving')
,('Account Manager','Product Management')
,('Consultancy Director','Product Management')
,('Consultant','Product Management')
,('Developer','Product Management')
,('Sales Director','Product Management')
,('Solutioning Director','Product Management')
,('Finance  Executive','Professional and Business Ethics')
,('Finance Director','Professional and Business Ethics')
,('Finance Manager','Professional and Business Ethics')
,('Consultancy Director','Project Management')
,('Consultant','Project Management')
,('Developer','Project Management')
,('Finance  Executive','Project Management')
,('Finance Manager','Project Management')
,('HR Director','Project Management')
,('IT Analyst','Project Management')
,('IT Director','Project Management')
,('Ops Planning Exec','Project Management')
,('Sales Director','Project Management')
,('Solutioning Director','Project Management')
,('Support Engineer','Project Management')
,('Finance Manager','Regulatory Compliance')
,('Finance Manager','Regulatory Risk Assessment')
,('Finance Director','Regulatory Strategy')
,('Sales Manager','Sales Closure')
,('Account Manager','Sales Strategy')
,('Consultancy Director','Sales Strategy')
,('Sales Director','Sales Strategy')
,('Solutioning Director','Sales Strategy')
,('Support Engineer','Security Administration')
,('Finance  Executive','Sense Making')
,('Junior Engineer','Sense Making')
,('IT Analyst','Service Level Management')
,('Support Engineer','Service Level Management')
,('HR Director','Skills Framework Adoption')
,('HR Executive','Skills Framework Adoption')
,('IT Director','Skills Framework Adoption')
,('L&D Executuve','Skills Framework Adoption')
,('Developer','Software Configuration')
,('Developer','Software Design')
,('Developer','Software Testing')
,('Developer','Solution Architecture')
,('Admin Executive','Solutions Design Thinking')
,('Ops Planning Exec','SOP Development and Implementation')
,('Account Manager','Stakeholder Management')
,('Admin Executive','Stakeholder Management')
,('Call Centre','Stakeholder Management')
,('Consultancy Director','Stakeholder Management')
,('Consultant','Stakeholder Management')
,('Developer','Stakeholder Management')
,('Engineering Director','Stakeholder Management')
,('Finance Director','Stakeholder Management')
,('Finance Manager','Stakeholder Management')
,('IT Analyst','Stakeholder Management')
,('Sales Director','Stakeholder Management')
,('Sales Manager','Stakeholder Management')
,('Solutioning Director','Stakeholder Management')
,('Support Engineer','Stakeholder Management')
,('Consultancy Director','Strategy Planning')
,('Sales Director','Strategy Planning')
,('Sales Manager','Strategy Planning')
,('Solutioning Director','Strategy Planning')
,('Developer','System Integration')
,('Support Engineer','System Integration')
,('HR Director','Talent Management')
,('Finance  Executive','Tax Computation')
,('Finance  Executive','Tax Implications')
,('Finance Director','Tax Implications')
,('Finance Manager','Tax Implications')
,('Call Centre','Technology Application')
,('Admin Executive','Technology Integration')
,('HR Director','Technology Integration')
,('IT Director','Technology Integration')
,('Sales Manager','Technology Integration')
,('Engineering Director','Technology Road Mapping')
,('Developer','User Interface Design');

DROP TABLE IF EXISTS `staff_skill`;
CREATE TABLE IF NOT EXISTS `staff_skill` (
    staff_id integer NOT NULL,
    skill_name varchar(50) NOT NULL,
    CONSTRAINT staff_skill_pkey PRIMARY KEY (staff_id, skill_name),
    CONSTRAINT staff_skill_fk1 FOREIGN KEY (skill_name) REFERENCES skills(skill_name) ON DELETE CASCADE,
    CONSTRAINT staff_skill_fk2 FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO staff_skill (staff_id, skill_name) VALUES
('140001','Account Management'),
('140001','Business Development'),
('140001','Customer Acquisition Management'),
('140001','Database Administration'),
('140001','Financial Statements Analysis'),
('140001','Pricing Strategy'),
('140001','Product Management'),
('140001','Technology Integration'),
('140002','Accounting and Tax Systems'),
('140002','Business Environment Analysis'),
('140002','Customer Relationship Management'),
('140002','Professional and Business Ethics'),
('140004','Account Management'),
('140004','Applications Development'),
('140004','Business Negotiation'),
('140004','Database Administration'),
('140004','Product Management');

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
('Consulting', 'Consultants are professionals who provide expert advice to organizations to help them improve their business performance, solve problems, and implement solutions. They are hired to analyze and assess current business processes, identify areas for improvement, and recommend strategies for enhanced efficiency and effectiveness.'),
('Design and Technical Service', 'Involves developing creative, tech-based solutions to existing problems'),
('Information Technology', 'Involves the implementation, support, maintenance, repair or protection of data or computer systems'),
('Engineering', 'Jobs that use science and mathematics to solve a variety of problems'),
('Finance', "Jobs where a company's funds and profitability are the primary focus"),
('Legal', 'Practicing the law'),
('Manufacturing and production', 'Involves the creation of new products either from raw materials or by assembling different components'),
('Marketing and advertising', "Responsible for planning, creating, and executing marketing campaigns to expand their company's reach and potential customer"),
('Sales and Communication', 'Customer service experience and sales skills');

DROP TABLE IF EXISTS `role_listing`;
CREATE TABLE IF NOT EXISTS `role_listing` (
    listing_id integer NOT NULL AUTO_INCREMENT,
    role_name varchar(50) NOT NULL,
    department varchar(100) NOT NULL,
    category varchar(120) NOT NULL,
    deadline date NOT NULL,
    CONSTRAINT role_listing_pkey PRIMARY KEY (listing_id),
    constraint role_listing_fk1 foreign key (category) references category(category) ON DELETE CASCADE,
    CONSTRAINT role_listing_fk2 FOREIGN KEY (role_name) REFERENCES role(role_name) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO role_listing (listing_id, role_name, department, category, deadline) VALUES
(1, 'HR Director', 'HR', 'Administration and Support', '2024-09-25'), 
(2, 'Senior Engineer', 'IT', 'Engineering', '2024-10-10'), 
(3, 'Finance Manager', 'Finance', 'Finance', '2023-10-10'), 
(4, 'Senior Engineer', 'IT', 'Information Technology', '2024-12-15'), 
(5, 'HR Executive', 'HR', 'Administration and Support', '2023-11-10'),
(6, 'Sales Manager', 'Sales', 'Sales and Communication', '2024-11-30'), 
(7, 'Consultant', 'Consultancy', 'Consulting', '2024-12-20'), 
(8, 'Engineering Director', 'Engineering', 'Information Technology', '2024-10-10'), 
(9, 'Finance  Executive', 'Finance', 'Finance', '2023-10-05'); 

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
(1, 140001, 1, '2023-09-19'), 
(2, 140002, 2, '2023-10-01'), 
(3, 140001, 3, '2023-08-01'), 
(4, 140002, 5, '2023-09-05'), 
(5, 140008, 7, '2023-09-15'), 
(6, 140004, 6, '2023-07-10'), 
(7, 140008, 9, '2023-09-01'), 
(8, 140004, 4, '2023-07-25');

DROP TABLE IF EXISTS `login_details`;
CREATE TABLE IF NOT EXISTS `login_details` (
    staff_id integer NOT NULL,
    staff_password varchar(255) NOT NULL,
    CONSTRAINT login_details_pkey PRIMARY KEY (staff_id),
    constraint login_details_fk1 foreign key (staff_id) references staff(staff_id) ON DELETE CASCADE
)  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO login_details (staff_id, staff_password) VALUES
(140001,'derek')
,(140002,'susan')
,(140008,'jaclyn')
,(140004,'mary');

COMMIT;