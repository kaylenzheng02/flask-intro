# -*- coding: utf-8 -*-
# %pip install flask requests pandas

import requests

url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
data = response.json()
data

dog_url = data["message"]
dog_url

from IPython.display import Image, display

display(Image(url=dog_url, width=300))

url = "https://dog.ceo/api/breeds/image/random/2"
dogs = requests.get(url).json()["message"]
dogs

for dog in dogs:
    display(Image(url=dog, width=250))

display(Image(dogs[0]))

from pathlib import Path

project = Path("dog-vote-workshop")
(project / "templates").mkdir(parents=True, exist_ok=True)
print("Project folder:", project.resolve())

# %%writefile dog-vote-workshop/dogs.py
# import requests
#
#
# def get_dogs():
#     response = requests.get("https://dog.ceo/api/breeds/image/random/2")
#     return response.json()["message"]

# %%writefile dog-vote-workshop/app.py
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
#     return "<h1>Which dog is cuter?</h1><p>Our first Flask page.</p>"

# %%writefile dog-vote-workshop/templates/index.html
# <!doctype html>
# <html lang="en">
# <head><meta charset="utf-8"><title>Dog vote</title></head>
# <body>
#   <h1>Which dog is cuter?</h1>
#   <img src="{{ dogs[0] }}" alt="Dog A" width="300">
#   <img src="{{ dogs[1] }}" alt="Dog B" width="300">
# </body>
# </html>

# %%writefile dog-vote-workshop/app.py
# from flask import Flask, render_template
# from dogs import get_dogs
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
#     dogs = get_dogs()
#     return render_template("index.html", dogs=dogs)

# %%writefile dog-vote-workshop/templates/index.html
# <!doctype html>
# <html lang="en">
# <head><meta charset="utf-8"><title>Dog vote</title></head>
# <body>
#   <h1>Which dog is cuter?</h1>
#   <p>{{ message }}</p>
#
#   <form method="post">
#     <input type="hidden" name="dog_a" value="{{ dogs[0] }}">
#     <input type="hidden" name="dog_b" value="{{ dogs[1] }}">
#
#     <img src="{{ dogs[0] }}" alt="Dog A" width="300">
#     <button name="winner" value="{{ dogs[0] }}">Vote for Dog A</button>
#
#     <img src="{{ dogs[1] }}" alt="Dog B" width="300">
#     <button name="winner" value="{{ dogs[1] }}">Vote for Dog B</button>
#   </form>
# </body>
# </html>

# %%writefile dog-vote-workshop/app.py
# from flask import Flask, render_template, request
# from dogs import get_dogs
#
# app = Flask(__name__)
#
#
# @app.route("/", methods=["GET", "POST"])
# def index():
#     message = ""
#     if request.method == "POST":
#         dog_a = request.form["dog_a"]
#         dog_b = request.form["dog_b"]
#         winner = request.form["winner"]
#         print("Dog A:", dog_a)
#         print("Dog B:", dog_b)
#         print("Winner:", winner)
#         message = "Vote received! Here are two more dogs."
#
#     dogs = get_dogs()
#     return render_template("index.html", dogs=dogs, message=message)

import pandas as pd

practice_vote = pd.DataFrame([{
    "dog_a": dogs[0],
    "dog_b": dogs[1],
    "winner": dogs[0],
}])
practice_vote

practice_file = project / "practice_votes.csv"
practice_vote.to_csv(practice_file, index=False)
pd.read_csv(practice_file)

# %%writefile dog-vote-workshop/app.py
# from pathlib import Path
#
# import pandas as pd
# from flask import Flask, render_template, request
# from dogs import get_dogs
#
# app = Flask(__name__)
# CSV_FILE = Path(__file__).parent / "votes.csv"
#
#
# @app.route("/", methods=["GET", "POST"])
# def index():
#     message = ""
#
#     if request.method == "POST":
#         vote = pd.DataFrame([{
#             "dog_a": request.form["dog_a"],
#             "dog_b": request.form["dog_b"],
#             "winner": request.form["winner"],
#         }])
#
#         if CSV_FILE.exists():
#             previous_votes = pd.read_csv(CSV_FILE)
#             vote = pd.concat([previous_votes, vote], ignore_index=True)
#
#         vote.to_csv(CSV_FILE, index=False)
#         message = "Vote saved! Here are two more dogs."
#
#     dogs = get_dogs()
#     return render_template("index.html", dogs=dogs, message=message)

votes_file = project / "votes.csv"
if votes_file.exists():
    votes = pd.read_csv(votes_file)
    print("Number of votes:", len(votes))
    display(votes)
else:
    print("Submit a vote in the browser first, then rerun this cell.")
