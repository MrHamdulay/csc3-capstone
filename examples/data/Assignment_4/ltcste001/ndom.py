#Stephanie Latchmanan
#LTCSTE001
#Assignment 4

def ndom_to_decimal(a):
    a=str(a)
    if len(a)==1 :
        a=int(a)
        return a
    
    elif len(a)==3 :
        dig=int(a[2])
        ten=int(a[1])
        hun=int(a[0])
        b=(dig*1)+(ten*6)+(hun*36)
        return b
    
    elif len(a)==2 :
            dig=int(a[1])
            ten=int(a[0])
            b=(dig*1)+(ten*6)
            return b
        
    elif len(a)==4 :
        dig=int(a[3])
        ten=int(a[2])
        hun=int(a[1])
        thous=int(a[0])
        b=(digits*1)+(tens*6)+(hundreds*36)+(thousands*216)
        return b
    
def decimal_to_ndom(a):
    thous=a//216
    hun=(a-(thous*216))//36
    ten=(a-(thous*216)-(hun*36))//6
    dig=(a-(thous*216)-(hun*36)-(ten*6))//1
    b=(thous*1000)+(hun*100)+(ten*10)+dig
    return b

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a+b
    c=decimal_to_ndom(c)
    return c

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a*b
    c=decimal_to_ndom(c)
    return c  