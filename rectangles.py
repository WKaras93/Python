from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if(isinstance(x1, str) or isinstance(y1, str) or isinstance(x2, str) or isinstance(y2, str)):
            raise TypeError("Wrong type of arguments")
        if(x1 > x2 or y1 > y2):
            raise ValueError("Wrong order of arguments")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return "[({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):        # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

    def area(self):                 # pole powierzchni
        return ((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):           # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(0, 0, 10, 10)
        self.r2 = Rectangle(1.0, 2.0, 10, 11.5)
        self.r3 = Rectangle(0, 0, 10, 10)
    
    def test_print(self):
        self.assertEqual(str(self.r1), "[(0, 0), (10, 10)]")
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 10, 10)")
    
    def test_equality(self):
        self.assertTrue(self.r1 == self.r3)
    
    def test_notEqual(self):
        self.assertTrue(self.r1 != self.r2)
    
    def test_center(self):
        self.assertEqual(self.r1.center(), Point(5,5))
    
    def test_area(self):
        self.assertEqual(self.r1.area(), 100)
    
    def test_move(self):
        self.assertEqual(self.r1.move(4, 1), Rectangle(4, 1, 14, 11))

if __name__ == "__main__":
    unittest.main()