from flask import Flask, render_template, request, make_response
from random import randint

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    existing_secret = request.cookies.get("secret")
    response = make_response(render_template("index.html"))

    if not existing_secret:
        secret = randint(1, 10)
        response.set_cookie("secret", str(secret))

    return response


@app.route("/result", methods=["POST"])
def result():

    guess = int(request.form.get("guess"))
    secret = int(request.cookies.get("secret"))
    if guess == secret:
        result = "Correct"

        response = make_response(render_template("result.html", result=result))

        secret = randint(1, 30)
        response.set_cookie("secret", str(secret))
        return response

    elif guess < secret:
        result = "too SMALL"
    elif guess > secret:
        result = "too BIG"

    response = make_response(render_template("result.html", result=result))

    return response


if __name__ == "__main__":
    app.run(use_reloader=True)
