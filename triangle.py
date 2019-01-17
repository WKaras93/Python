from points import Point

def det(x1, y1, x2, y2, x3, y3):
    return x1*y2+y1*x3+x2*y3-x3*y2-x1*y3-x2*y1

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""
    def __init__(self, x1, y1, x2, y2, x3, y3):
        if(det(x1, y1, x2, y2, x3, y3) == 0):
            raise ValueError("Points are collinear")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
            self.pt3 = Point(x3, y3)

    def __str__(self):              # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[({}, {}), ({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __repr__(self):             # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):        # obsługa tr1 == tr2
        if(self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3):
            return True
        else:
            return False          

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):               # zwraca środek trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)

    def area(self):                 # pole powierzchni
        return abs((self.pt2.x-self.pt1.x)*(self.pt3.y-self.pt1.y) - (self.pt2.y-self.pt1.y)*(self.pt3.x-self.pt1.x))/2

    def move(self, x, y):           # przesunięcie o (x, y)
        return Triangle(self.pt1.x+x, self.pt1.y+y, self.pt2.x+x, self.pt2.y+y, self.pt3.x+x, self.pt3.y+y)

    def make4(self):                # zwraca listę czterech mniejszych
        s1 = Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)
        s2 = Point((self.pt2.x + self.pt3.x)/2, (self.pt2.y + self.pt3.y)/2)
        s3 = Point((self.pt3.x + self.pt1.x)/2, (self.pt3.y + self.pt1.y)/2)
        return [Triangle(self.pt1.x, self.pt1.y, s1.x, s1.y, s3.x, s3.y), Triangle(s1.x, s1.y, s2.x, s2.y, s3.x, s3.y), Triangle(s3.x, s3.y, s2.x, s2.y, self.pt3.x, self.pt3.y), Triangle(s1.x, s1.y, self.pt2.x, self.pt2.y, s2.x, s2.y)]

# Kod testujący moduł.
import unittest

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.t1 = Triangle(0, 0, 6, 0, 0, 6)
        self.t2 = Triangle(-1, -1, 2, 2, 5, -1)
    
    def test_print(self):
        self.assertEqual(str(self.t1), "[(0, 0), (6, 0), (0, 6)]")
        self.assertEqual(repr(self.t2), "Triangle(-1, -1, 2, 2, 5, -1)")
    
    def test_equal(self):
        self.assertTrue(self.t1 == Triangle(0, 0, 6, 0, 0, 6))
    
    def test_notEqual(self):
        self.assertTrue(self.t1 != self.t2)
    
    def test_center(self):
        self.assertEqual(self.t1.center(), Point(2, 2))
        self.assertEqual(self.t2.center(), Point(2, 0))
    
    def test_area(self):
        self.assertEqual(self.t1.area(), 18)
    
    def test_move(self):
        self.assertEqual(self.t1.move(-3, -3), Triangle(-3, -3, 3, -3, -3, 3))

if __name__ == "__main__":
    unittest.main()