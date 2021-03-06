from math import gcd

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1): #czy y != 0 i czy x i y to liczby!
        if(isinstance(x, int) == False or isinstance(y, int) == False):
            raise TypeError
        elif(y == 0):
            raise DenominatorZeroError()
        elif(y < 0):
            p = gcd(x, y)
            self.x = -int(x/p)
            self.y = -int(y/p)
        else:
            p = gcd(x, y)
            self.x = int(x/p)
            self.y = int(y/p)
        
    def __str__(self):              # zwraca "x/y" lub "x" dla y=1
        if(self.y != 1):
            return "{}/{}".format(self.x, self.y)
        else:
             return "{}".format(self.x)

    def __repr__(self):             # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    def cmp(self, other):           # porównywanie
        if(float(self) > float(other)):
            return -1
        elif(float(self) < float(other)):
            return 1
        else:
            return 0

    def __add__(self, other):       # frac1+frac2, frac+int
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)

    __radd__ = __add__              # int+frac

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):       # frac1-frac2, frac-int
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):       # frac1*frac2, frac*int
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__              # int*frac

    def __truediv__(self, other):       # frac1/frac2, frac/int
        if(other.x == 0):
            raise DenominatorZeroError()
        else:
            return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):      # int/frac
        if(self.x == 0):
            raise DenominatorZeroError()
        else:
            return Frac(self.y * other.x, self.x * other.y)

    # operatory jednoargumentowe
    def __pos__(self):              # +frac = (+1)*frac
        return self

    def __neg__(self):              # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):           # odwrotnosc: ~frac
        if(self.x == 0):
            raise DenominatorZeroError()
        else:
            return Frac(self.y, self.x)

    def __float__(self):            # float(frac)
        return float(self.x / self.y)
    
# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.p1 = Frac(3, 4)
        self.p2 = Frac(1, 4)
        self.p3 = Frac(1, 4)
        self.p4 = Frac(9, -11)
        
    def test_print(self):
        self.assertEqual(str(self.p1), "3/4")
        self.assertEqual(str(self.p4), "-9/11")
        self.assertEqual(repr(self.p1), "Frac(3, 4)")
        self.assertEqual(repr(self.p4), "Frac(-9, 11)")

    def test_cmp(self):
        self.assertEqual(self.p1.cmp(self.p4), -1)
        self.assertEqual(self.p1.cmp(Frac(15,20)), 0)

    def test_add(self):
        self.assertEqual(self.p2 + self.p3, Frac(1,2))
        self.assertEqual(self.p1 + self.p4, Frac(-3,44))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Frac(1,2))
        self.assertEqual(self.p1 - self.p4, Frac(69,44))

    def test_rsub(self):
        self.assertEqual((Frac(5) - self.p1), Frac(17,4))

    def test_mul(self):
        self.assertEqual(self.p2 * self.p3, Frac(1,16))
        self.assertEqual(self.p1 * self.p4, Frac(-27,44))

    def test_div(self):
        self.assertEqual(self.p2 / self.p3, Frac(1))
        self.assertEqual(self.p1 / self.p4, Frac(-11,12))

    def test_pos(self):
        self.assertTrue((+self.p1) == self.p1)

    def test_neg(self):
        self.assertTrue((-self.p4).x == 9 and (-self.p4).y == 11)

    def test_invert(self):
        self.assertEqual(~self.p1, Frac(4,3))
        self.assertEqual((~self.p4), Frac(-11,9))

    def test_float(self):
        self.assertEqual(float(self.p1), 0.75)
        self.assertAlmostEqual(float(self.p4), -0.81818182)

if __name__ == "__main__":
    unittest.main()

class DenominatorZeroError(Exception):
    def __init__(self):
        self.data = "Mianownik nie moze byc rowny 0"
    def __str__(self):
        return repr(self.data)