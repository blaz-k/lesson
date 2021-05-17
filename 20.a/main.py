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
    first_name = db.Column(db.String, unique=False)
    last_name = db.Column(db.String, unique=False)
    address = db.Column(db.String, unique=False)
    password = db.Column(db.String, unique=False)
    session_token = db.Column(db.String, unique=False)
    deleted = db.Column(db.Boolean, default=False)


app = Flask(__name__)


db.create_all()


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dashboard/all-users")
def all_users():
    session_cookie = request.cookies.get("session")

    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()

        if user:
            all_users = db.query(User).filter_by(deleted=False).all()

            return render_template("dashboard-all-users.html", all_users=all_users)

    return "You are not logged in!"


@app.route("/dashboard/user/<user_id>")
def dashboard_user_details(user_id):
    session_cookie = request.cookies.get("session")

    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()

        if user:
            selected_user = db.query(User).filter_by(id=int(user_id)).first()
            return render_template("dashboard-user-details.html", selected_user=selected_user)


@app.route("/dashboard/user-delete/<user_id>", methods=["POST"])
def user_delete(user_id):
    session_cookie = request.cookies.get("session")
    print("user_delete: ")

    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()
        print("if session cookie: {}".format(session_cookie))

        if user:
            print("if user: ")
            user_to_delete = db.query(User).filter_by(id=int(user_id)).first()
            print("if user_to_delete: {}".format(user_to_delete))
            user_to_delete.deleted = True
            user_to_delete.save()

            return redirect(url_for("all_users"))

    return "You are not allowed to delete, you are not logged in!!"




@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    session_cookie = request.cookies.get("session")
    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()
        if user:
            return render_template("dashboard.html", user=user)

    return "You are not logged in!!"


@app.route("/dashboard/edit-profile", methods=["GET", "POST"])
def dashboard_edit_profile():
    session_cookie = request.cookies.get("session")

    user = None

    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()

        if not user:
            return "You are not logged-in!!!"

    else:
        return "You are not logged in"

    if request.method == "GET":
        return render_template("dashboard-edit-profile.html", user=user)

    elif request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        address = request.form.get("address")

        user.first_name = first_name
        user.last_name = last_name
        user.address = address
        user.save()

        return redirect(url_for("dashboard"))



@app.route("/", methods=["GET", "POST"])
def home():
    session_cookie = request.cookies.get("session")
    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()
        if user:
            return render_template("index.html", user=user)
    return render_template("index.html")


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


@app.route("/logout", methods=["POST"])
def logout():

    session_cookie = request.cookies.get("session")
    user = db.query(User).filter_by(session_token=session_cookie).first()
    user.session_token = ""
    user.save()

    return render_template("logout.html")



@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")

    elif request.method == "POST":
        #get all the names
        email = request.form.get("user-email")
        password = request.form.get("password")
        repeat = request.form.get("repeat")
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        address = request.form.get("address")

        # ce ga se ni mormo nardit novega userja in preverit ce je v bazi

        existing_user = db.query(User).filter_by(email=email).first()

        if existing_user:
            return "This user already exists!"
        else:
        #preveriti moramo ce se passworda ujemata
            if password == repeat:
                password_hash = sha256(password.encode("utf-8")).hexdigest()
                # moramo zakamuflirat password
                new_user = User(email=email, password=password_hash, first_name=first_name, last_name=last_name, address=address)
                new_user.save()
            else:
                return "Passwords do not match!"

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(use_reloader=True)