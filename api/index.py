from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static",
    static_url_path="/static",
)

PROFILE = {
    "owner_nickname": "Chrysalis",
    "owner_name": "Chrysalis Woon",
    "website_creation": "Jan 2026",
    "role": "Systems Analyst",
    "role_description": "focused on cloud infrastructure, reliability, and making complex problems feel simple",
    "about_intro_line1": "Hello! I’m Chrysalis, a passionate software developer and DevOps enthusiast. My experience spans across various programming languages and frameworks, enabling me to contribute effectively to full-stack development and DevOps practices. ",
    "about_intro_line2": "I am currently exploring opportunities where I can apply my skills in continuous integration and deployment, infrastructure as code, and collaborative software development to drive impactful solutions in the tech industry.",

"tech_stack_carousel": [
            {
        "name": "AWS",
        "icon": "assets/tech/aws.png"
    },
            {
        "name": "Docker",
        "icon": "assets/tech/docker.png"
    },
            {
        "name": "Linux",
        "icon": "assets/tech/linux.png"
    },
            {
        "name": "Git",
        "icon": "assets/tech/git.png"
    },
            {
        "name": "CI/CD",
        "icon": "assets/tech/cicd.png"
    },

    {
        "name": "Python",
        "icon": "assets/tech/python.png"
    },
            {
        "name": "Javascript",
        "icon": "assets/tech/javascript.png"
    },
            {
        "name": "React",
        "icon": "assets/tech/react.png"
    },
            {
        "name": "Angular",
        "icon": "assets/tech/angular.png"
    },
            {
        "name": "Spring Boot",
        "icon": "assets/tech/springboot.png"
    },
            {
        "name": "HTML/CSS",
        "icon": "assets/tech/htmlcss.png"
    },
            {
        "name": "MySQL",
        "icon": "assets/tech/sql.png"
    },
            {
        "name": "MongoDB",
        "icon": "assets/tech/mongodb.png"
    },
            {
        "name": "Redis",
        "icon": "assets/tech/redis.png"
    },
            {
        "name": "Jira",
        "icon": "assets/tech/jira.png"
    },
],

}

PROJECTS = [

    {
        "slug": "booktribe",
        "title": "BookTribe",
        "subtitle": "Reading Platform Using Modern Full-Stack Architecture",
        "image": "assets/projects/booktribe.png",
         "modal_image": "",
        "stack": ["Angular", "Spring Boot", "MySQL", "DigitalOcean"],
                        "shots": [
                            "assets/projects/booktribe/register.png",
                            "assets/projects/booktribe/login.png",
                            "assets/projects/booktribe/contact.png",


        ],
        "description": (
            "Developed a full-stack reading platform with user authentication "
            "and dynamic content rendering. Implemented RESTful APIs and "
            "deployed a scalable backend on DigitalOcean."
        ),
        "links": {
            "github": "https://github.com/yourname/booktribe",
            "slides": "https://your-presentation-link",
            "demo": None
        },
        "tags": ["Full Stack", "REST API"],
        "featured": True
    },

    {
        "slug": "financial-tracker",
        "title": "Finance Tracker",
        "subtitle": "Collaborative Expense Tracking App",
        "image": "assets/projects/finance_tracker.png",
                 "modal_image": "",
        "stack": [
            "MongoDB", "Express.js", "React", "Node.js", "Vercel"
        ],
        "description": (
            "Built a full-stack expense tracking application supporting "
            "multi-user input and real-time updates. Designed collaborative "
            "wireframes and user flows in Figma, implemented Git workflows, "
            "and deployed via Vercel for CI/CD."
        ),
        "links": {
            "github": "https://github.com/yourname/financial-tracker",
            "demo": None
        },
        "tags": ["MERN", "CI/CD", "Collaboration"],
        "featured": False
    },
            {
        "slug": "cloudscale",
        "title": "Cloud Scale",
        "subtitle": "Automated Report Generation Using AWS Cloud Services",
        "image": "assets/projects/cloudscale.png",
        "modal_image": "assets/projects/cloudscale.png",
        "stack": ["AWS Lambda", "EC2", "Apache Superset"],
        "shots": [
            "assets/projects/cloudscale/dashboard.png",
            "assets/projects/cloudscale/login.png",
            "assets/projects/cloudscale/project_structure.png"
        ],

        "description": (
            "This capstone project is designed to demonstrate the use of AWS infrastructure for managing scalable cloud environments, a serverless Lambda-based application, and Apache Superset for data visualization.\n\n"
            "The goal is to provide a solution that integrates these components to offer efficient, scalable, and user-friendly data management and visualization."
            
        ),
        "links": {
            "docs": "https://chrysalis-1.gitbook.io/sctp-capstone-project/",
            "github": None,
            "demo": None
        },
        "tags": ["Cloud", "Serverless", "Analytics"],
        "featured": True
    },
    {
        "slug": "catris",
        "title": "Catris",
        "subtitle": "Cat-Themed Puzzle Game Inspired by Classic Tetris",
        "image": "assets/projects/catris.png",

    },
        {
        "slug": "landscape game",
        "title": "Landscape Game",
        "subtitle": "Landscape game inspired by Coffee Tycoon",
        "image": "assets/projects/landscape.png",

    },

]

EXPERIENCES = [
  {
    "role": "Sr. Systems Application Support",
    "company": "Visa Worldwide Pte Ltd",
    "dates": "June 2023 – July 2025",
    "links": {
      "website": "https://www.visa.com"
    },
    "summary": "Supported mission-critical zTPF mainframe systems powering global payment transactions, ensuring high availability and operational reliability.",
    "bullets": [
      "Provided system-level operational support for Visa’s zTPF mainframe environments powering global payment transactions.",
      "Troubleshoot technical incidents, coordinated with cross-regional engineering teams, and ensured uptime compliance.",
      "Authored detailed technical documentation for MQ channel configurations and system workflows.",
      "Assisted infrastructure teams with deployments and configuration updates to support zero-downtime change initiatives.",
      "Collaborated with global support and development teams to analyze and resolve performance issues."
    ],
    "tags": ["Mainframe Systems", "Incident Management", "High Availability", "Production Support", "Global Operations"]
  },
  {
    "role": "Associate Systems Analyst Trainee",
    "company": "Visa Worldwide Pte Ltd",
    "dates": "May 2022 – June 2023",
    "links": {},
    "summary": "Provided frontline operational support for enterprise systems, responding to incidents, monitoring system health, and escalating issues through ITSM workflows.",
    "bullets": [
      "Responded to IT incidents and system alerts, assisting in maintaining 24/7 operational reliability.",
      "Monitored system metrics and escalated issues through ServiceNow and internal ticketing systems.",
      "Documented recurring issues and contributed to internal knowledge bases for smoother handovers.",
      "Supported production system maintenance and user access management processes in alignment with ITIL standards."
    ],
    "tags": ["IT Operations", "Monitoring & Alerts", "ServiceNow", "ITIL", "Production Support"]
  },
    {
    "role": "Instructional Team",
    "company": "Kodecoon Academy",
    "dates": "Nov 2021 – Mar 2023",
    "links": {},
    "summary": "Combined technical expertise with teaching and program design to make software development accessible and engaging for learners.",
    "bullets": [
      "Delivered hands-on programming instruction in Python, JavaScript, and web development (HTML/CSS/JS) to youth learners.",
      "Spearheaded curriculum redesign initiatives, increasing student retention rates by 40%.",
      "Collaborated with internal dev teams to produce scalable digital learning materials and optimize content delivery pipelines.",
    ],
    "tags": ["Technical Education", "Python & Javascript", "Curriculum Design", "EdTech", "Content Delivery"]
  },
      {
    "role": "Product Team",
    "company": "Saturday Kids",
    "dates": "Feb 2018 – Nov 2021",
    "links": {},
    "summary": "Bridged product thinking with execution, ensuring that growth was supported by automation, documentation, and repeatable workflows.",
    "bullets": [
      "Designed and launched 8+ technical education products, contributing to consistent annual revenue growth.",
      "Developed an internal ATS system using Airtable, automating 60% of recruitment workflows and reducing manual HR processes.",
      "Standardized onboarding frameworks for new technical instructors, cutting training time by 50% through reusable documentation and process improvements.",
    ],
    "tags": ["Product Development", "Process Automation", "Airtable", "Operations & Optimization"]
  },
]


@app.get("/")
def start():
    return render_template("start.html")

@app.get("/home")
def overview():
    return render_template("overview.html", profile=PROFILE, active_page="overview")

@app.get("/projects")
def projects():
    return render_template(
        "projects.html",
        profile=PROFILE,     # keep profile for the left panel + navbar brand
        projects=PROJECTS,   # projects data for the grid
        active_page="projects"
    )


@app.get("/about")
def about():
    return render_template("about.html", profile=PROFILE, experiences = EXPERIENCES, active_page="about")
