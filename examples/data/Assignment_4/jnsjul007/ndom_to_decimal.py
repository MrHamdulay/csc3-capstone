def ndom_to_decimal (a):
    decimal_hundreds=(a//36)*100
    rem_hundreds = (a%36)
    decimal_tens = (rem_hundreds//6)*10
    rem_tens = ((a%6)//1)*1
    decimal = (rem_tens + decimal_tens + decimal_hundreds)
    print(decimal)
ndom_to_decimal (12)    

def decimal_to_ndom(b):
    ndom_hundreds = (b//100)*36
    rem_hundreds = b%100
    ndom_tens = (rem_hundreds//10)*6
    rem_tens = (b%10)
    ndom = (rem_tens + ndom_tens + ndom_hundreds)
    print(ndom)
decimal_to_ndom(20)    