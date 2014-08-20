def ndom_to_decimal (a):
    a = str(a)
    z = len(a)

    if z == 3:
        number1 = eval(a[0])
        number2 = eval(a[1])
        number3 = eval(a[2])
        result = (number1*36 + number2*6 + number3)
   
    elif z == 2:
        number1 = eval(a[0])
        number2 = eval(a[1]) 
        result = (number1*6 +number2)
    
    elif z == 1:
        number1 = eval(a[0])
        result = number1
        
    return result

def decimal_to_ndom (a):
    if a >= 216:
        b= a//216    
        a = a-(216*b)
        if a < 216 and a >= 36:
            c= a//36    
            a = a-(36*c)
            if a < 36 and a >=6:
                d= a//6    
                a = a-(6*d)
                if a <6 and a >= 0:
                    e= a//1    
                    a = a-(1*e)
                    Result = b*1000+c*100+d*10+e*1
    elif a < 216 and a >= 36:
        b= a//36    
        a = a-(36*b)
        if a < 36 and a >=6:
            c= a//6    
            a = a-(6*c)
            if a <6 and a >= 0:
                d= a//1    
                a = a-(1*d)
                Result = b*100+c*10+d*1
        elif a <6 and a >= 0:
                c= a//1    
                a = a-(1*c)
                Result = b*100+c*1
    elif a < 36 and a >=6:
        b= a//6    
        a = a-(6*b)
        if a <6 and a >= 0:
            c= a//1    
            a = a-(1*c)
            Result = b*10+c*1    
    elif a <6 and a >= 0:
        b= a//1    
        a = a-(1*b)
        Result = b     
    
    return Result

def ndom_add (a, b):
    return decimal_to_ndom (ndom_to_decimal (a) -- ndom_to_decimal (b))

def ndom_multiply (a, b):
    return decimal_to_ndom (ndom_to_decimal (a) * ndom_to_decimal (b))