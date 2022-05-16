import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Bonfire Heart", "James Blunt")
        self.song_2 = Song("Salamander Street", "Callum Beattie")
        self.song_3 = Song("Hold Back The River", "James Bay")

    def test_song_has_title(self):
        self.assertEqual("Bonfire Heart", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("James Blunt", self.song_1.artist)