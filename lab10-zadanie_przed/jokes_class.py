
class Joke:
    """
    Joke Class. Contains attributes

    :param content: actual joke
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if not content:
            raise ValueError("Content cannot be empty")
        else:
            self.__content = content

    @property
    def content(self) -> str:
        return self.__content

    def __str__(self) -> str:
        return f"{self.__content}"

    def __repr__(self) -> str:
        return f"{self.__content}"

    def save_joke(self):
        try:
            with open("saved_jokes.txt", "a+") as filehandle:
                filehandle.write(f"{self.content}\n")
        except Exception as e:
            return str(e)
