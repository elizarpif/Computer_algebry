from numpy.polynomial.polynomial import Polynomial as Poly
from fractions import Fraction
import math

#1. С помощью метода Ньютона реализовать функцию нахождения многочлена, обратного к заданному f*g = 1
#2. Реализовать операцию деления с остатком a = qb + r

def GCD(a: int, b: int):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    a0, a1, q = a, b, 0
    if (b == 0):
        return a, 1, 0
    while (a1):
        q = a0 // a1  # 1
        a0, a1 = a1, a0 - a1 * q  # a1 = 612 - 342*1 = 270, a0 = 342
        x0, x1 = x1, x0 - x1 * q  # x0=0,x1=1
        y0, y1 = y1, y0 - y1 * q  # y0=1, y1 = -1
    return a0, x0, y0

#Поиск обратного элемента в кольце вычетов по модулю n
def inverse(b, n):
    g, x, y = GCD(b, n)
    if g == 1:
        return x % n
    else:   #Если нет элемента
        return None

def modPoly(f: Poly, n: int):
    coefs = f.coef
    for i in range(len(coefs)):
        coefs[i] = coefs[i]%n
    return Poly(coefs)

def PolyInverseModOverZn(f: Poly, r: int, zn: int): #r=2, mod zn r = log2
    if (r<1) or (zn<1):
        raise ValueError
    #f = modPoly(f, zn)
    f0 = f.coef[0]
    if (not(f0 == 1)):
        g = Poly(inverse(f0,zn))
    else:
        g = Poly(f0)
    if (g.coef[0] == None or zn==1):
        return None
    l = int(math.ceil(math.log2(r)))
    for k in range(1, l + 1):
        g = (2 * g - f * (g ** 2))

        g = g.truncate(2 ** k)
        g = modPoly(g,zn)
    return g


def PolyInverseModOverQ(f: Poly, r: int): #r=2, предполагаем f0[0] = 1
    f = f.trim()
    if (r<1):
        raise ValueError
    #f = modPoly(f, zn)
    f0 = f.coef[0]
    if (f0 != Fraction(1,1)):
        f0 = 1/f0
    if (f0 == Fraction(0,1)):
        return None
    g = Poly(f0)

    l = int(math.ceil(math.log2(r)))

    for k in range(1, l + 1):
        g = (2 * g - f * (g ** 2))
        g = g.truncate(2 ** k)
    return g

def PolyDivModOverZn (a, b : Poly , n : int): #−> (Poly , Poly ):
    a = a.trim()
    b = b.trim()
    if (n<1):
        raise ValueError
    if (a.degree() < b.degree()):
        return Poly([0]), a
    m = a.degree() - b.degree()
    revb = Poly(b.coef[::-1])
    rrevb = PolyInverseModOverZn(revb, m+1,n)
    if (rrevb is None):
        raise ZeroDivisionError("")
    reva = Poly(a.coef[::-1])
    q1 = reva*rrevb
    q1 = q1.truncate(m+1)
    q = Poly(q1.coef[::-1])
    q = modPoly(q, n)
    bq = b*q
    bq = modPoly(bq,n)
    r = modPoly(a - b*q,n)
    r = Poly(r.coef[::-1])
    r.trim()
    r = Poly(r.coef[::-1])
    return q, r

def PolyDivModOverQ (a, b : Poly ): #−> (Poly , Poly ):
    while(a.degree()>0 and  a.coef[a.degree()] == Fraction(0,1)):
        a = Poly(a.coef[:a.degree()])
    while(b.degree()>0 and  b.coef[b.degree()] == Fraction(0,1)):
        b = Poly(b.coef[:b.degree()])
    if (a.degree() < b.degree()):
        return Poly([Fraction(0,1)]),a

    m = a.degree() - b.degree()
    revb = Poly(b.coef[::-1])
    rrevb = PolyInverseModOverQ(revb, m+1)
    if (rrevb is None):
        raise ZeroDivisionError("ohohoh")
    q1 = Poly(a.coef[::-1])*rrevb
    q1 = Poly(q1.coef[:(m+1)])
    q = Poly(q1.coef[::-1])
    r = a - b * q
    while(r.degree()>0 and r.coef[r.degree()] == Fraction(0,1)):
        r = Poly(r.coef[:r.degree()])
    return q, r


# a = Poly([1,2,3,4])
# print(a*a)
# a = Poly([1,2,3,4,5,6,7,8,9])
# print(a*a)

