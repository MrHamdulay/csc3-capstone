#Robin Hall
#Program to inter-convert between senary and decimal numbers
#4/4/2014

def ndom_to_decimal(a):
    a = str(a)
    x = len(a)
    
    if x == 3:
        dig_1 = eval(a[0])
        dig_2 = eval(a[1])
        dig_3 = eval(a[2])
        decimal = dig_1*36 + dig_2*6 + dig_3
        return decimal
    
    elif x == 2:
        dig_1 = eval(a[0])
        dig_2 = eval(a[1])
        decimal = dig_1*6 + dig_2
        return decimal
    
    elif x == 1:
        dig_1 = eval(a[0])
        decimal = dig_1
        return decimal
    
    else:
        False

def decimal_to_ndom(a):
    a = str(a)
    x = len(a)
    
    if x == 3:
        
        a = eval(a)
        if a > 215:
            dig_1 = a//216
            r1 = a%216
            dig_2 = r1//36
            r2 = r1%36
            dig_3 = r2//6
            r3 = r2%6
            dig_4 = r3
            ndom = dig_1*1000+dig_2*100+dig_3*10+dig_4
            return ndom
        
        else:
            dig_1 = a//36
            r1 = a%36
            dig_2 = r1//6
            r2 = r1%6
            dig_3 = r2
            ndom = dig_1*100+dig_2*10+dig_3
            return ndom
        
    elif x == 2:
        
        a = eval(a)
        if a > 35:
            dig_1 = a//36
            r1 = a%36
            dig_2 = r1//6
            r2 = r1%6
            dig_3 = r2
            ndom = dig_1*100+dig_2*10+dig_3
            return ndom
        
        else:
            dig_1 = a//6
            r1 = a%6
            dig_2 = r1
            ndom = dig_1*10+dig_2
            return ndom
        
    elif x == 1:
        
        a = eval(a)
        ndom = a%6+10
        return ndom
    
    else:
        False
        
def ndom_add(a,b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    decimal = x + y
    ndom = decimal_to_ndom(decimal)
    return ndom

def ndom_multiply(a,b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    decimal = x*y
    ndom = decimal_to_ndom(decimal)
    return ndom
    
    
