import os
from flask import Flask, render_template, request, redirect, url_for, make_response
from sqla_wrapper import SQLAlchemy
from hashlib import sha256
import uuid

db_url = os.getenv("DATABASE_URL", "sqlite:///db.sqlite").replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(db_url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)
    session_token = db.Column(db.String, unique=False)


app = Flask(__name__)


db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    session_cookie = request.cookies.get("session")
    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()
        if user:
            return render_template("index.html", user=user)
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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        email = request.form.get("user-email")
        password = request.form.get("password")

        password_hash = sha256(password.encode("utf-8")).hexdigest()
        existing_user = db.query(User).filter_by(email=email, password=password_hash).first()

        if existing_user:
            session_token = str(uuid.uuid4())
            existing_user.session_token = session_token
            existing_user.save()

            response = make_response(redirect(url_for("home")))
            response.set_cookie("session", session_token)
            return response

        else:
            return "Username or password is not correct"

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(use_reloader=True)