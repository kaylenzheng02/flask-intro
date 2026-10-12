import requests


def get_dogs():
    response = requests.get("https://dog.ceo/api/breeds/image/random/2")
    return response.json()["message"]
