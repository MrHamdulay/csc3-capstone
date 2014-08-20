def decimal_to_ndom (num):  
    sixno = 0
    oneno = 0
    ret = 0
    if(num == 1 or num == 2 or num ==3 or num == 4 or num == 5):
        #number stays the same
        num = num
        ret = num
    else:
        n1 = num//36
        sizno = num%36
        n2 = sizno//6
        n3 = sizno%6
        st1 = str(n1) + str(n2) + str(n3)
        ret = int(st1)
    return ret

def ndom_to_decimal(num):
    finalnum = 0
    s1 = str(num)
    if(num == 1 or num == 2 or num ==3 or num == 4 or num == 5):
        #number stays the same
        num = num
        ret = num
    elif(len(s1) == 3):
        n1 = int(s1[0]) * 36
        n2 = int(s1[1]) * 6
        n3 = int(s1[2]) * 1
        finalnum = n1+n2+n3
        ret = finalnum
    else:#len == 2
        n1 = int(s1[0]) * 6
        n2 = int(s1[1]) * 1
        finalnum = n1+n2
        ret = finalnum
    return ret    

def ndom_add(a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    sumn = a + b
    return decimal_to_ndom(sumn)

def ndom_multiply(a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    sumn = a * b
    return decimal_to_ndom(sumn)


