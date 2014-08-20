#Question2
#Ndom and decimal
#By: Dean de Haast

def ndom_to_decimal (a):
    total=0
    a=str(a)
    exp=len(a)
    for x in a:
        exp=exp-1
        x=int(x)
        total +=(x*(6**exp))      
    return(total)
        
def decimal_to_ndom (a):
    quot=a
    total=""
    while quot !=0:
        rem = quot%6
        quot =quot//6
        rem=str(rem)
        total=total+rem
       
    return(total[::-1])    

def ndom_add (a,b):

    totala=0
    a=str(a)
    exp=len(a)
    for x in a:
        exp=exp-1
        x=int(x)
        totala +=(x*(6**exp))
            
    totalb=0
    b=str(b)
    exp=len(b)
    for x in b:
        exp=exp-1
        x=int(x)
        totalb +=(x*(6**exp))
        
    total = totala +totalb
       
    quot=total
    newtotal=""
    while quot !=0:
        rem = quot%6
        quot =quot//6
        rem=str(rem)
        newtotal=newtotal+rem
    return(newtotal[::-1])

def ndom_multiply (a, b):
    
    totala=0
    a=str(a)
    exp=len(a)
    for x in a:
        exp=exp-1
        x=int(x)
        totala +=(x*(6**exp))
            
    totalb=0
    b=str(b)
    exp=len(b)
    for x in b:
        exp=exp-1
        x=int(x)
        totalb +=(x*(6**exp))
        
    total = totala *totalb
       
    quot=total
    newtotal=""
    while quot !=0:
        rem = quot%6
        quot =quot//6
        rem=str(rem)
        newtotal=newtotal+rem
    return(newtotal[::-1])        