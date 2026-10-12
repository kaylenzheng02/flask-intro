import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        dog_a = request.form["dog_a"]
        dog_b = request.form["dog_b"]
        winner = request.form["winner"]
        if winner not in (dog_a, dog_b):
            return "Invalid vote", 400
        message = "vote recevied ! Here are two more ducks"

    response = requests.get(
        "https://dog.ceo/api/breeds/image/random/2",
    )
    response.raise_for_status()
    dogs = response.json()["message"]

    return render_template("index.html", dogs=dogs, message=message)


if __name__ == '__main__':
    app.run(debug=True)