import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1, 0, 200, 0)
        self.room_2 = Room(2, 0, 100, 0)
        self.room_3 = Room(3, 0, 150, 0)
    
    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.number)

    def test_room_has_capacity(self):
        self.assertEqual(0, self.room_1.capacity)

    def test_room_has_price(self):
        self.assertEqual(200, self.room_1.price)

    def test_room_has_till(self):
        self.assertEqual(0, self.room_1.till)

    def test_room_starts_with_no_guests(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_can_add_guest_to_room(self):
        guest = Guest("Cameron Wilson", "Bonfire Heart", 300)
        self.room_1.add_guest_to_room(guest)
        self.assertEqual(1, self.room_1.guest_count())

    def test_can_remove_guest_from_room(self):
        guest = Guest("Cameron Wilson", "Bonfire Heart", 300)
        self.room_1.add_guest_to_room(guest)
        self.room_1.remove_guest_from_room(guest)
        self.assertEqual(0, self.room_1.guest_count())
