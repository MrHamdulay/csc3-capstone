#To change from a ndom to a decimal
def ndom_to_decimal(a):
    deci_num=(a//100)*36+(a%100//10)*6+a%10
    return deci_num

#To change from a decimal to a ndom
def decimal_to_ndom(a):
    third = a//36
    sec=((a%36)//6)
    first=a%6
    
    if third == 0:
        third =""
    if sec==0 and third==0:
        sec=""
    output = str(third)+str(sec)+str(first)
    eval(output)
    return output

#To add two ndom numbers
def ndom_add(x,y):
    deci_for_x=ndom_to_decimal(x)
    deci_for_y=ndom_to_decimal(y)
    z=deci_for_x+deci_for_y
    return decimal_to_ndom(z)

#to multiply two ndom numbers
def ndom_multiply(x,y):
    deci_for_x=ndom_to_decimal(x)
    deci_for_y=ndom_to_decimal(y)
    z=deci_for_x*deci_for_y
    return decimal_to_ndom(z)
