class Artist:
    """
    Artist class. Contains attributes:

    :param name: Artist's name
    :type name: string

    :param date_of_birth: Artist's date of birth
    :type date_of_birth: string

    """

    def __init__(self, name: str, date_of_birth: str = "") -> None:
        if not name:
            raise ValueError("Artist's name cannot be empty")
        else:
            self._name = name
        self._date_of_birth = date_of_birth

    def get_name(self) -> str:
        return self._name

    def get_date_of_birth(self) -> str:
        return self._date_of_birth

    def set_name(self, name: str) -> None:
        if not name:
            raise ValueError("Artist's name cannot be empty")
        else:
            self._name = name

    def set_date_of_birth(self, date_of_birth: str) -> None:
        if not date_of_birth:
            raise ValueError("Artist's date of birth cannot be empty")
        else:
            self._date_of_birth = date_of_birth

    def info(self) -> str:
        """
        Returns some basic info about an artist
        (name, date of birth)
        """
        name = f"The artist - {self._name}"
        date_of_birth = f"born {self._date_of_birth}"
        return f"{name} {date_of_birth}"

    def __str__(self) -> str:
        return self.info()


class Song:
    """
    Song class. Contains attributes:

    :param performer: creator of the song
    :type performer: Artist

    :param title: title of the song
    :type title: string

    :param duration: duration of the song in minutes
    :type duration: float
    """

    def __init__(self, performer: Artist, title: str, duration: float) -> None:
        self._performer = performer
        self._title = title
        self._duration = float(duration)

    def get_performer(self) -> Artist:
        return self._performer

    def get_title(self) -> str:
        return self._title

    def get_duration(self) -> float:
        return self._duration

    def set_performer(self, performer: Artist) -> None:
        if not performer:
            raise ValueError("Performer cannot be null")
        else:
            self._performer = performer

    def set_title(self, title: str) -> None:
        if not title:
            raise ValueError("Title cannot be empty")
        else:
            self._title = title

    def set_duration(self, duration: float) -> None:
        duration = float(duration)
        if not duration:
            raise ValueError("Duration cannot be null")
        if duration < 0:
            raise ValueError("Duration cannot be negative")
        else:
            self._duration = duration

    def info(self) -> str:
        """
        Returns some basic info about a song
        (performer, title, duration)
        """
        performer = f"performed by {self._performer}"
        title = f"titled {self._title}"
        duration = f"lasting {self._duration} minutes"
        return f"The song {title} {performer} {duration}"

    def __str__(self) -> str:
        return self.info()
