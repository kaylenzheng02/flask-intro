import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get(
        "https://dog.ceo/api/breeds/image/random/2",
    )
    response.raise_for_status()
    dogs = response.json()["message"]

    return render_template("index.html", dogs=dogs)


if __name__ == '__main__':
    app.run(debug=True)