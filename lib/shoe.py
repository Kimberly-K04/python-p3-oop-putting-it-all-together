#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.clean = True
        self.worn = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value <= 0:
                print("size must be a positive integer")
            else:
                self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        """Repairs the shoe"""
        self.condition = "New"
        print("Your shoe is as good as new!")
