#!/usr/bin/env python3

"""
p = q + r #Point.__add__()
p += q #Point.__iadd__()
p = q - r #Point.__sub__()
p -= q #Point.__isub__()
p = q * r #Point.__mul__()
p *= q #Point.__imul__()
p = q / n #Point.__tuediv__()
p /= n #Point.__itruediv__()
p = q // n #Point.__floordiv__()
p //= n #Point.__ifloordiv__()
n is number
p,q,r is object
"""


import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __floordiv__(self, other):
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        return self


    @property
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return ("{0.__class__.__name__}({0.x!r}, {0.y!r})".format(self))

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin - self.radius)

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        assert radius > 0, "radius must be nonzero and non-negative"
        self.__radius = radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return ("{0.__class__.__name__}({0.radius!r}, {0.x!r}, {0.y!r})".format(self))

if __name__ == '__main__':
    import doctest
    doctest.testmod()