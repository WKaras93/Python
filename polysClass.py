from collections import OrderedDict
def sort(slownik):
    return OrderedDict(sorted(slownik.items()), key = lambda x:x[0])

class Poly:
    """Klasa reprezentujaca wielomiany."""
    def __init__(self, slownik = {0:0}):
        if(isinstance(slownik, (dict, OrderedDict))):
            for k,v in slownik.items():
                if(not isinstance(k, int)):
                    raise TypeError("Wrong type of first argument in dict")
                elif(not isinstance(v, (int, float))):
                    raise TypeError("Wrong type of second argument in dict")
            self.a = slownik
        else:
            raise TypeError("Argument is not dict")
    
    def __str__(self):
        return str(self.a)
    
    def __repr__(self):
        return str(sort(self.a))
    
    def __add__(self, other):
        if(isinstance(other, Poly)):
            poly = self.a
            for k,v in other.a.items():
                if k in poly:
                    poly[k] += v
                else:
                    poly[k] = v
            return Poly(poly)
        else:
            raise TypeError("Second argument is not poly")
    
    def __sub__(self, other):
        if(isinstance(other, Poly)):
            poly = self.a
            for k,v in other.a.items():
                if k in poly:
                    poly[k] -= v
                else:
                    poly[k] = -v
            return Poly(poly)
        else:
            raise TypeError("Second argument is not poly")
    
    def __mul__(self, other):
        if(isinstance(other, Poly)):
            poly = {}
            for k,v in self.a.items():
                for a,b in other.a.items():
                    if((k+a) in poly):
                        poly[k+a] += v*b
                    else:
                        poly[k+a] = v*b
            return Poly(poly)
        else:
            raise TypeError("Second argument is not poly")
    
    def __pos__(self):
        return Poly(self.a)
    
    def __neg__(self):
        poly = {}
        for k,v in self.a.items():
            poly[k] = -v
        return Poly(poly)
    
    def __eq__(self, other):
        if(isinstance(other, Poly)):
            if(len(self.a) != len(other.a)):
                return False
            else:
                for k,v in other.a.items():
                    if k in self.a:
                        continue
                    else:
                        return False
                return True
        else:
            raise TypeError("Second argument is not poly")

    def __ne__(self, other):
        return not self == other

    def __pow__(self, n):
        poly = {}
        for k,v in self.a.items():
            poly[pow(k,n)] = pow(v,n)
        return Poly(poly)
    
    def diff(self):
        poly = {}
        for k,v in self.a.items():
            if(k > 0):
                poly[k-1] = k*v
        return Poly(poly)

import unittest
class TestPolysClass(unittest.TestCase):
    def setUp(self):
        self.p1 = Poly({0:5, 1:3, 4:6})
        self.p2 = Poly({0:3, 2:3, 5:6})
        self.p3 = Poly({0:5, 1:-3})
    
    def test_print(self):
        self.assertEqual(str(self.p1), "{0: 5, 1: 3, 4: 6}")
    
    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Poly({0:8, 1:3, 2:3, 4:6, 5:6}))
        #self.assertEqual(self.p1 + self.p3, Poly({0:10, 1:0, 4:6}))
    
    def test_sub(self):
        #self.assertEqual(self.p1 - self.p2, Poly({0:2, 1:3, 2:-3, 4:6, 5:6}))
        self.assertEqual(self.p1 - self.p3, Poly({0:0, 1:6, 4:6}))
    
    def test_mul(self):
        self.assertEqual(self.p1 * self.p3, Poly({0:25, 1:0, 2:-9, 4:30, 5:-18}))
    
    def test_pos(self):
        self.assertEqual(+self.p1, self.p1)
    
    def test_neg(self):
        self.assertEqual(-self.p2, Poly({0:-3, 2:-3, 5:-6}))
    
    def test_pow(self):
        self.assertEqual(self.p3**2, Poly({0:25, 1:9}))
    
    def test_diff(self):
        self.assertEqual(self.p2.diff(), Poly({1:6, 4:30}))

if __name__ == "__main__":
    unittest.main()