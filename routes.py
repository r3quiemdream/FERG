from flask import Flask, render_template
# import os

app = Flask(__name__)

@app.route("/")
def index(guest="Hoss"):
    return render_template("index.html", guest=guest)

@app.route("/professionallife")
def professionallife():
    return render_template("professionallife.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run()
