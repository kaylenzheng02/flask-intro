from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request
from dogs import get_dogs

app = Flask(__name__)
CSV_FILE = Path(__file__).parent / "votes.csv"


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        vote = pd.DataFrame([{
            "dog_a": request.form["dog_a"],
            "dog_b": request.form["dog_b"],
            "winner": request.form["winner"],
        }])

        if CSV_FILE.exists():
            previous_votes = pd.read_csv(CSV_FILE)
            vote = pd.concat([previous_votes, vote], ignore_index=True)

        vote.to_csv(CSV_FILE, index=False)
        message = "Vote saved! Here are two more dogs."

    dogs = get_dogs()
    return render_template("index.html", dogs=dogs, message=message)


@app.route("/textform", methods=["GET", "POST"])
def text_form():
    submitted_text = ""
    error = ""

    if request.method == 'POST':
        submitted_text = request.form.get("text", "").strip()
        if not submitted_text:
            error = "Please enter some text."

    return render_template(
        "textform.html",
        submitted_text=submitted_text,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)