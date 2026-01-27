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

    "tech_stack": {
        "Cloud": ["AWS", "Docker", "Terraform"],
        "DevOps": ["CI/CD"],
        "Programming": ["Python", "Java"]
    },

}

PROJECTS = [
        {
        "slug": "cloudscale",
        "title": "Cloud Scale",
        "subtitle": "Automated Report Generation Using AWS Cloud Services",
        "image": "assets/projects/cloudscale.png",
        "stack": ["AWS Lambda", "EC2", "Apache Superset"],
                "shots": [

        ],
        "description": (
            "Designed a scalable analytics platform using cost-effective, "
            "serverless architecture with AWS Lambda. Visualized real-time "
            "data pipelines with Superset and integrated monitoring to track usage."
        ),
        "links": {
            "docs": "https://your-gitbook-link",
            "github": None,
            "demo": None
        },
        "tags": ["Cloud", "Serverless", "Analytics"],
        "featured": True
    },

    {
        "slug": "booktribe",
        "title": "BookTribe",
        "subtitle": "Reading Platform Using Modern Full-Stack Architecture",
        "image": "assets/projects/booktribe.png",
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
    return render_template("about.html", profile=PROFILE, active_page="about")
