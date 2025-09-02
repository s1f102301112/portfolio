from flask import Flask, render_template, json

app = Flask(__name__)

# プロジェクト情報をJSONから読み込む
def load_projects():
    with open("data/projects.json", encoding="utf-8") as f:
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

if __name__ == "__main__":
    app.run(debug=True)
