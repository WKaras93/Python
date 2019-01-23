from math import sqrt

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        x = format(round(self.x, 2), '.2f')
        y = format(round(self.y, 2), '.2f')
        return "({}, {})".format(x, y)

    def __repr__(self):         # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):    # obsługa point1 == point2
        if(self.x == other.x and self.y == other.y):
            return True
        else:
            return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # suma 2 wektorow
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)          # zwraca wektor

    def __sub__(self, other):       # roznica dwoch wektorow
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def test_print(self):
        self.assertEqual(str(Point(12, 13)), "(12.00, 13.00)")
        self.assertEqual(str(Point(12, 13.00455)), "(12.00, 13.00)")
        self.assertEqual(repr(Point(12, 13)), "Point(12, 13)")
        self.assertEqual(repr(Point(12.00001, 13)), "Point(12.00001, 13)")
    
    def test_equal(self):
        self.assertEqual(Point(12, 13), Point(12, 13))
        self.assertTrue(Point(12, 13) == Point(12, 13))
        self.assertFalse(Point(12, 13) == Point(12, 13.00001))
    
    def test_notEqual(self):
        self.assertNotEqual(Point(1, 2), Point(1.5, 2))
        self.assertTrue(Point(12, 13) != Point(12, 13.00001))

    def test_add(self):
        self.assertEqual(Point(12, 13.9999) + Point(13, 14), Point(25, 27.9999))
        self.assertEqual(Point(12.0001, 13) + Point(13, 14.045), Point(25.0001, 27.045))
        self.assertEqual(Point(-12, 13) + Point(13, -14), Point(1, -1))
    
    def test_sub(self):
        self.assertEqual(Point(12, 13) - Point(13, 14), Point(-1, -1))
        self.assertEqual(Point(-12, 13) - Point(13, -14), Point(-25, 27))
    
    def test_mul(self):
        self.assertEqual(Point(12, 13) * Point(13, 14), 338)
        self.assertEqual(Point(1.00001, 2) * Point(9, 1), 11.00009)
        self.assertEqual(Point(2, 2) * Point(0.0009, -1), -1.9982)

    def test_cross(self):
        self.assertEqual(Point.cross(Point(12, 13), Point(13, 14)), -1)
        self.assertEqual(Point.cross(Point(1.00001, 2), Point(9, 1)), -16.99999)
        
    def test_length(self): pass

if __name__ == "__main__":
    unittest.main()