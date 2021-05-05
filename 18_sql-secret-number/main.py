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
    secret_number = randint(1, 10)
    guess = int(request.form.get("guess"))

    if guess == secret_number:
        result = "Correct"
    elif guess < secret_number:
        result = "It is bigger"
    elif guess > secret_number:
        result = "It is smaller"

    return result


if __name__ == "__main__":
    app.run(use_reloader=True)