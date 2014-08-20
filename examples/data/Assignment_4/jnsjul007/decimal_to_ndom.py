def ndom_to_decimal (a):
    decimal_hundreds=(a//36)*100
    rem_hundreds = (a%36)
    decimal_tens = (rem_hundreds//6)*10
    rem_tens = ((a%6)//1)*1
    decimal = (rem_tens + decimal_tens + decimal_hundreds)
    return decimal


def decimal_to_ndom(b):
    ndom_hundreds = (b//100)*36
    rem_hundreds = b%100
    ndom_tens = (rem_hundreds//10)*6
    rem_tens = (b%10)
    ndom1 = (rem_tens + ndom_tens + ndom_hundreds)
    return ndom1

def ndom_add (a, b):
    