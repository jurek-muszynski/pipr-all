from datetime import datetime
from classes import Author, Article, GENRES
import pytest


def test_create_author_standard():
    author = Author("John", "Adams", "youngest american novelist")
    assert author.fname == "John"
    assert author.lname == "Adams"
    assert author.background == "youngest american novelist"


def test_create_author_invalid():
    with pytest.raises(ValueError):
        Author("John", "", "sample")

    with pytest.raises(ValueError):
        Author("", "Wayne", "sample")


def test_author_as_str_standard():
    author = Author("John", "Adams", "youngest american novelist")
    assert str(author) == "John Adams"


def test_author_compare_standard():
    author1 = Author("John", "Adams", "youngest american novelist")
    author2 = Author("Bob", "House", "bio...")
    assert author1 < author2


def test_create_article_standard():
    author = Author("John", "Adams", "youngest american novelist")
    article = Article("fantasy1", "content", GENRES,
                      [author], datetime(2023, 12, 5))
    assert article.authors == [author]
    assert article.title == "Fantasy1"
    assert article.content == "content"
    assert article.genre == "FANTASY"
    assert article.date == datetime(2023, 12, 5)


def test_create_article_invalid():
    author = Author("John", "Adams", "youngest american novelist")
    article = Article("fantasy1", "content", GENRES,
                      [author], datetime(2023, 12, 5))
    with pytest.raises(ValueError):
        Article("", "content", GENRES,
                [author], datetime(2023, 12, 5))
    with pytest.raises(ValueError):
        Article("fantasy1", "", GENRES,
                [author], datetime(2023, 12, 5))
    with pytest.raises(ValueError):
        Article("fantasy1", "content", GENRES,
                [], datetime(2023, 12, 5))
    with pytest.raises(TypeError):
        Article("fantasy1", "content", GENRES,
                [author], "2022")


def test_create_article_no_genre():
    author = Author("John", "Adams", "youngest american novelist")
    article = Article("article1", "content", GENRES,
                      [author], datetime(2023, 12, 5))
    assert article.title == "Article1"
    assert article.authors == [author]
    assert article.date == datetime(2023, 12, 5)
    assert article.content == "content"
    assert article.genre == "unrecognized genre"


def test_article_print_html():
    author = Author("John", "Adams", "youngest american novelist")
    article = Article("sci-fi1", "content", GENRES,
                      [author], datetime(2023, 12, 5))
    assert article.print_title() == "<title>Sci-Fi1</title>\n"
    assert article.print_content() == "<div>content</div>\n"
    assert article.print_date() == "<p>2023-12-05 00:00:00</p>\n"
    assert article.print_authors() == "<ul> John Adams </ul>\n"


def test_article_set_date_standard():
    author = Author("John", "Adams", "youngest american novelist")
    article = Article("bio1", "content", GENRES,
                      [author], datetime(2023, 12, 5))
    new_date = datetime(2023, 12, 7)
    assert article.date == datetime(2023, 12, 5)
    article.set_date(new_date)
    assert article.date == datetime(2023, 12, 7)


def test_article_set_date_invalid():
    author = Author("John", "Adams", "youngest american novelist")
    article = Article("bio1", "content", GENRES,
                      [author], datetime(2023, 12, 5))
    new_date = datetime(2022, 12, 7)
    assert article.date == datetime(2023, 12, 5)
    with pytest.raises(ValueError):
        article.set_date(new_date)
    with pytest.raises(TypeError):
        article.set_date("2022")


def test_article_str_standard():
    author = Author("John", "Adams", "youngest american novelist")
    article = Article("bio1", "content", GENRES,
                      [author], datetime(2023, 12, 5))
    assert str(article) == "Article - Bio1"


def test_article_compare_standard():
    author = Author("John", "Adams", "youngest american novelist")
    article1 = Article("bio1", "content", GENRES,
                       [author], datetime(2023, 12, 5))
    article2 = Article("sci-fi1", "content", GENRES,
                       [author], datetime(2022, 12, 5))
    assert article1 > article2
