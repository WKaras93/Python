from points import Point
from math import pi, sqrt

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):             # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):                 # pole powierzchni
        return pi * pow(self.radius, 2)

    def move(self, x, y):           # przesuniecie o (x, y)
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):         # okrąg pokrywający oba
        if(self.pt.x - self.radius <= other.pt.x - other.radius and self.pt.x + self.radius >= other.pt.x + other.radius and self.pt.y - self.radius <= other.pt.y - other.radius and self.pt.y + self.radius >= other.pt.y + other.radius):
            return self
        elif(self.pt.x - self.radius >= other.pt.x - other.radius and self.pt.x + self.radius <= other.pt.x + other.radius and self.pt.y - self.radius >= other.pt.y - other.radius and self.pt.y + self.radius <= other.pt.y + other.radius):
            return other
        else:
            l = sqrt(pow(self.pt.x - other.pt.x, 2) + pow(self.pt.y - other.pt.y, 2))
            return Circle((self.pt.x + other.pt.x)/2, (self.pt.y + other.pt.y)/2, l/2 + max([self.radius, other.radius]))

# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(10, 10, 3)
        self.c2 = Circle(1, 1, 3)
        self.c3 = Circle(-3.2, -3.3, 12.5)
        self.c4 = Circle(10, 10, 11)

    def test_print(self):
        self.assertEqual(repr(self.c1), "Circle(10, 10, 3)")

    def test_equal(self):
        self.assertTrue(self.c1.radius == self.c2.radius)
    
    def test_notEqual(self):
        self.assertTrue(self.c1 != self.c2)
        self.assertTrue(self.c1.pt.x != self.c2.pt.x)
    
    def test_area(self):
        self.assertAlmostEqual(self.c1.area(), 28.2743339)
        self.assertAlmostEqual(self.c3.area(), 490.8738521)

    def test_move(self):
        self.assertEqual(self.c2.move(9, 9).pt.x, self.c1.pt.x)
        self.assertTrue(self.c2.move(9, 9).radius != self.c4.radius)

    def test_cover(self):
        self.assertEqual(self.c1.cover(self.c4), self.c4)

if __name__ == "__main__":
    unittest.main()