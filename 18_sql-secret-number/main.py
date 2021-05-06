from flask import Flask, render_template, request, make_response
from models import User, db
from random import randint

app = Flask(__name__)
db.create_all()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    secret = randint(1, 10)
    guess = int(request.form.get("guess"))
    user = request.form.get("username")
    existing_user = User(username=user)

    if not existing_user:
        new_secret = randint(1, 10)
        new_user = User(username=user, secret_number=new_secret)

        db.add(new_user)
        db.commit()

    if guess == secret:
        result = "CORRECT"


    else:
        result = "WRONG"

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(use_reloader=True)