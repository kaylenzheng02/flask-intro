from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


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