from Classes import Artist, Song
import pytest


def test_create_artist_standard():
    artist = Artist("xyz", "11.11.2011")
    assert artist.get_name() == "xyz"
    assert artist.get_date_of_birth() == "11.11.2011"


def test_create_artist_no_date_of_birth():
    artist = Artist("xyz")
    assert artist.get_name() == "xyz"
    assert artist.get_date_of_birth() == ""


def test_create_artist_no_name():
    with pytest.raises(TypeError):
        Artist()


def test_artist_set_name_standard():
    artist = Artist("xyz")
    assert artist.get_name() == "xyz"
    artist.set_name("zyx")
    assert artist.get_name() == "zyx"


def test_artist_set_name_invalid():
    artist = Artist("xyz")
    with pytest.raises(ValueError):
        artist.set_name("")


def test_artist_set_date_of_birth_standard():
    artist = Artist("xyz")
    assert artist.get_date_of_birth() == ""
    artist.set_date_of_birth("11.11.2011")
    assert artist.get_date_of_birth() == "11.11.2011"


def test_artist_set_date_of_birth_invalid():
    artist = Artist("xyz")
    assert artist.get_date_of_birth() == ""
    with pytest.raises(ValueError):
        artist.set_date_of_birth("")


def test_arist_get_description():
    artist = Artist("xyz", "11.11.2011")
    assert artist.info() == "The artist - xyz born 11.11.2011"


def test_artist_get_description_as_string():
    artist = Artist("xyz", "11.11.2011")
    assert artist.info() == str(artist)


def test_create_song_standard():
    artist = Artist("xyz")
    song = Song(artist, "song", 5.25)
    assert song.get_performer() == artist
    assert song.get_title() == "song"
    assert song.get_duration() == 5.25


def test_create_song_invalid():
    with pytest.raises(TypeError):
        Song(1, 1)


def test_song_set_performer():
    artist = Artist("xyz")
    artist_to_change = Artist("zyx")
    song = Song(artist, "song", 5.25)
    assert song.get_performer() == artist
    song.set_performer(artist_to_change)
    assert song.get_performer() == artist_to_change


def test_song_set_performer_invalid():
    artist = Artist("xyz")
    song = Song(artist, "song", 5.25)
    assert song.get_performer() == artist
    with pytest.raises(ValueError):
        song.set_performer("")


def test_song_set_title_standard():
    song = Song(Artist("xyz", "11.11.2011"), "song", 5.25)
    assert song.get_title() == "song"
    song.set_title("song song")
    song.get_title() == "song song"


def test_song_set_title_invalid():
    song = Song(Artist("xyz", "11.11.2011"), "song", 5.25)
    assert song.get_title() == "song"
    with pytest.raises(ValueError):
        song.set_title("")


def test_song_set_duration_standard():
    song = Song(Artist("xyz", "11.11.2011"), "song", 5.25)
    assert song.get_duration() == 5.25
    song.set_duration(1.25)
    assert song.get_duration() == 1.25


def test_song_set_duration_invalid():
    song = Song(Artist("xyz", "11.11.2011"), "song", 5.25)
    assert song.get_duration() == 5.25
    with pytest.raises(ValueError):
        song.set_duration("")
    with pytest.raises(ValueError):
        song.set_duration(-1)


def test_song_get_description():
    song = Song(Artist("xyz", "11.11.2011"), "song", 5.25)
    assert song.info() == "The song titled song performed by The artist - xyz born 11.11.2011 lasting 5.25 minutes"


def test_song_get_description_as_string():
    song = Song(Artist("xyz", "11.11.2011"), "song", 5.25)
    assert song.info() == str(song)
