# a library for ndom
# mashau zwivhuya
# 1 april 2014
def decimal_to_ndom (a):
    num=a
    strr=""
    rem=""
    while num>0.0001:
        b=num//6
        strr=num%6
        rem=str(strr)+rem
        num=b
    remm=int(rem)    
    return remm 
#
def ndom_add (a, b):
    #convert ndom to decimal a
    lenth=len(str(a))
    count=0
    num=str(a)[::-1]
    for i in range(lenth):
        x=(6**i)*eval(num[i])
        count=x+count
    dec_numbera=count
    #convert ndom to decimal b
    lenth=len(str(b))
    count=0
    num=str(b)[::-1]
    for i in range(lenth):
        x=(6**i)*eval(num[i])
        count=x+count
    dec_numberb=count 
    #add decimals
    total=dec_numbera+dec_numberb
    #convert back to ndom
    num=total
    strr=""
    rem=""
    while num>0.0001:
        b=num//6
        strr=num%6
        rem=str(strr)+rem
        num=b
    remm=int(rem)    
    return remm 
#
def ndom_to_decimal (a):
    lenth=len(str(a))
    count=0
    num=str(a)[::-1]
    for i in range(lenth):
        x=(6**i)*eval(num[i])
        count=x+count
    return count
#
def ndom_multiply (a, b):
    #convert ndom to decimal a
    lenth=len(str(a))
    count=0
    num=str(a)[::-1]
    for i in range(lenth):
        x=(6**i)*eval(num[i])
        count=x+count
    dec_numbera=count
    #convert ndom to decimal b
    lenth=len(str(b))
    count=0
    num=str(b)[::-1]
    for i in range(lenth):
        x=(6**i)*eval(num[i])
        count=x+count
    dec_numberb=count    
    #multiply decimals
    mult=dec_numberb*dec_numbera
    #convert back to ndom
    num=mult
    strr=""
    rem=""
    while num>0.0001:
        b=num//6
        strr=num%6
        rem=str(strr)+rem
        num=b
    remm=int(rem)    
    return remm

        
        
    