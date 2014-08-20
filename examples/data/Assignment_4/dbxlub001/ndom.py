#some awkward number game:

def ndom_to_decimal(a):
    num=str(a)
    newNum= 0
    if len(num)==3:
        newNum= int(num[0:1])*36 + int(num[1:2])*6 + int(num[2:3])
    elif len(num)==2:
        newNum= int(num[0:1])*6 + int(num[1:2])
    elif len(num)==1:
        newNum= int(num)
    return (newNum)

def decimal_to_ndom (a):
    dig1=a%36
    dig2=dig1%6
    ans=((a//36)*100)+((dig1//6)*10)+dig2
    return ans
def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    i=(x+y)
    ans=decimal_to_ndom(i)
    return ans
def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    i=(x*y)
    ans=decimal_to_ndom(i)
    return ans
    