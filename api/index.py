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
    "about_intro": "You’ve wandered into a place where logic meets quiet magic. I build calm, resilient systems—cloud infrastructure, reliability engineering, and thoughtful automation.",
    "tech_stack": {
        "Cloud": ["AWS", "Docker", "Terraform"],
        "DevOps": ["CI/CD"],
        "Programming": ["Python", "Java"]
    },

}

@app.get("/")
def start():
    return render_template("start.html")

@app.get("/home")
def overview():
    return render_template("overview.html", profile=PROFILE, active_page="overview")

@app.get("/projects")
def projects():
    return render_template("projects.html", profile=PROFILE, active_page="projects")

@app.get("/about")
def about():
    return render_template("about.html", profile=PROFILE, active_page="about")
