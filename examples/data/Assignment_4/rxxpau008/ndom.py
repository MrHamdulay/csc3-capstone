def ndom_to_decimal(a):
    x = a
    i = 0
    f = 0
    while x:
        p = (x%10)*(6**i)
        x = x//10
        f = f+p
        i+=1
    return f
    
def decimal_to_ndom(a):
    f = ''
    while a:
        f = str(a%6)+f
        a = a//6  
    return eval(f)
    
def ndom_add(a,b):
    add = ndom_to_decimal(a)+ndom_to_decimal(b)
    return decimal_to_ndom(add)    
    
def ndom_multiply(a,b):
    multiply = ndom_to_decimal(a)*ndom_to_decimal(b)
    return decimal_to_ndom(multiply)