from requests import get
from jokes_class import Joke

headers = {
    "Accept": "application/json"
}

urls = {
    "get_random": "https://icanhazdadjoke.com/"
}


def get_joke():
    joke_response = get(urls["get_random"], headers=headers).json()
    if joke_response["status"] == 200:
        joke = Joke(joke_response["joke"])
        print(joke)
        return joke
