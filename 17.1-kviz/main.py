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


@app.route("/", methods=["GET"])
def index():
    country = random.choice(list(country_capitals.keys()))
    existing_country = request.cookies.get("country")
    response = make_response(render_template("index.html"))

    if not existing_country:
        country = random.choice(list(country_capitals.keys()))
        response.set_cookie("country", country)

    return response


@app.route("/result", methods=["POST"])
def result():
    country = request.cookies.get("country")
    guess = request.form.get("guess")
    response = make_response(render_template("result.html"))

    if guess == country:
        print("if stavek: ")
        result = "correct"

        country = random.choice(list(country_capitals.keys()))
        response.set_cookie("country", country)

        return response
    elif guess != country:
        print("elif")
        result = "not good"

    response = make_response(render_template("result.html", result=result))
    return response


if __name__ == "__main__":
    app.run(port=7070, use_reloader=True)