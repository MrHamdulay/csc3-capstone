def ndom_to_decimal(num):
    num = str(num)
    dec_num = 0
    if len(num) == 3:
        dec_num = (eval(num[0])*36+eval(num[1])*6+eval(num[2]))
    elif len(num) == 2:
        dec_num = (eval(num[0])*6+eval(num[1]))
    elif len(num) == 1:
        dec_num = eval(num)
    return dec_num

def decimal_to_ndom(num):
    num = str(num)
    ndom_num = 0
    if len(num) == 1:
        ndom_num = eval(num)
    elif len(num) == 2:
        dig1 = str(eval(num)%6)
        dig2 = str((eval(num)//6)%6)
        if eval(num)>36:
            dig3 = str((eval(num)//36)%6)
            ndom_num = eval(dig3+dig2+dig1)
        else:
            ndom_num = eval(dig2+dig1)
        
    elif len(num) == 3:
        dig1 = str(eval(num)%6)
        dig2 = str((eval(num)//6)%6)
        dig3 = str((eval(num)//36)%6)
        if eval(num)>216:
            dig4 = str((eval(num)//216)%6)
            ndom_num = eval(dig4+dig3+dig2+dig1)
        else:
            ndom_num = eval(dig3+dig2+dig1)
    return ndom_num

def ndom_add(num1,num2):
    return decimal_to_ndom(ndom_to_decimal(num1)+ndom_to_decimal(num2))

def ndom_multiply(num1,num2):
    return decimal_to_ndom(ndom_to_decimal(num1)*ndom_to_decimal(num2))

