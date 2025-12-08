class Parking:
    def __init__(self, capacity, position, address):
        self.capacity = capacity
        self.position = position
        self.address = address

    def to_dict(self):
        return {
            "capacity": self.capacity,
            "position": self.position,
            "address": self.address.__dict__
        }

    def __repr__(self):
        return f"Parking(capacity={self.capacity}, position={self.position}, address={repr(self.address)})"
