from flask import Flask, render_template, request, make_response
from models import User, db
from random import randint

app = Flask(__name__)
db.create_all()


@app.route("/", methods=["GET"])
def index():
    user = db.query(User)
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    secret_number = randint(1, 10)
    print(secret_number)
    guess = int(request.form.get("guess"))
    print(guess)
    user = request.form.get("username")
    print(user)
    existing_user = User(username=user)

    if not existing_user:
        new_user = User(username=user)
        new_secret = randint(1, 10)
        db.commit(new_user, new_secret)
        db.add()
    if guess == secret_number:
        result = "CORRECT"
    else:
        result = "WRONG"

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(use_reloader=True)