from flask import Flask, render_template, request
from dogs import get_dogs

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        dog_a = request.form["dog_a"]
        dog_b = request.form["dog_b"]
        winner = request.form["winner"]
        print("Dog A:", dog_a)
        print("Dog B:", dog_b)
        print("Winner:", winner)
        message = "u voted! Here are two more dogs."

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