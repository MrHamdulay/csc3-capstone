#Dumisani J Nyathi
#03-04-2014
def ndom_to_decimal(a):
    x=str(a)
    x=x[::-1]
    
    ones=int(x[:1])
    
    
    sixes=x[1:2]
    if sixes!="":
        sixes=(int(sixes))*6
    else: sixes=0
    
    
    thirtySixes=x[2:3]
    if thirtySixes!="":
        thirtySixes=(int(thirtySixes))*36
    else: thirtySixes=0
          
    ans=(ones + sixes + thirtySixes)
    return ans


def decimal_to_ndom (a):
    x=str((a//36))
    x+=str(((a%36)//6))
    x+=str((a%36)%6)
    x=int(x)
    return x

def ndom_add(a, b):
    c=ndom_to_decimal(a)
    d=ndom_to_decimal(b)
    e=c+d
    f=decimal_to_ndom (e)
    return f
    
def ndom_multiply (a, b):
    g=ndom_to_decimal(a)
    h=ndom_to_decimal(b)
    i=g*h
    j=decimal_to_ndom (i)
    return j