class Crop:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.crops_available = []

    def add_crop(self, crop):
        self.crops_available += crop.name
        print(self.crops_available)