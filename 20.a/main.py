import os
from flask import Flask, render_template, request, redirect, url_for
from sqla_wrapper import SQLAlchemy
from hashlib import sha256
import uuid

db_url = os.getenv("DATABASE_URL", "sqlite:///db.sqlite").replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(db_url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)


app = Flask(__name__)


db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():

    return render_template("index.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")

    elif request.method == "POST":
        #get all the names
        email = request.form.get("user-email")
        password = request.form.get("password")
        repeat = request.form.get("repeat")

        # ce ga se ni mormo nardit novega userja in preverit ce je v bazi

        existing_user = db.query(User).filter_by(email=email).first()

        if existing_user:
            return "This user already exists!"
        else:
        #preveriti moramo ce se passworda ujemata
            if password == repeat:
                password_hash = sha256(password.encode("utf-8")).hexdigest()
                # moramo zakamuflirat password
                new_user = User(email=email, password=password_hash)
                new_user.save()
            else:
                return "Passwords do not match!"

    return redirect(url_for("home"))


        #moramo zakamuflirat password



@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")






if __name__ == '__main__':
    app.run(use_reloader=True)