from flask import Flask, render_template, request
from models import User, db
from random import randint

app = Flask(__name__)
db.create_all()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    username = request.form.get("username")# tuki zaprosim za ime od userja
    secret = randint(1, 10) #tuki dolocimo random secret
    guess = int(request.form.get("guess"))

    user = db.query(User).filter_by(username=username).first()

    if not user: #ce ne obstaja:
        user = User(username=username, secret_number=secret)

        db.add(user)
        db.commit()

    if guess == user.secret_number:
        result = "CORRECT"
        user.secret_number = randint(1, 10)
        user.save()

    else:
        result = "WRONG"

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(use_reloader=True)