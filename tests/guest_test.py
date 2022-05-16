import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Cameron Wilson", "Bonfire Heart", 300)
        self.guest_2 = Guest("Vince Watson", "Salamander Street", 250)
        self.guest_3 = Guest("Tommy Tate", "Hold Back The River", 350)

    def test_guest_has_name(self):
        self.assertEqual("Cameron Wilson", self.guest_1.name)

    def test_guest_has_fav_song(self):
        self.assertEqual("Bonfire Heart", self.guest_1.fav_song)

    def test_guest_has_wallet(self):
        self.assertEqual(300, self.guest_1.wallet)
