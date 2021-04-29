from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

country_capitals = {"Greece": "Athens", "Serbia": "Belgrade", "Germany": "Berlin", "Switzerland": "Bern",
"Slovakia": "Bratislava", "Belgium": "Brussels", "Romania": "Bucharest", "Hungary": "Budapest", "Moldova": "Chisinau",
"Denmark": "Copenhagen", "Ireland": "Dublin", "Finland": "Helsinki", "Ukraine": "Kiev", "Portugal": "Lisbon",
"Slovenia": "Ljubljana", "United Kingdom": "London", "Luxembourg": "Luxembourg", "Andorra": "Andorra la Vella",
"Spain": "Madrid", "Belarus": "Minsk", "Monaco": "Monaco", "Russia": "Moscow", "Cyprus": "Nicosia", "Greenland": "Nuuk",
"Norway": "Oslo", "France": "Paris", "Montenegro": "Podgorica", "Czech Republic": "Prague", "Iceland": "Reykjavik",
"Latvia": "Riga", "Italy": "Rome", "San Marino": "San Marino", "Bosnia": "Sarajevo", "North Macedonia": "Skopje",
"Bulgaria": "Sofia", "Sweden": "Stockholm", "Estonia": "Tallinn", "Albania": "Tirana", "Liechtenstein": "Vaduz",
 "Malta": "Valletta", "Vatican": "Vatican city", "Austria": "Vienna", "Poland": "Warsaw", "Croatia": "Zagreb",
 "Netherlands": "Amsterdam", "Lithuania": "Vilnius", "Armenia": "Yerevan", "Turkey": "Ankara", "Azerbaijan": "Baku",
 "Georgia": "Tbilisi"}

country = random.choice(list(country_capitals.keys()))


@app.route("/", methods=["GET"])
def index():
    guess = random.choice(list(country_capitals.keys()))
    response = make_response(render_template("index.html", country=guess))

    return response


@app.route("/result", methods=["POST"])
def result():
    guess = request.form.get("guess")
    response = make_response(render_template("result.html"))

    if guess == country_capitals.get(country):
        result = "correct"
        response = make_response(render_template("result.html", country=response))

    elif guess != country_capitals.get(country):
        result = "Not good"

    response = make_response(render_template("result.html", result=result))
    return response


if __name__ == "__main__":
    app.run(port=7070, use_reloader=True)