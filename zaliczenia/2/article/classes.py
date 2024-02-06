from datetime import datetime


GENRES = {
    "SCI-FI": [
        "sci-fi1", "sci-fi2", "sci-fi3"
    ],
    "BIOGRAPHY": [
        "bio1", "bio2", "bio3"
    ],
    "FANTASY": [
        "fantasy1", "fantasy2", "fantasy3"
    ]
}


class Author():
    """
    Author class. Contains attributes:

    :param fname: author's first name
    :type fname: str

    :param lname: author's last name
    :type lname: str

    :param background: author's brief background
    :type background: str
    """

    def __init__(self, fname: str, lname: str, background: str = "") -> None:
        if not fname:
            raise ValueError("Name cannot be empty")
        else:
            self.__fname = fname
        if not lname:
            raise ValueError("Name cannot be empty")
        else:
            self.__lname = lname
        self.__background = background

    @property
    def fname(self) -> str:
        return self.__fname

    @property
    def lname(self) -> str:
        return self.__lname

    @property
    def background(self) -> str:
        return self.__background

    def __lt__(self, author_to_compare) -> bool:
        """
        Compares authors in terms of their last name,
        so that they could be presented in an alphabetical order
        """
        return self.__lname < author_to_compare.lname

    def __str__(self) -> str:
        """
        Returns a string containing author's first & last name
        """
        return f"{self.__fname} {self.__lname}"


class Article():
    """
    Article class. Contains attributes:

    :param title: article's title
    :type title: str

    :param content: article's main content
    :type content: str

    :param genre: article's genre, defined using a global dictionary
    :type genre: str

    :param authors: article's authors
    :type authors: list[Author]

    :param date: article's publication date
    :type date: datetime
    """

    def __init__(self, title: str, content: str, genres: dict[str], authors: list[Author],  date: datetime) -> None:
        if not title:
            raise ValueError("Title cannot be empty")
        else:
            self.__title = str.title(title)
        if not content:
            raise ValueError("Content cannot be empty")
        else:
            self.__content = content
        if not authors:
            raise ValueError("There cannot be no authors")
        else:
            self.__authors = sorted(authors)
        if not isinstance(date, datetime):
            raise TypeError("Incorrect date type entered")
        else:
            self.__date = date
        self.__genre = "unrecognized genre"
        for genre, titles in genres.items():
            if title in titles:
                self.__genre = genre
                break

    @property
    def title(self) -> str:
        return self.__title

    @property
    def content(self) -> str:
        return self.__content

    @property
    def genre(self) -> str:
        return self.__genre

    @property
    def authors(self) -> str:
        return self.__authors

    @property
    def date(self) -> datetime:
        return self.__date

    def print_title(self) -> str:
        """
        Returns article's title wrapped in a <title> tag
        """
        return f"<title>{self.__title}</title>\n"

    def print_content(self) -> str:
        """
        Returns article's content wrapped in a <div> tag
        """
        return f"<div>{self.__content}</div>\n"

    def print_authors(self) -> str:
        """
        Returns article's authors wrapped in a <ul> tag
        """
        authors_str = ""
        for author in self.__authors:
            authors_str += f" {str(author)} "
        return f"<ul>{authors_str}</ul>\n"

    def print_date(self) -> str:
        """
        Returns article's publication date wrapped in a <p> tag
        """
        return f"<p>{self.__date}</p>\n"

    def print(self) -> str:
        """"
        Returns article's HTML representation
        """
        main_tag = f"<HTML>\n\t{self.print_title()}\t{self.print_content()}\t{self.print_authors()}\t{self.print_date()}</HTML>"
        return main_tag

    def set_date(self, new_date: datetime) -> None:
        """
        Allows to edit the publication date of an article.
        Raises ValueError if the new date is before the initial one
        """
        if self.__date > new_date:
            raise ValueError(
                "New publication date cannot be before the inital one")
        elif not isinstance(new_date, datetime):
            raise TypeError("Incorrect date type entered")
        else:
            self.__date = new_date

    def set_content(self, new_content: str) -> None:
        if not new_content:
            raise ValueError("Content cannot be empty")
        else:
            self.__content = new_content

    def __str__(self) -> str:
        return f"Article - {self.__title}"

    def __lt__(self, article_to_compare) -> bool:
        return self.__date < article_to_compare.date


def main():
    author1 = Author("John", "Moore", "Lorem Ipsum ...")
    author2 = Author("Bob", "Adams", "Lorem Ipsum ...")
    article1 = Article("sci-fi1", "content", GENRES,
                       [author1, author2], datetime(2023, 4, 12))
    article2 = Article("bio1", "content", GENRES,
                       [author1], datetime(2022, 5, 12))
    article1.set_content("sample edited content")
    article1.set_date(datetime(2023, 5, 12, 23, 00))
    print(article1.print())
    print(article1 > article2)


if __name__ == "__main__":
    main()
