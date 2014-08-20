def ndom_to_decimal(z):
    nu=(z//100)*36+(z%100//10)*6+z%10
    return nu

def decimal_to_ndom(z):
    uni=z%6
    tens=(z%36)//6
    hunds = z//36
    if hunds == 0:
        hunds=""
    if tens==0 and hunds==0:
        tens=""
    nu = str(hunds)+str(tens)+str(uni)
    eval(nu)
    return nu
    
def ndom_add(z,x):
    a_decimal=ndom_to_decimal(z)
    b_decimal=ndom_to_decimal(x)
    c=a_decimal+b_decimal
    return decimal_to_ndom(c)
    
def ndom_multiply(z,x):
    a_decimal=ndom_to_decimal(z)
    b_decimal=ndom_to_decimal(x)
    c=a_decimal*b_decimal
    return decimal_to_ndom(c)