from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")
# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)

DB_URL = "postgres+psycopg2://empenvsomaaxca:1be38b183f984b63d363707b8c9cc55734d339e5eaf3e7157f153a7531a08e2d@ec2-54-243-59-122.compute-1.amazonaws.com:5432/d5r632cf3ld71m"

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning

db = SQLAlchemy(app)


class Jobs(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    jobstart = db.Column(db.Date())
    jobend = db.Column(db.Date())
    jobdescription = db.Column(db.String(500))

    def __init__(self, title, jobstart, jobend, jobdescription):
        self.title = title
        self.jobstart = jobstart
        self.jobend = jobend
        self.jobdescription = jobdescription

    def __repr__(self):
        return self


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
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)),debug=True)
