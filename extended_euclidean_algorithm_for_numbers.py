

def ext_eucl(a, b): #612,342

    x0, x1 = 1, 0
    y0, y1 = 0,1

    a0, a1, q = a, b, 0
    
    if (b==0):
        return a, 1, 0
    
    while(a1!=0):
        
        q = a0//a1 #1
        a0, a1 = a1, a0 - a1*q #a1 = 612 - 342*1 = 270, a0 = 342
        x0, x1 = x1, x0 - x1*q #x0=0,x1=1
        y0, y1 = y1, y0-y1*q #y0=1, y1 = -1

    return a0, x0, y0
    
        
        

a = int(input())
b = int(input())
if (a<b):
    tmp = a
    a = b
    b = tmp

gcd,u,v = ext_eucl(a,b)
print(gcd, " = ", u, " * ", a, " + ", v, " * ", b )
#q, r = extended_eucl(int(a), int(b))
#print(a, " = ", q, " * ", b, " + ", r)
