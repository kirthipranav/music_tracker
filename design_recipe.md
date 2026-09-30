## 1 Problem

'''
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
'''

## 2 Designing class interface

'''
class music_tracker

    def __init__(self):
        pass


    Parameters: track, str
    Returns: None
    Side effects: None

    def add_track(self, track):
        pass


    Parameters: None
    Returns: tracks, list
    Side effects: None

    def list_tracks(self):
        pass
'''

## 3 Examples of tests

'''
example = music_tracker()

1. Testing if list_tracks will return an empty list if there are no tracks added.

example.list_tracks() => []

2. Testing if a track can be added successfully.

example.add_track("Stayin Alive")
example.list_tracks() => ["Stayin Alive"]

3. Testing if multiple tracks can be added successfully.

example.add_track("Congratulations")
example.list_tracks() => ["Stayin Alive", "Congratulations"]
'''