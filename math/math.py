from flask import Flask, render_template, request, make_response


app = Flask(__name__)

#f = c * 1.8 +32
lb = 0.45
mile = 0.621371192

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/celsius", methods=["POST"])
def celsius():
    return render_template("celsius.html")


@app.route("/kg", methods=["POST"])
def kg():
    return render_template("kg.html")


@app.route("/meters", methods=["POST"])
def meters():
    return render_template("meters.html")









if __name__ == "__main__":
    app.run(use_reloader=True)
