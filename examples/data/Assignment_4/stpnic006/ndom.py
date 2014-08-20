

def ndom_to_decimal(a):
    num = 0    
    number = str(a)
    if (len(number) ==3):
        num += int(number[0:1])*36+ int(number[1:2])*6 + int(number[2:])
    elif(len(number) == 2):
        num+= int(number[0:1])*6 + int(number[1:])
    else:
        num+= int(number)
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
    add = num1 * num2
    return decimal_to_ndom(add)