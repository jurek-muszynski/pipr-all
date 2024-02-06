class Parcel:
    """
    Parcel class. Contains attributes:

    :param sender: sender's name
    :type sender: string

    :param receiver: receiver's name
    :type receiver: string

    :param width: parcel's width
    :type width: float

    :param height: parcel's height
    :type height: float

    :param length: parcel's length
    :type length: float

    :param weight: parcel's weight
    :type weight: float
    """

    def __init__(self, sender: str, receiver: str, width: float, height: float, length: float, weight: float) -> None:
        self._sender = sender
        self._receiver = receiver
        self._width = float(width)
        self._height = float(height)
        self._length = float(length)
        self._weight = float(weight)

    def get_sender(self) -> str:
        return self._sender

    def get_receiver(self) -> str:
        return self._receiver

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height

    def get_length(self) -> float:
        return self._length

    def get_weight(self) -> float:
        return self._weight

    def set_sender(self, sender: str) -> None:
        if not sender:
            raise ValueError("Sender's name cannot be empty")
        else:
            self._sender = sender

    def set_receiver(self, receiver: str) -> None:
        if not receiver:
            raise ValueError("Receiver's name cannot be empty")
        else:
            self._receiver = receiver

    def set_width(self, width: float) -> None:
        if width < 0:
            raise ValueError("Width cannot be negative")
        else:
            self._width = float(width)

    def set_height(self, height: float) -> None:
        if height < 0:
            raise ValueError("Height cannot be negative")
        else:
            self._height = float(height)

    def set_length(self, length: float) -> None:
        if length < 0:
            raise ValueError("Length cannot be negative")
        else:
            self._length = float(length)

    def set_weight(self, weight: float) -> None:
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        else:
            self._weight = float(weight)

    def smallest_side(self) -> float:
        return min(self._width, self._height, self._length)

    def biggest_side(self) -> float:
        return max(self._width, self._height, self._length)

    def info(self) -> str:
        """
        Returns some basic info about a parcel
        (sender, receiver, size)
        """
        sender = f"sent by {self._sender}"
        receiver = f"to {self._receiver}"
        size = f"{self.smallest_side()} x {self.biggest_side()}"
        return f"Parcel {size} {sender} {receiver}"

    def __str__(self) -> str:
        return self.info()
