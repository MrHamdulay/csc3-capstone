
def ndom_to_decimal(at):
    deci_number=(at//100)*36+(at%100//10)*6+at%10
    return deci_number


def decimal_to_ndom(at):
    three = at//36
    two=((at%36)//6)
    one=at%6
    
    if three == 0:
        three=""
    if two==0 and three==0:
        two=""
    output = str(three)+str(two)+str(one)
    eval(output)
    return output


def ndom_add(at,bj):
    deci_for_a=ndom_to_decimal(at)
    deci_for_b=ndom_to_decimal(bj)
    c=deci_for_a+deci_for_b
    return decimal_to_ndom(c)


def ndom_multiply(at,bj):
    deci_for_a=ndom_to_decimal(at)
    deci_for_b=ndom_to_decimal(bj)
    c=deci_for_a*deci_for_b
    return decimal_to_ndom(c)
