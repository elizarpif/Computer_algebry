def binary_pow_mod(a, b, n): #3, 7=111, n = 6
    
    res = 1
    if ((b==0)&(a==0)) or (n==0):
        return None
    while( b>0): #if b<0, 1 will be returned
           
        if (b&1):
            res = res * a%n
        a = a*a 
        #print(res)
        b = b>>1
            
    return res   
    
print("введите число")
a = input()
print("введите степень")
b = input()
print("введите mod ")
n = input()
print("( ", a, " ^ ", b, " ) mod ", n, " = ", binary_pow_mod(int(a), int(b), int(n)))
