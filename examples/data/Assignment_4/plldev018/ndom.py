def ndom_to_decimal(a):
    num = 0    
    number = str(a)
    if (len(number) ==3):
        x = number[0:1]
        y = number[1:2]
        z = number [2:]
        num = num + int(x)*36+ int(y)*6 + int(z)
    elif(len(number) == 2):
        x = number[0:1]
        y = number[1:]
        num = num + int(x)*6 + int(y)
    else:
        num = num + int(number)
    return num

def decimal_to_ndom(a):
    numstr = ""
    x = a // 36
    y = (a - (36*x))//6
    r = a - x*36 - y*6
    numstr = str(x) + str(y) + str(r) 
    return int(numstr)

def ndom_add(a,b):
    num1 = ndom_to_decimal(a)
    
    num2 = ndom_to_decimal(b)
    add = num1 + num2
    return decimal_to_ndom(add)

def ndom_multiply(a,b):
    num1 = ndom_to_decimal(a)
    num2 = ndom_to_decimal(b)
    multiply = num1 * num2
    return decimal_to_ndom(multiply)