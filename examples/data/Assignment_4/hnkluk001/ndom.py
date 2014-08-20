# Luke Henkeman, HNKLUK001
# CSC1015F, Assignment 4, Q2
# 30 March 2014

def decimal_to_ndom(a):
    z = str(a)
    if len(z) == 3:
        a3 = a//216
        a2 = (a%216)//36
        a1 = ((a%216)%36)//6
        a0 = ((a%216)%36)%6
        return a0+a1*10+a2*100+a3*1000
    elif len(z) == 2:
        a2 = a//36
        a1 = (a%36)//6
        a0 = (a%36)%6
        return a0+a1*10+a2*100
    else:
        a1 = a//6
        a0 = a%6
        return a0+a1*10
        
def ndom_to_decimal(a):
    z = str(a)
    if len(z) == 3:
        a2 = a//100
        a1 = (a%100)//10
        a0 = (a%100)%10
        return a0+a1*6+a2*36
    elif len(z) == 2:
        a2 = a//100
        a1 = (a%100)//10
        a0 = (a%100)%10
        return a0+a1*6+a2*36
    else:
        a1 = a//10
        a0 = a%10
        return a0+a1*6
        
def ndom_add(a,b):
    dec_a = ndom_to_decimal(a)
    dec_b = ndom_to_decimal(b)
    dec_c = dec_a + dec_b
    return decimal_to_ndom(dec_c)

def ndom_multiply(a,b):
    dec_a = ndom_to_decimal(a)
    dec_b = ndom_to_decimal(b)
    dec_c = dec_a * dec_b
    return decimal_to_ndom(dec_c)


        
