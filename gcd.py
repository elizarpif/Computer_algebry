import numpy


#Поиск обратного элемента в кольце вычетов по модулю n
def inverse(b, n):
    g, x, y = GCD(b, n)
    if g == 1:
        return x % n
    else:   #Если нет элемента
        return None

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

def PolyGcd(a: numpy.array, b: numpy.array):
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
        s0,s1 = s1, s0 - tmp
        s1 = s1/lu
        tmpt = numpy.trim_zeros(numpy.polymul(t1,q))
        if (len(tmpt)==0):
            tmpt=0
        t0,t1 = t1, t0 - tmpt
        t1 = t1/lu
    return a1,s1,t1

# a = numpy.array([18,-42,30,-6])
# print(len(a))
# b = numpy.array([-12,10,-2])
# r,s,t = PolyGcd(a,b)
#
# print(r)
# print(s)
# print(t)