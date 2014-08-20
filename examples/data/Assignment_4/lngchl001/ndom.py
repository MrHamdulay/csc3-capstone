def ndom_to_decimal(a):
    b=0
    c=1
    firstmult=0
    for i in range(len(str(a))):
        first=eval(str(a)[b:c])
        firstmult+=first
        firstmult=firstmult*6
        b+=1
        c+=1
    final=(firstmult//6)
    return int(final)
    
def decimal_to_ndom(a):
    dec1=''    
    while True:    
        dec=str(round(a%6,1))
        dec1= dec+dec1
        a=round(a//6)
        #print(dec1,end="")
        #ans=ans[::-1]
        #print(ans)
        if a==0:
            break 
    return int(dec1)

    
def ndom_add(a,b):
    no1=ndom_to_decimal(a)
    no2=ndom_to_decimal(b)
    added=no1+no2
    no3=decimal_to_ndom(added)
    return no3

def ndom_multiply(a,b):
    no1=ndom_to_decimal(a)
    no2=ndom_to_decimal(b)    
    mult=no1*no2
    no3=decimal_to_ndom(mult)
    return no3