from flask import Flask, render_template
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy("sqlite:///localhost.sqlite")

app = Flask(__name__)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)





@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()