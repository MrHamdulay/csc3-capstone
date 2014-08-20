#To change from a ndom to a decimal
def ndom_to_decimal(a):
    deci_number=(a//100)*36+(a%100//10)*6+a%10
    return deci_number

#To change from a decimal to a ndom
def decimal_to_ndom(a):
    three = a//36
    two=((a%36)//6)
    one=a%6
    
    if three == 0:
        three=""
    if two==0 and three==0:
        two=""
    output = str(three)+str(two)+str(one)
    eval(output)
    return output

#To add two ndom numbers
def ndom_add(a,b):
    deci_for_a=ndom_to_decimal(a)
    deci_for_b=ndom_to_decimal(b)
    c=deci_for_a+deci_for_b
    return decimal_to_ndom(c)

#to multiply two ndom numbers
def ndom_multiply(a,b):
    deci_for_a=ndom_to_decimal(a)
    deci_for_b=ndom_to_decimal(b)
    c=deci_for_a*deci_for_b
    return decimal_to_ndom(c)