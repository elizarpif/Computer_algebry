
def Karatsuba(a, b):
    
    alen = len(str(a))
    blen = len(str(b))
    length = max(alen, blen)

    if (length<2):
        return a*b
    
    if (length&1):
        length = length+1
    
    length = length//2
    
    al = a//10**length
    ar = a%10**length
    
    bl = b//10**length
    br = b%10**length

    p1 = Karatsuba(al, bl)
    p2 = Karatsuba(ar,br)

    return p1*10**(length*2)+p2+(Karatsuba(al+ar, bl+br)-p1-p2)*10**length


a = input()
b = input()
c = Karatsuba(int(a), int(b))
                
print (a, "*", b, " = ", c)
    


    
        
