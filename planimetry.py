"""The module contains classes of plane figure"""
from math import pi, pow


class Rectangle:
    def __init__(self, a, b):
        """The constructor accepts a length and a width"""
        self.length = a
        self.width = b

    def area(self):
        """Method for area calculation"""
        return round(self.length * self.width, 2)

    def perimeter(self):
        """Method for perimeter calculation"""
        return 2 * (self.length * self.width)


class Circle:
    """Class circle."""
    def __init__(self, radius):
        """Constructor take a radius."""
        self.r = radius

    def square(self):
        """Method for area of circle calculation."""
        return round(pi * pow(self.r, 2), 2)

    def length(self):
        """Method for length of circle calculation"""
        return round(2 * pi * self.r)


