# Алгоритм Карацубы ( для чиселок и многочленов )
# 305*485
# (03+05)(04+85)
#
#def Karatsuba(a, b):


def multiply(str1, str2, length):
    
    if (length<2):
        return int(str1)* int(str2)
    else:
        return Karatsuba(str1, str2)


def degree(string, n): #дополнение нулями n раз
    
    while (n>0):
        string = "0" + string
        n = n-1
        
    return string
    



def Karatsuba(a, b):

    a_len = len(a)
    b_len = len(b)

    if (a_len < b_len): #берем разряд a_len как наибольщий
        temp = a_len
        a_len = b_len
        b_len = temp
        
    if (a_len & 1): #если нечетное
        a = degree(a, 1)
        a_len += 1

    #дополняем нулями вторую строку
    b = degree(b, a_len - b_len)
    
    #print("a = ", a, " , b = ", b)
    
    a_len = int(a_len/2)
                
    a1 = a[:a_len]
    a2 = a[a_len:]
    b1 = b[:a_len]
    b2 = b[a_len:]
                
    temp_mult = multiply(a1,b2, a_len)+multiply(a2,b1, a_len)
    

    res = pow(10, a_len*2)*multiply(a1,b1, a_len) + pow(10, a_len)*temp_mult + multiply(a2,b2, a_len)

    return res
        



#return string[int(len(string)/2):]
a = input()
b = input()
c = Karatsuba(a, b)
                
print (a, "*", b, " = ", c)
    


#print("остаток от деления", a_count%2)

    
        
