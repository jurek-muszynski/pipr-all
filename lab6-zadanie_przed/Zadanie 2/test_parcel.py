from Parcel import Parcel
import pytest


def test_parcel_standard():
    parcel = Parcel("x", "y", 1, 1, 1, 1)
    assert parcel.get_sender() == "x"


def test_parcel_invalid():
    with pytest.raises(TypeError):
        Parcel()


def test_parcel_get_description():
    parcel = Parcel("x", "y", 1, 1, 1, 1)
    assert parcel.info() == "Parcel 1.0 x 1.0 sent by x to y"


def test_parcel_get_description_string():
    parcel = Parcel("x", "y", 1, 1, 1, 1)
    assert str(parcel) == parcel.info()


def test_parcel_set_sender_standard():
    parcel = Parcel("x", "y", 1, 1, 1, 1)
    assert parcel.get_sender() == "x"
    parcel.set_sender("sender")
    assert parcel.get_sender() == "sender"


def test_parcel_set_sender_no_name():
    parcel = Parcel("x", "y", 1, 1, 1, 1)
    assert parcel.get_sender() == "x"
    with pytest.raises(ValueError):
        parcel.set_sender("")


def test_parcel_set_receiver_standard():
    parcel = Parcel("x", "y", 1, 1, 1, 1)
    assert parcel.get_receiver() == "y"
    parcel.set_sender("receiver")
    assert parcel.get_sender() == "receiver"


def test_parcel_set_receiver_no_name():
    parcel = Parcel("x", "y", 1, 1, 1, 1)
    assert parcel.get_receiver() == "y"
    with pytest.raises(ValueError):
        parcel.set_receiver("")


def test_parcel_set_size_standard():
    parcel = Parcel("x", "y", 1, 2, 3, 4)
    assert parcel.get_width() == 1
    assert parcel.get_height() == 2
    assert parcel.get_length() == 3
    assert parcel.get_weight() == 4
    parcel.set_width(4)
    parcel.set_height(3)
    parcel.set_length(2)
    parcel.set_weight(1)
    assert parcel.get_width() == 4
    assert parcel.get_height() == 3
    assert parcel.get_length() == 2
    assert parcel.get_weight() == 1


def test_parcel_set_size_negative():
    parcel = Parcel("x", "y", 1, 2, 3, 4)
    assert parcel.get_width() == 1
    assert parcel.get_height() == 2
    assert parcel.get_length() == 3
    assert parcel.get_weight() == 4
    with pytest.raises(ValueError):
        parcel.set_width(-1)
    with pytest.raises(ValueError):
        parcel.set_height(-3)
    with pytest.raises(ValueError):
        parcel.set_length(-2)
    with pytest.raises(ValueError):
        parcel.set_weight(-1)


def test_parcel_smallest_side():
    parcel = Parcel("x", "y", 1, 2, 3, 4)
    assert parcel.smallest_side() == 1


def test_parcel_biggest_side():
    parcel = Parcel("x", "y", 1, 2, 3, 4)
    assert parcel.biggest_side() == 3
