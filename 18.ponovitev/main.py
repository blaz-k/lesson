from flask import Flask, render_template, request
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy("sqlite:///localhost.sqlite")

app = Flask(__name__)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)


db.create_all()


@app.route("/", methods=["GET"])
def index():
    user = db.query(User).first()
    return render_template("index.html", user=user)


@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("username")
    email = request.form.get("email")
    user_obj = User(username=name, email=email)
    db.add(user_obj)
    db.commit()

    return render_template("result.html", username=name, email=email)


if __name__ == "__main__":
    app.run(use_reloader=True)