import math


def decimal_to_ndom(x):
    
    

    num = 0
    q = 1
    p = 0
    while (1==1):
        num += (x%6)*10**p
        if(x//6) == 0:
            break
    
        x = x//6
        p +=1
    
    
    return num

def ndom_to_decimal (x):
    num1 = 0
    l = len(str(x))
    cnt = len(str(x))
    p = cnt-1
    for i in range (l):
        num1+=eval(str(x)[i])*(6**p)
        p= p-1
    return (num1)

def ndom_add(x,y):
    added = ndom_to_decimal(x)+ ndom_to_decimal(y)
    value = decimal_to_ndom(added)
    return (value)
def ndom_multiply(x,y):
    added = ndom_to_decimal(x)* ndom_to_decimal(y)
    value = decimal_to_ndom(added)
    return (value)

        



    
    
    
