class Room:
    def __init__(self, number, capacity, price, till):
        self.number = number
        self.capacity = 0
        self.price = price
        self.till = till
        self.guest = []
        self.songs = []

    def guest_count(self):
        return len(self.guest)

    def add_guest_to_room(self, guest):
        self.guest.append(self.guest)

    def remove_guest_from_room(self, guest):
        self.guest.remove(self.guest)


        

