def ndom_to_decimal (num):
    a=str(num)
    g=0                          #CHANGES from BASE 6 to BASE 10
    e=1                          
    if len(a)==1:
        x=eval(a[g])*6
        return x
    elif len(a)==2:
        x=eval(a[g])*6
        y=x+(eval(a[e]))
        return y
    elif len(a)==3:
        x=eval(a[g])*6
        y=x+(eval(a[e]))        
        g+=1
        e+=1
        x=y*6
        y=x+(eval(a[e]))
        return y

def decimal_to_ndom(num):
        y=''
        if len(str(num))==1:
                z=num%6             #CHANGES from BASE 10 to BASE 6
                y=y+str(z)
                y=y[::-1]
                y=int(y)
                return y
        elif len(str(num))==2 :
                z=num%6
                y=y+str(z)        
                x=num//6
                z=x%6
                y=y+str(z)
                x=x//6
                z=x%6
                y=y+str(z)                
                y=y[::-1]
                y=int(y)
                return(y)
        elif len(str(num))==3 :
                z=num%6
                y=y+str(z)        
                x=num//6
                z=x%6
                y=y+str(z)        
                x=x//6
                z=x%6
                y=y+str(z)
                y=y[::-1]
                y=int(y)
                return(y)     

def ndom_add (a, b):
    hun=(a//100)*(6**2)          #Hundreds
    ten=((a%100)//10)*(6**1)      #Tens
    uni=((a%100)%10)*(6**0)       #Units
    a=hun+ten+uni                 #Adds BASE 6 numbers
            
    hun=(b//100)*(6**2)
    ten=((b%100)//10)*(6**1)
    uni=((b%100)%10)*(6**0)
    b=hun+ten+uni   
            
    ndomadd=a+b
    num=ndomadd
    y=''
    if len(str(num))==1:
        z=num%6
        y=y+str(z)
        y=y[::-1]
        y=int(y)
        return y
    elif len(str(num))==2 :
        z=num%6
        y=y+str(z)        
        x=num//6
        z=x%6
        y=y+str(z)
        y=y[::-1]
        y=int(y)
        return y
    elif len(str(num))==3 :
        z=num%6
        y=y+str(z)        
        x=num//6
        z=x%6
        y=y+str(z)        
        x=x//6
        z=x%6
        y=y+str(z)
        y=y[::-1]
        y=int(y)
        return y  
        
         
def ndom_multiply (a, b):
    hun=(a//100)*(6**2)          #Hundreds
    ten=((a%100)//10)*(6**1)      #Tens
    uni=((a%100)%10)*(6**0)       #Units
    a=hun+ten+uni                 #Adds BASE 6 numbers
  
    hun=(b//100)*(6**2)
    ten=((b%100)//10)*(6**1)
    uni=((b%100)%10)*(6**0)
    b=hun+ten+uni   
    ndommultiply=a*b
    num=ndommultiply
    y=''
    if len(str(num))==1:
        z=num%6
        y=y+str(z)
        y=y[::-1]
        y=int(y)
        return y
    elif len(str(num))==2 :
        z=num%6
        y=y+str(z)        
        x=num//6
        z=x%6
        y=y+str(z)
        x=x//6
        z=x%6
        y=y+str(z)        
        y=y[::-1]
        y=int(y)
        return y
    elif len(str(num))==3 :
        z=num%6
        y=y+str(z)        
        x=num//6
        z=x%6
        y=y+str(z)        
        x=x//6
        z=x%6
        y=y+str(z)
        y=y[::-1]
        y=int(y)
        return y  
