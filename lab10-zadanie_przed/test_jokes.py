from jokes_services import Joke
from jokes_services import get_joke
import pytest
from requests import Response


def test_create_joke_std():
    joke = Joke("123")
    assert joke.content == "123"


def test_create_joke_invalid():
    with pytest.raises(ValueError):
        Joke("")


def test_joke_as_str():
    joke = Joke("123")
    assert str(joke) == "123"


def test_get_joke_std(monkeypatch):
    response = Response()
    response._content = b'{"status": 200, "joke": "123"}'
    monkeypatch.setattr("jokes_services.get", lambda url, headers: response)
    joke = get_joke()
    assert joke.content == "123"


def test_get_joke_not_found(monkeypatch):
    response = Response()
    response._content = b'{"status": 404, "joke": ""}'
    monkeypatch.setattr("jokes_services.get", lambda url, headers: response)
    joke = get_joke()
    assert joke is None


def test_get_joke_server_error(monkeypatch):
    response = Response()
    response._content = b'{"status": 500}'
    monkeypatch.setattr("jokes_services.get", lambda url, headers: response)
    joke = get_joke()
    assert joke is None
