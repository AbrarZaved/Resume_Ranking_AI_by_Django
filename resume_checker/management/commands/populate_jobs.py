from django.core.management.base import BaseCommand
from resume_checker.models import JobDescription


class Command(BaseCommand):
    help = "Populate the database with various job descriptions"

    def handle(self, *args, **kwargs):
        jobs = [
            {
                "job_title": "Senior Full Stack Developer",
                "job_description": """
We are seeking a highly skilled Senior Full Stack Developer to join our dynamic engineering team. In this role, you will be responsible for designing, developing, and maintaining both front-end and back-end components of our web applications. You will work closely with product managers, designers, and other developers to create scalable, high-performance solutions that meet our business objectives.

Key Responsibilities:
- Design and develop robust, scalable web applications using modern frameworks and technologies
- Build responsive and intuitive user interfaces using React, Vue.js, or Angular
- Develop RESTful APIs and microservices using Node.js, Python Django, or Java Spring Boot
- Implement database schemas and optimize queries for PostgreSQL, MySQL, or MongoDB
- Write clean, maintainable, and well-documented code following best practices
- Conduct code reviews and mentor junior developers
- Collaborate with cross-functional teams to define and implement new features
- Troubleshoot and debug complex issues in production environments
- Implement automated testing strategies including unit, integration, and end-to-end tests
- Stay updated with emerging technologies and industry trends

Required Skills:
- 5+ years of professional experience in full stack development
- Expert knowledge of JavaScript/TypeScript and modern frameworks (React, Vue.js, or Angular)
- Strong proficiency in at least one backend language (Python, Node.js, Java, or Go)
- Experience with RESTful API design and implementation
- Solid understanding of database design and SQL/NoSQL databases
- Proficiency with version control systems (Git)
- Experience with cloud platforms (AWS, Azure, or GCP)
- Knowledge of containerization technologies (Docker, Kubernetes)
- Strong understanding of software design patterns and SOLID principles
- Experience with CI/CD pipelines and DevOps practices
- Excellent problem-solving and analytical skills
- Strong communication and collaboration abilities

Requirements:
- Bachelor's degree in Computer Science, Software Engineering, or related field (or equivalent experience)
- Minimum 5 years of professional software development experience
- Portfolio or GitHub profile demonstrating technical expertise
- Experience working in Agile/Scrum development environments
- Proven track record of delivering high-quality software products
- Strong understanding of web security best practices
- Experience with testing frameworks (Jest, Mocha, PyTest, JUnit)
- Ability to work independently and as part of a team
- Excellent written and verbal communication skills

Compensation:
- Competitive salary range: $120,000 - $160,000 per year based on experience
- Comprehensive health, dental, and vision insurance
- 401(k) retirement plan with company matching up to 6%
- Flexible work arrangements with remote work options
- Professional development budget of $5,000 annually
- Performance-based bonuses up to 15% of base salary
- Stock options or equity participation
- Generous paid time off including 20 vacation days, 10 sick days, and major holidays
- Parental leave program
- Home office stipend for remote workers
- Annual company retreats and team-building events
""",
            },
            {
                "job_title": "Data Scientist - Machine Learning",
                "job_description": """
We are looking for an experienced Data Scientist specializing in Machine Learning to join our innovative AI team. You will work on cutting-edge projects involving predictive modeling, natural language processing, and deep learning to solve complex business challenges. This role offers the opportunity to work with large-scale datasets and deploy ML models that directly impact millions of users.

Key Responsibilities:
- Design and implement machine learning models for various business applications
- Analyze large-scale structured and unstructured datasets to extract meaningful insights
- Develop and deploy predictive models for forecasting, classification, and recommendation systems
- Build NLP models for text analysis, sentiment analysis, and language understanding
- Implement deep learning architectures using TensorFlow, PyTorch, or Keras
- Collaborate with engineering teams to productionize ML models
- Conduct A/B testing and statistical analysis to measure model performance
- Create data visualizations and dashboards to communicate findings to stakeholders
- Research and implement state-of-the-art ML techniques and algorithms
- Optimize model performance and scalability for production environments
- Document methodologies, findings, and best practices
- Mentor junior data scientists and contribute to team knowledge sharing

Required Skills:
- 3+ years of experience in data science and machine learning
- Strong proficiency in Python and ML libraries (scikit-learn, pandas, NumPy)
- Hands-on experience with deep learning frameworks (TensorFlow, PyTorch, Keras)
- Expertise in statistical analysis and hypothesis testing
- Experience with SQL and big data technologies (Spark, Hadoop, Hive)
- Knowledge of feature engineering and model optimization techniques
- Proficiency in data visualization tools (Matplotlib, Seaborn, Tableau, PowerBI)
- Understanding of ML operations (MLOps) and model deployment pipelines
- Experience with cloud ML services (AWS SageMaker, Azure ML, Google AI Platform)
- Strong mathematical foundation in linear algebra, calculus, and probability
- Knowledge of natural language processing techniques
- Experience with version control and collaborative development (Git)
- Excellent analytical and problem-solving skills
- Strong communication skills to explain complex concepts to non-technical audiences

Requirements:
- Master's or PhD in Computer Science, Statistics, Mathematics, or related field (or equivalent experience)
- Minimum 3 years of hands-on experience in building and deploying ML models
- Proven track record of delivering successful data science projects
- Experience with real-time model serving and monitoring
- Portfolio of ML projects or published research papers (preferred)
- Understanding of business metrics and KPIs
- Experience with experiment design and A/B testing frameworks
- Ability to work in a fast-paced, collaborative environment
- Strong project management and organizational skills

Compensation:
- Salary range: $130,000 - $180,000 per year depending on experience
- Comprehensive health benefits package (medical, dental, vision)
- 401(k) with 5% company match
- Flexible hybrid work model
- Annual learning and development budget of $6,000
- Access to premium online courses and conference attendance
- Performance bonuses up to 20% of base salary
- Stock options or RSUs
- 25 days of paid time off plus holidays
- Wellness programs and gym membership reimbursement
- Latest technology and equipment for your work
- Collaborative and inclusive work culture
""",
            },
            {
                "job_title": "DevOps Engineer",
                "job_description": """
We are seeking a talented DevOps Engineer to join our infrastructure team and help build and maintain our cloud-based systems. You will play a crucial role in automating our deployment processes, ensuring system reliability, and implementing best practices for continuous integration and continuous delivery. This position is ideal for someone who is passionate about automation, infrastructure as code, and building scalable systems.

Key Responsibilities:
- Design, implement, and maintain CI/CD pipelines for automated testing and deployment
- Manage and optimize cloud infrastructure on AWS, Azure, or Google Cloud Platform
- Implement infrastructure as code using Terraform, CloudFormation, or Ansible
- Configure and maintain containerization platforms (Docker, Kubernetes)
- Monitor system performance and implement alerting solutions
- Automate routine operational tasks to improve efficiency
- Implement security best practices and ensure compliance with industry standards
- Manage version control systems and branching strategies
- Troubleshoot production issues and perform root cause analysis
- Collaborate with development teams to optimize application performance
- Implement disaster recovery and backup strategies
- Document processes, procedures, and system architectures
- Participate in on-call rotation for production support
- Evaluate and recommend new tools and technologies

Required Skills:
- 3+ years of experience in DevOps, SRE, or system administration
- Strong proficiency with at least one cloud platform (AWS, Azure, or GCP)
- Expert knowledge of containerization technologies (Docker, Kubernetes)
- Experience with infrastructure as code tools (Terraform, CloudFormation, Ansible)
- Proficiency in scripting languages (Python, Bash, PowerShell)
- Strong understanding of CI/CD concepts and tools (Jenkins, GitLab CI, GitHub Actions, CircleCI)
- Experience with configuration management tools (Ansible, Chef, Puppet)
- Knowledge of monitoring and logging solutions (Prometheus, Grafana, ELK Stack, Datadog)
- Understanding of networking concepts (DNS, load balancing, VPN, firewalls)
- Experience with database administration (PostgreSQL, MySQL, MongoDB)
- Knowledge of security best practices and compliance frameworks
- Strong Linux/Unix administration skills
- Experience with version control systems (Git)
- Excellent troubleshooting and problem-solving abilities

Requirements:
- Bachelor's degree in Computer Science, Information Technology, or related field (or equivalent experience)
- Minimum 3 years of hands-on DevOps or infrastructure experience
- Relevant certifications (AWS Certified Solutions Architect, CKA, or similar) preferred
- Experience with microservices architecture
- Understanding of Agile methodologies
- Strong documentation skills
- Ability to work in a fast-paced environment
- Excellent communication and collaboration skills
- Experience with on-call responsibilities and incident management
- Commitment to continuous learning and improvement

Compensation:
- Competitive salary: $110,000 - $150,000 per year based on experience
- Comprehensive health insurance (medical, dental, vision, life insurance)
- 401(k) retirement plan with 6% company contribution
- Remote-first culture with flexible working hours
- Professional development and certification reimbursement up to $4,000 annually
- Performance-based annual bonus up to 12% of salary
- Stock options
- 22 days paid vacation plus holidays and sick leave
- Parental leave benefits
- Home office equipment and ergonomic furniture allowance
- Team building activities and annual company offsite
- Mental health and wellness support programs
""",
            },
            {
                "job_title": "UX/UI Designer",
                "job_description": """
We are looking for a creative and user-focused UX/UI Designer to join our design team. In this role, you will be responsible for creating exceptional user experiences across our digital products. You will work closely with product managers, developers, and other designers to transform complex requirements into intuitive, accessible, and aesthetically pleasing interfaces that delight our users.

Key Responsibilities:
- Conduct user research, interviews, and usability testing to understand user needs and pain points
- Create user personas, journey maps, and user flow diagrams
- Design wireframes, mockups, and interactive prototypes using industry-standard tools
- Develop comprehensive design systems and component libraries
- Create high-fidelity visual designs that align with brand guidelines
- Collaborate with developers to ensure accurate implementation of designs
- Conduct design reviews and iterate based on feedback from stakeholders and users
- Stay current with design trends, tools, and best practices
- Advocate for user-centered design principles across the organization
- Create and present design concepts to stakeholders and executive leadership
- Perform competitive analysis and benchmark against industry standards
- Ensure designs meet accessibility standards (WCAG)
- Participate in design critiques and provide constructive feedback to team members
- Contribute to the evolution of our design language and processes

Required Skills:
- 3+ years of professional experience in UX/UI design
- Expert proficiency in design tools (Figma, Sketch, Adobe XD)
- Strong portfolio demonstrating excellent visual design and UX problem-solving skills
- Experience with prototyping tools (InVision, Principle, ProtoPie, Figma)
- Knowledge of user research methodologies and usability testing
- Understanding of information architecture and interaction design principles
- Proficiency in creating and maintaining design systems
- Knowledge of HTML, CSS, and responsive design principles
- Experience with design handoff tools (Zeplin, Abstract, Figma)
- Understanding of accessibility standards and inclusive design
- Strong visual design skills including typography, color theory, and layout
- Experience with motion design and micro-interactions (preferred)
- Familiarity with front-end frameworks and design constraints
- Excellent communication and presentation skills
- Strong attention to detail and commitment to pixel-perfect design

Requirements:
- Bachelor's degree in Design, HCI, or related field (or equivalent experience)
- Minimum 3 years of UX/UI design experience for web and mobile applications
- Portfolio showcasing end-to-end design projects and design thinking process
- Experience working in Agile/Scrum environments
- Understanding of both iOS and Android design guidelines
- Experience designing for diverse user groups and international markets
- Ability to balance business goals with user needs
- Strong collaboration skills and ability to work with cross-functional teams
- Self-motivated with excellent time management abilities
- Passion for creating user-centered designs
- Experience with A/B testing and data-driven design decisions

Compensation:
- Salary range: $90,000 - $130,000 per year based on experience
- Comprehensive benefits package including health, dental, and vision insurance
- 401(k) with company match up to 5%
- Flexible work environment with hybrid or remote options
- Annual professional development budget of $3,500
- Access to design conferences and workshops
- Performance-based bonuses up to 10% of base salary
- Stock options or equity
- 20 days PTO plus holidays
- Ergonomic workspace and latest design tools
- Creative environment with talented team members
- Regular design team activities and knowledge sharing sessions
""",
            },
            {
                "job_title": "Product Manager",
                "job_description": """
We are seeking an experienced Product Manager to lead the strategy and execution of our product initiatives. In this role, you will be the voice of the customer, working at the intersection of business, technology, and user experience to deliver products that solve real problems and drive business value. You will own the product roadmap, prioritize features, and work with cross-functional teams to bring products to market.

Key Responsibilities:
- Define and communicate product vision, strategy, and roadmap
- Conduct market research and competitive analysis to identify opportunities
- Gather and analyze user feedback through interviews, surveys, and data analysis
- Create and prioritize product backlog based on business value and user impact
- Write detailed user stories, acceptance criteria, and product requirements
- Collaborate with design and engineering teams throughout the product development lifecycle
- Make data-driven decisions using analytics and key performance indicators
- Lead sprint planning, refinement sessions, and backlog grooming
- Coordinate product launches and go-to-market strategies
- Work with stakeholders across the organization to align on priorities
- Monitor product performance and iterate based on user feedback and metrics
- Define success metrics and track product KPIs
- Communicate product updates to executives, customers, and internal teams
- Manage product lifecycle from conception to retirement
- Advocate for technical improvements and manage technical debt

Required Skills:
- 4+ years of experience in product management for digital products
- Strong understanding of Agile/Scrum methodologies
- Experience with product analytics tools (Google Analytics, Mixpanel, Amplitude)
- Proficiency in product management tools (Jira, Asana, Productboard, Aha!)
- Excellent analytical and data interpretation skills
- Strong understanding of user experience design principles
- Experience with A/B testing and experiment design
- Knowledge of software development processes and technical concepts
- Excellent stakeholder management and communication skills
- Strong prioritization and decision-making abilities
- Experience creating product roadmaps and strategy documents
- Understanding of business models and go-to-market strategies
- Ability to translate technical concepts for non-technical audiences
- Experience with SQL or data analysis tools (preferred)
- Knowledge of design thinking and lean startup methodologies

Requirements:
- Bachelor's degree in Business, Computer Science, Engineering, or related field; MBA preferred
- Minimum 4 years of product management experience
- Proven track record of successfully launching and scaling products
- Experience managing products through full product lifecycle
- Strong understanding of both B2B and B2C product dynamics
- Experience working with engineering, design, sales, and marketing teams
- Demonstrated ability to influence without authority
- Strong problem-solving and critical thinking skills
- Excellent written and verbal communication skills
- Customer-centric mindset with passion for solving user problems
- Experience in SaaS, mobile apps, or consumer technology (preferred)
- Technical background or ability to quickly learn technical concepts

Compensation:
- Salary range: $120,000 - $170,000 per year depending on experience
- Comprehensive health benefits (medical, dental, vision, life insurance)
- 401(k) retirement plan with 5% company matching
- Flexible work arrangements including remote options
- Annual learning budget of $5,000 for courses and conferences
- Performance-based bonuses up to 20% of base salary
- Stock options or equity stake in company growth
- 25 days of paid time off plus holidays
- Parental leave program
- Company-sponsored product management certifications
- Access to industry events and networking opportunities
- Collaborative culture with opportunity for career growth
- Regular team offsites and product strategy sessions
""",
            },
            {
                "job_title": "Cybersecurity Analyst",
                "job_description": """
We are hiring a Cybersecurity Analyst to protect our organization's critical assets and ensure the security of our systems, networks, and data. You will be responsible for monitoring security events, identifying vulnerabilities, responding to incidents, and implementing security best practices. This role is perfect for someone who is passionate about information security and wants to make a real impact in protecting against cyber threats.

Key Responsibilities:
- Monitor security alerts and events using SIEM tools and security monitoring platforms
- Conduct vulnerability assessments and penetration testing
- Investigate and respond to security incidents and breaches
- Perform threat hunting and analysis of suspicious activities
- Implement and maintain security controls and policies
- Conduct security audits and risk assessments
- Develop and maintain incident response procedures and playbooks
- Analyze malware and conduct forensic investigations
- Manage security tools including firewalls, IDS/IPS, and endpoint protection
- Collaborate with IT teams to remediate security vulnerabilities
- Create security awareness training materials for employees
- Stay updated on latest security threats, vulnerabilities, and attack techniques
- Participate in security assessments of new applications and systems
- Document security procedures, findings, and recommendations
- Contribute to security architecture and design decisions

Required Skills:
- 3+ years of experience in cybersecurity or information security
- Strong knowledge of security frameworks (NIST, ISO 27001, CIS Controls)
- Experience with SIEM tools (Splunk, QRadar, ArcSight, ELK)
- Proficiency in network security and protocols (TCP/IP, DNS, HTTP/HTTPS)
- Knowledge of security tools (Nessus, Qualys, Metasploit, Wireshark)
- Understanding of cloud security (AWS, Azure, GCP)
- Experience with endpoint detection and response (EDR) solutions
- Knowledge of identity and access management (IAM) principles
- Familiarity with security automation and orchestration (SOAR)
- Understanding of web application security and OWASP Top 10
- Experience with scripting languages (Python, PowerShell, Bash)
- Knowledge of malware analysis and reverse engineering techniques
- Understanding of encryption, PKI, and cryptographic protocols
- Strong analytical and problem-solving skills
- Excellent written and verbal communication abilities

Requirements:
- Bachelor's degree in Computer Science, Information Security, or related field
- Minimum 3 years of hands-on cybersecurity experience
- Relevant certifications such as Security+, CEH, CISSP, GCIA, or GCIH (preferred)
- Experience with incident response and forensic investigations
- Knowledge of compliance requirements (GDPR, HIPAA, PCI-DSS, SOC 2)
- Understanding of threat intelligence and threat modeling
- Experience with penetration testing methodologies
- Ability to work in high-pressure situations and respond to security incidents
- Strong attention to detail and ability to identify subtle anomalies
- Continuous learning mindset to stay current with evolving threats
- Experience with security information sharing and collaboration
- Ability to communicate security risks to technical and non-technical audiences

Compensation:
- Competitive salary: $100,000 - $140,000 per year based on experience
- Comprehensive health insurance package (medical, dental, vision)
- 401(k) with 6% company match
- Remote work options with flexible schedule
- Professional development budget of $5,000 annually for certifications and training
- Bonus structure up to 15% of base salary
- Stock options
- 20 days paid vacation plus sick leave and holidays
- Certification exam fees and renewal costs covered
- Access to cybersecurity conferences and training events
- Latest security tools and technologies
- Collaborative security team environment
- Opportunity to work on challenging security projects
""",
            },
            {
                "job_title": "Mobile Application Developer - iOS",
                "job_description": """
We are looking for an experienced iOS Developer to join our mobile development team. You will design and build advanced applications for the iOS platform, working on both new features and maintaining existing functionality. This role offers the opportunity to create delightful mobile experiences for millions of users while working with the latest iOS technologies and frameworks.

Key Responsibilities:
- Design and build advanced iOS applications using Swift and SwiftUI
- Collaborate with cross-functional teams to define and ship new features
- Implement clean, maintainable, and efficient code following iOS best practices
- Work on bug fixing and improving application performance
- Continuously discover, evaluate, and implement new technologies
- Integrate with RESTful APIs and third-party libraries
- Write unit tests and UI tests to ensure code quality
- Participate in code reviews and provide constructive feedback
- Work closely with UI/UX designers to implement pixel-perfect designs
- Optimize applications for maximum performance and scalability
- Implement offline-first capabilities and data synchronization
- Handle App Store submission process and manage releases
- Debug and resolve technical issues and crashes
- Mentor junior developers and share knowledge with the team
- Stay up-to-date with iOS platform updates and new features

Required Skills:
- 4+ years of professional iOS development experience
- Expert proficiency in Swift and SwiftUI/UIKit
- Strong understanding of iOS SDK, Xcode, and development tools
- Experience with iOS frameworks (Core Data, Core Animation, Core Graphics)
- Knowledge of RESTful APIs and JSON parsing
- Proficiency with Git and version control workflows
- Experience with dependency managers (CocoaPods, Swift Package Manager, Carthage)
- Understanding of MVVM, MVC, or other architectural patterns
- Experience with asynchronous programming and Grand Central Dispatch
- Knowledge of memory management and performance optimization
- Familiarity with push notifications and deep linking
- Experience with App Store Connect and app submission process
- Understanding of mobile security best practices
- Proficiency in debugging tools and instruments
- Strong problem-solving and analytical skills
- Excellent communication and teamwork abilities

Requirements:
- Bachelor's degree in Computer Science or related field (or equivalent experience)
- Minimum 4 years of iOS development experience
- Published iOS apps in the App Store (portfolio required)
- Experience with CI/CD for mobile applications (Fastlane, Bitrise)
- Knowledge of reactive programming (RxSwift or Combine)
- Understanding of Apple Human Interface Guidelines
- Experience with offline storage and threading
- Familiarity with cloud message APIs and push notifications
- Experience working in Agile development environment
- Strong attention to UI/UX details
- Ability to work independently and in team settings
- Passion for mobile technology and creating great user experiences
- Experience with A/B testing and analytics integration

Compensation:
- Salary range: $115,000 - $155,000 per year based on experience
- Comprehensive benefits including health, dental, and vision insurance
- 401(k) retirement plan with 5% employer match
- Hybrid work model with flexible hours
- Annual professional development allowance of $4,000
- Performance bonuses up to 15% of base salary
- Stock options or RSUs
- 22 days of paid time off plus holidays
- Latest MacBook Pro and iPhone for development
- Apple Developer Program membership covered
- Conference attendance and training opportunities
- Collaborative and innovative work environment
- Regular team events and hackathons
""",
            },
            {
                "job_title": "Cloud Solutions Architect",
                "job_description": """
We are seeking a highly skilled Cloud Solutions Architect to design and implement scalable, secure, and cost-effective cloud infrastructure solutions. You will work closely with engineering teams, stakeholders, and clients to architect cloud-native applications and migrate legacy systems to the cloud. This role requires deep expertise in cloud platforms and the ability to translate business requirements into technical solutions.

Key Responsibilities:
- Design end-to-end cloud solutions architecture for complex enterprise applications
- Lead cloud migration projects from planning through execution
- Evaluate and recommend cloud services and tools based on requirements
- Create detailed architecture diagrams, documentation, and technical specifications
- Implement cloud security best practices and compliance frameworks
- Design high-availability, fault-tolerant, and disaster recovery solutions
- Optimize cloud infrastructure for performance and cost efficiency
- Establish cloud governance policies and standards
- Conduct architecture reviews and provide technical guidance to development teams
- Automate infrastructure provisioning using IaC tools
- Design and implement multi-region and multi-cloud strategies
- Collaborate with DevOps teams on CI/CD pipeline architecture
- Provide technical leadership during pre-sales and client engagements
- Mentor and train team members on cloud technologies
- Stay current with cloud platform innovations and industry trends

Required Skills:
- 6+ years of experience in cloud architecture and engineering
- Expert knowledge of major cloud platforms (AWS, Azure, or Google Cloud)
- Strong experience with infrastructure as code (Terraform, CloudFormation, ARM templates)
- Deep understanding of cloud networking, security, and identity management
- Experience designing microservices and serverless architectures
- Proficiency with containerization and orchestration (Docker, Kubernetes)
- Knowledge of database services and data architecture in cloud environments
- Experience with cloud cost optimization and FinOps practices
- Strong understanding of DevOps practices and CI/CD pipelines
- Experience with monitoring, logging, and observability solutions
- Knowledge of compliance frameworks (SOC 2, ISO 27001, HIPAA, PCI-DSS)
- Excellent architectural documentation and diagramming skills
- Strong scripting abilities (Python, PowerShell, Bash)
- Experience with API design and management
- Outstanding communication and presentation skills

Requirements:
- Bachelor's or Master's degree in Computer Science, Engineering, or related field
- Minimum 6 years of hands-on cloud architecture experience
- Cloud certifications required (AWS Solutions Architect Professional, Azure Solutions Architect Expert, or Google Cloud Professional Architect)
- Proven track record of successful cloud migration projects
- Experience with enterprise-scale deployments
- Strong understanding of networking concepts and protocols
- Experience with Agile methodologies and working with cross-functional teams
- Ability to balance technical excellence with business pragmatism
- Strong problem-solving and analytical capabilities
- Excellent stakeholder management skills
- Experience with Well-Architected Framework reviews
- Background in software development or systems engineering

Compensation:
- Salary range: $150,000 - $200,000 per year depending on experience
- Comprehensive health benefits (medical, dental, vision, life insurance)
- 401(k) plan with 6% company contribution
- Flexible remote work policy
- Professional development budget of $7,000 annually
- Cloud certification exam fees and renewals covered
- Annual performance bonus up to 20% of base salary
- Equity or stock options
- 25 days of paid vacation plus holidays and sick leave
- Conference attendance including AWS re:Invent, Microsoft Ignite, Google Cloud Next
- Home office setup allowance
- Health and wellness programs
- Collaborative culture with opportunities for innovation
""",
            },
            {
                "job_title": "Quality Assurance Engineer",
                "job_description": """
We are hiring a Quality Assurance Engineer to ensure the quality and reliability of our software products. You will design and execute comprehensive test strategies, create automated test suites, and work closely with development teams to identify and prevent defects. This role is ideal for someone who is detail-oriented, analytical, and passionate about delivering high-quality software.

Key Responsibilities:
- Design and develop comprehensive test plans and test cases
- Execute manual and automated tests for web and mobile applications
- Create and maintain automated test scripts using industry-standard frameworks
- Perform functional, regression, integration, and performance testing
- Identify, document, and track software defects through resolution
- Collaborate with developers to reproduce and diagnose issues
- Conduct API testing using tools like Postman or REST Assured
- Participate in requirement reviews and provide QA perspective
- Perform exploratory testing to identify edge cases and usability issues
- Set up and maintain test environments and test data
- Integrate automated tests into CI/CD pipelines
- Monitor and analyze test results and metrics
- Conduct accessibility and security testing
- Create and maintain test documentation and QA processes
- Mentor junior QA team members and promote quality culture

Required Skills:
- 3+ years of experience in software quality assurance
- Strong knowledge of QA methodologies and best practices
- Experience with test automation frameworks (Selenium, Cypress, Playwright, Appium)
- Proficiency in at least one programming language (Python, Java, JavaScript)
- Experience with API testing tools (Postman, SoapUI, REST Assured)
- Knowledge of performance testing tools (JMeter, LoadRunner, Gatling)
- Understanding of SQL and database testing
- Familiarity with CI/CD tools (Jenkins, GitLab CI, GitHub Actions)
- Experience with test management tools (TestRail, Zephyr, qTest)
- Knowledge of version control systems (Git)
- Understanding of Agile/Scrum methodologies
- Experience with bug tracking systems (Jira, Bugzilla)
- Strong analytical and problem-solving skills
- Excellent attention to detail
- Good communication and collaboration abilities

Requirements:
- Bachelor's degree in Computer Science, Engineering, or related field
- Minimum 3 years of QA engineering experience
- Experience testing web applications, mobile apps, and APIs
- Hands-on experience with test automation frameworks
- Understanding of software development lifecycle
- Experience with both black-box and white-box testing
- Knowledge of security testing principles (preferred)
- ISTQB certification or equivalent (preferred)
- Experience with cross-browser and cross-platform testing
- Ability to work in fast-paced Agile environment
- Strong organizational and time management skills
- Self-motivated with ability to work independently
- Passion for quality and continuous improvement

Compensation:
- Salary range: $85,000 - $120,000 per year based on experience
- Comprehensive health insurance (medical, dental, vision)
- 401(k) with 5% company match
- Flexible work arrangements including remote options
- Professional development budget of $3,000 annually
- QA certification and training support
- Performance-based bonuses up to 10% of base salary
- Stock options
- 20 days PTO plus holidays and sick days
- Collaborative team environment
- Modern testing tools and technologies
- Career growth opportunities
- Regular team building activities
""",
            },
            {
                "job_title": "Business Intelligence Analyst",
                "job_description": """
We are looking for a Business Intelligence Analyst to transform data into actionable insights that drive business decisions. You will work with stakeholders across the organization to understand their data needs, create reports and dashboards, and provide analytical support for strategic initiatives. This role combines technical skills with business acumen to deliver data-driven solutions.

Key Responsibilities:
- Design, develop, and maintain interactive dashboards and reports
- Analyze complex datasets to identify trends, patterns, and insights
- Collaborate with stakeholders to understand business requirements
- Create data models and dimensional schemas for data warehousing
- Write complex SQL queries to extract and transform data
- Perform ad-hoc analysis to support business decisions
- Develop KPIs and metrics to measure business performance
- Present findings and recommendations to executive leadership
- Ensure data quality and integrity across reporting systems
- Optimize query performance and dashboard load times
- Document data sources, definitions, and methodologies
- Train end users on BI tools and self-service analytics
- Participate in data governance and master data management initiatives
- Identify opportunities for process improvement through data analysis
- Stay current with BI tools, technologies, and best practices

Required Skills:
- 3+ years of experience in business intelligence or data analytics
- Expert proficiency in SQL for data querying and manipulation
- Strong experience with BI tools (Tableau, Power BI, Looker, or Qlik)
- Knowledge of data warehousing concepts and dimensional modeling
- Experience with ETL processes and data integration tools
- Proficiency in Excel including advanced formulas, pivot tables, and macros
- Understanding of statistical analysis methods
- Experience with Python or R for data analysis (preferred)
- Knowledge of database systems (SQL Server, PostgreSQL, MySQL, Oracle)
- Strong data visualization and storytelling skills
- Experience with cloud data platforms (Snowflake, Redshift, BigQuery)
- Understanding of data governance and data quality principles
- Excellent analytical and problem-solving abilities
- Strong communication skills to explain technical concepts to business users
- Attention to detail and commitment to accuracy

Requirements:
- Bachelor's degree in Business, Statistics, Computer Science, or related field
- Minimum 3 years of BI analyst or data analyst experience
- Proven track record of delivering impactful BI solutions
- Experience working with large datasets and complex data structures
- Strong business acumen and understanding of key business metrics
- Experience collaborating with cross-functional teams
- Ability to translate business requirements into technical specifications
- Knowledge of Agile methodologies
- Self-starter with ability to manage multiple priorities
- Strong presentation and stakeholder management skills
- Experience in specific industry vertical (e-commerce, finance, healthcare) preferred
- Certification in BI tools (Tableau Desktop Specialist, Microsoft Certified: Power BI) preferred

Compensation:
- Salary range: $80,000 - $115,000 per year depending on experience
- Full health benefits package (medical, dental, vision, life insurance)
- 401(k) retirement plan with 4% company match
- Hybrid work model with flexibility
- Annual training budget of $2,500 for courses and certifications
- Performance bonuses up to 12% of base salary
- Stock options
- 18 days paid vacation plus holidays
- Professional development opportunities
- Modern BI tools and data platforms
- Collaborative culture focused on data-driven decision making
- Regular lunch and learns with data team
""",
            },
        ]

        # Create job descriptions
        created_count = 0
        for job_data in jobs:
            job, created = JobDescription.objects.get_or_create(
                job_title=job_data["job_title"],
                defaults={"job_description": job_data["job_description"]},
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created job: {job.job_title}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Job already exists: {job.job_title}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nCompleted! Created {created_count} new job descriptions."
            )
        )
