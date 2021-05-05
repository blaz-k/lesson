import os
from flask import Flask, render_template, request, redirect, url_for
from sqla_wrapper import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///db.sqlite"))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    text = db.Column(db.String)


db.create_all()


@app.route("/", methods=["GET"])
def index():

    return render_template("index.html")


@app.route("/add-message", methods=["POST"])
def add_message():
    username = request.form.get("username")
    message_text = request.form.get("message")
    message = Message(author=username, text=message_text)
    db.add(message)
    db.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(use_reloader=True)
