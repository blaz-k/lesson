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
    guess = int(request.form.get("guess"))

    return render_template("result.html")


if __name__ == "__main__":
    app.run(use_reloader=True)