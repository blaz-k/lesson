from flask import Flask, render_template, request, make_response
from random import randint

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    secret = randint(1, 30)
    guess = int(request.form.get("guess"))

    if guess == secret:
        result = "Correct"

        response = make_response(render_template("result.html", result=result))
        return response
    else:
        result = "not correct"

        response = make_response(render_template("result.html", result=result))
        return response


if __name__ == "__main__":
    app.run(use_reloader=True)
