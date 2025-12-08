class Address:
    def __init__(self, postal_code, street, house_number):
        self.postal_code = postal_code
        self.street = street
        self.house_number = house_number

    def __repr__(self):
        return f"Address(city={self.city}, region={self.region}, postal_code={self.postal_code}, street_address={self.street}, house_number={self.house_number})"
