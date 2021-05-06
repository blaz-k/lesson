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
    user = request.form.get("username")
    print(user)
    secret = randint(1, 10)
    print(secret)
    guess = int(request.form.get("guess"))
    print(guess)

    existing_user = db.query(User).filter_by(username=user).first()
    print(existing_user)

    if not existing_user:
        new_user = User(username=user, secret_number=secret)
        print(new_user)
        db.add(new_user)
        db.commit()

    if guess == secret:
        result = "CORRECT"

    else:
        result = "WRONG"

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(use_reloader=True)