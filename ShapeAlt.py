#!/usr/bin/env python3


import math

class Point:

    def __init__(self, x=0, y=0):
        '''A 2D cartestion coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        '''
        self.x = x
        self.y = y
        
    @property
    def distance_from_origin(self):
        '''The distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin
        5.0
        '''
        return math.hypot(self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return ("{0.__class__.__name__}({0.x!r}, {0.y!r})".format(self))

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

class Circle(Point):

    def __init__(slef, radius, x=0, y=0):
        '''A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        '''
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        '''The circle's area

        >>> circle = Circle(3)
        >>> a = circle.area
        >>> int(a)
        28
        '''
        return math.pi * (self.radius ** 2)

    @property
    def edge_distance_from_origin(slef):
        '''The distance of the circle's edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin
        3.0
        '''
        return abs(self.distance_from_origin - self.radius)


    @property
    def circumference(self):
        '''The circle's circumference

        >>> circle = Circle(3)
        >>> d = circle.circumference
        >>> int(d)
        18
        '''
        return 2 * math.pi * self.radius

    @property
    def radius(self):
        '''The circle's radius

        >>> circle = Circle(-2)
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle = Circle(4)
        >>> circle.radius = -1
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        '''
        return self.__radius

    @property
    def radius(self, radius):
        assert radius > 0, "radius must be nonzero and non-negative"
        self.__radius = radius
        
    def __eq__(slef, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return ("{0.__class__.__name__}({0.radius!r}, {0.x!r}, "
                "{0.y!r})".format(self))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

