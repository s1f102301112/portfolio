# app.py
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# プロジェクトデータ読み込み
def load_projects():
    with open("data/projects.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    projects = load_projects()
    return render_template("projects.html", projects=projects)

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Render での公開用
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
