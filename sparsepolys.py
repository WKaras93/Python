
def add_poly(poly1, poly2):
    poly = poly1.copy()
    for x, y in poly2.items():
        print(x, y)
        if x in poly1:
            poly[x] += y
        else:
            poly[x] = y
    return poly

def sub_poly(poly1, poly2):
    poly = poly1.copy()
    for x, y in poly2.items():
        print(x, y)
        if x in poly1:
            poly[x] -= y
        else:
            poly[x] = -y
    return poly

def mul_poly(poly1, poly2):
    poly = {}
    for x, y in poly1.items():
        for a,b in poly2.items():
            if((x+a) in poly):
                poly[x+a] += y * b
            else:
                poly[x+a] = y * b
    return poly

def is_zero(poly):
    i = 0
    for x in poly.values():
        if(x == 0):
            i += 1
    if(i == len(poly)):
        return True
    else:
        return False

def cmp_polys(poly1, poly2):
    if(len(poly1) == len(poly2)):
        for x in poly1:
            if(x in poly2 and poly1[x] == poly2[x]):
                continue
            else:
                return False
        return True
    else:
        return False

def pow_poly(poly, n):
    poly2 = {}
    for x in poly:
        poly2[pow(x, n)] = pow(poly[x], n)
    return poly2

def diff_poly(poly):
    poly2 = {}
    for x in poly:
        if(x > 0):
            poly2[x-1] = poly[x] * x
    return poly2