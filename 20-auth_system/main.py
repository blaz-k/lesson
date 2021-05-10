import os
from flask import Flask, render_template, request, redirect, url_for
from sqla_wrapper import SQLAlchemy

db_url = os.getenv("DATABASE_URL", "sqlite:///db.sqlite").replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(db_url)


class User(db.Model):
    email = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String, unique=False)
    repeat = db.Column(db.String, unique=False)


app = Flask(__name__)


db.create_all()


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


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
                new_user = User(email=email, password=password)
                new_user.save()
            else:
                return "ERROR: Passwords do not match!"
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(use_reloader=True)