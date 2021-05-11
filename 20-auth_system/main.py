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


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

        #ce je email isti kot ga najde v bazi potem je uredu cene pa se mora registrirati
    elif request.method == "POST":
        email = request.form.get("user-email").lower()
        password = request.form.get("password")

        password_hash = sha256(password.encode("utf-8")).hexdigest()
        existing_user = db.query(User).filter_by(email=email, password=password_hash)

        if existing_user:
            session_token = str(uuid.uuid4())
            existing_user.session_token = session_token
            existing_user.save()

            response = make_response(redirect(url_for("home")))
            response.set_cookie("session", session_token)
            # ce je password_hash pravilen potem ok ce ni potem je password ali email napacen
            return render_template("chat.html")
        else:
            return "Password or username not correct!"


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")

    elif request.method == "POST":
        email = request.form.get("user-email")
        password = request.form.get("password")
        repeat = request.form.get("repeat")

        existing_user = db.query(User).filter_by(email=email).first()
        # ce user ze obstaja napisi da ze obstaja
        if existing_user:
            return "ERROR: This email already exists!"
        else:
            #ce user se ne obstaja, potem preglej ce se ujema password
            if password == repeat:
                password_hash = sha256(password.encode("utf-8")).hexdigest()
                new_user = User(email=email, password=password_hash)
                new_user.save()
            else:
                return "ERROR: Passwords do not match!"
    return redirect(url_for("home"))


@app.route("/chat", methods=["GET", "POST"])
def chat():
    return render_template("chat.html")


if __name__ == "__main__":
    app.run(use_reloader=True)
