import numpy

#Поиск обратного элемента в кольце вычетов по модулю n
def InverseMod(b, n):
    if (n==0):
        raise ValueError
    g, x, y = GCD(b, n)
    if g == 1:
        return x % n
    else:   #Если нет элемента
        return None

def GCD_rec(a:int, b: int):
    a, b = abs(a), abs(b)
    if (a==0 and b==0):
        return None, None, None
    if (a<b):
        tmp = a
        a = b
        b = tmp
    return GCD_rec2(a,b)

def GCD_rec2(a: int, b: int):

    if (b == 0):
        return a, 1, 0
    q = a//b #a=14, b=7, q=2
    gcd,quo,rem = GCD_rec(b, a - b*q)

    return (gcd, rem, quo - q*rem)

def GCD(a: int, b: int):
    if (a==0 and b==0):
        return None, None, None
    a0, a1, q = abs(a), abs(b), 0
    if (a0<a1):
        tmp = a0
        a0 = a1
        a1 = tmp
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    if (b == 0):
        return a, 1, 0
    while (a1):
        q = a0 // a1  # 1
        a0, a1 = a1, a0 - a1 * q  # a1 = 612 - 342*1 = 270, a0 = 342
        x0, x1 = x1, x0 - x1 * q  # x0=0,x1=1
        y0, y1 = y1, y0 - y1 * q  # y0=1, y1 = -1
    return a0, x0, y0

def PolyGCD(a: numpy.array, b: numpy.array):
    a = numpy.trim_zeros(a)
    b = numpy.trim_zeros(b)
    if (len(a)<len(b) or (len(a)==0) or (len(b)==0)):
        return None, None, None
    p0 = a[0]
    p1 = b[0]
    a0,a1 = a/p0, b/p1
    s0,s1 = 1/p0, 0
    t0, t1 = 0, 1/p1

    while(len(a1)):
        q,r = numpy.polydiv(a0,a1)

        if (len(numpy.trim_zeros(a0 - numpy.polymul(a1,q)))==0):
            return a1,s1,t1

        a0, a1 = a1, a0 - numpy.polymul(a1,q)
        a1 = numpy.trim_zeros(a1)
        lu = a1[0]
        a1 = a1/lu
        tmp = numpy.trim_zeros(numpy.polymul(s1,q))
        if (len(tmp)==0):
            tmp=0
        s0,s1 = s1, (s0 - tmp)/lu
        tmpt = numpy.trim_zeros(numpy.polymul(t1,q))
        if (len(tmpt)==0):
            tmpt=0
        t0,t1 = t1, (t0 - tmpt)/lu
    return a1,s1,t1

def PolyGCD_rec (a: numpy.array, b: numpy.array):
    a = numpy.trim_zeros(a)
    b = numpy.trim_zeros(b)
    if (len(a) < len(b) or len(a)==0):
        return None, None, None
    if (len(b) == 0):
        return a, 1, 0
    p1 = b[0]
    a = a/a[0]
    b = b/p1
    q,r = numpy.polydiv(a,b)
    tmp = numpy.trim_zeros(numpy.polymul(b, q))
    if (len(tmp) == 0):
        tmp = 0
    gcd,quo,rem = PolyGCD_rec(b, a - tmp)
    tmp1 = numpy.trim_zeros(numpy.polymul(q, rem))
    if (len(tmp1) == 0):
        tmp1 = 0
    return (gcd, rem/p1, (quo - tmp1)/p1)


