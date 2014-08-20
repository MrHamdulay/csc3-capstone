def decimal_to_ndom(num):
    rem=num%36
    num-=rem
    hundreds=(num//36)*100
    rem2=rem%6
    rem-=rem2
    tens=(rem//6)*10
    ndom=hundreds+tens+rem2
    return ndom

def ndom_to_decimal(num):
    rem=num%100
    num-=rem
    thirsixs=(num//100)*36
    rem2=rem%10
    rem-=rem2
    six=(rem//10)*6
    deci=thirsixs+six+rem2
    return deci

def ndom_add (num1, num2):
    decimal = ndom_to_decimal(num1)+ndom_to_decimal(num2)
    return decimal_to_ndom(decimal)

def ndom_multiply (num1, num2):
    decimal = ndom_to_decimal(num1)*ndom_to_decimal(num2)
    return decimal_to_ndom(decimal)    