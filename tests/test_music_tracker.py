from lib.music_tracker import *

def test_pytest():
    assert True

def test_empty_list():
    example = music_tracker()
    assert example.list_tracks() == []

def test_add_one_track():
    example = music_tracker()
    example.add_track("Stayin Alive")
    assert example.list_tracks() == ["Stayin Alive"]

def test_add_multiple_tracks():
    example = music_tracker()
    example.add_track("Stayin Alive")
    example.add_track("Congratulations")
    assert example.list_tracks() == ["Stayin Alive", "Congratulations"]