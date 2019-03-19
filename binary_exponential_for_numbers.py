

##def binary_pow_recursive(a, b):
##    if (b==0):
##        return 1;
##    if (b % 2==0):
##        temp = binary_pow(a, int(b/2))
##        return temp*temp;
##    if (b%2 == 1):
##        return binary_pow(a, b-1)*a

def binary_pow(a, b): 
    
    res = 1
    if (b==0)&(a==0):
        return None
    while( b>0): #if b<0, 1 will be returned
           
        if (b&1):
            res *= a
        a = a*a
        b = b>>1
            
    return res   
    
print("введите число")
a = input()
print("введите степень")

b = input()
print(a, " ^ ", b, " = ", binary_pow(int(a), int(b)))
