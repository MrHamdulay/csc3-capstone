def decimal_to_ndom(num):
    decimal = int(num)
    ndom = ""
    base = 6
    while  num>0:
            answer = num//base
            remainder = num%base
            remainder = str(remainder)
            ndom = ndom + remainder
            num = answer
    ndom=int(ndom[::-1])
    return ndom

def ndom_to_decimal(num):
    num=str(num)
    ZERO=num[0]
    ONE=num[1]
    length=len(num)
    base=6
    if length==2:
        ZERO=int(ZERO)
        ONE=int(ONE)
        num=int(num)
        ANSWER=(ZERO*base**1) + (ONE*base**0)
    else:
        if length==3:
            ZERO=int(ZERO)
            ONE=int(ONE)
            TWO=num[2]
            TWO=int(TWO)
            num=int(num)
            ANSWER=ZERO*base**2 + ONE*base**1 + TWO*base**0    
    return ANSWER

def ndom_add(num1,num2):
    num1=ndom_to_decimal(num1)
    num2=ndom_to_decimal(num2)
    SUM=num1 + num2
    answer=decimal_to_ndom(SUM)
    return answer

def ndom_multiply(num1, num2):
    num1=ndom_to_decimal(num1)
    num2=ndom_to_decimal(num2)
    product=num1*num2
    answer=decimal_to_ndom(product)
    return answer   
