import numpy as np

def IntKaratsuba(a: int, b: int):

    if ((a < 0) and (b > 0))or((a > 0)and(b < 0)):
        flg = -1
    else:
        flg = 1

    return IntKaratsuba2(a,b)*flg

def IntKaratsuba2(a: int, b: int):

    if (a == 0) or (b == 0):
        return 0

    a = abs(a)
    b = abs(b)

    length = max(int(np.log10(a)+1), int(np.log10(b)+1))
    if length < 2:
        return a * b

    if length & 1:
        length = length + 1

    length = length // 2

    al = a // 10 ** length
    ar = a % 10 ** length

    bl = b // 10 ** length
    br = b % 10 ** length

    p1 = IntKaratsuba2(al, bl)
    p2 = IntKaratsuba2(ar, br)

    return p1 * 10 ** (length * 2) + p2 + (IntKaratsuba2(al + ar, bl + br) - p1 - p2) * 10 ** length


def PolyKaratsuba(a: np.array, b: np.array):

    length = max(a.size, b.size)

    if length < 2:
        return a*b

    if length & 1:
        length += 1

    a = np.append(np.zeros((length-a.size,), dtype=int),a)
    b = np.append(np.zeros((length-b.size,), dtype=int),b)


    len2 = length//2
    #надо поделить пополам
    al = a[:len2]
    ar = a[len2:]

    bl = b[:len2]
    br = b[len2:]

    p1 = PolyKaratsuba(al, bl)
    p2 = PolyKaratsuba(ar, br)

    p3 = PolyKaratsuba(np.polyadd(al,ar), np.polyadd(bl,br))
    p3 = np.polysub(p3,p1)
    p3 = np.polysub(p3, p2)

    p1 = np.append(p1,np.zeros((length,), dtype=np.int))
    p3 = np.append(p3, np.zeros((len2,), dtype=np.int))
    res = np.polyadd(p1,p2)
    res = np.polyadd(res, p3)
    while (res.size > 1 and res[0] == 0):
     res = res[1:]
    return res


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
#
# def BinPowMod_rec(a, b):
#    if (b==0):
#        return 1;
#    if (b % 2==0):
#        temp = BinPowMod_rec(a, int(b/2))
#        return temp*temp;
#    if (b%2 == 1):
#        return BinPowMod_rec(a, b-1)*a

def BinPowMod(a, b, n):
    res = 1
    if (n==0):
        raise ValueError("mod 0")
    if (b == 0) and (a == 0):
        return None
    if (b<0):
        a = inverse(a,n)
        if (not a) and (not(a==0)):
            return a
        b *= -1
    while (b > 0):  # if b<0, 1 will be returned

        if (b & 1):
            res = (res*a)%n
        a = a * a
        b = b >> 1

    return res