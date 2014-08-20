#Decimals and Ndom
def ndom_to_decimal(a):
    if len(str(a))==1:
        if 6<=a<=9:
            return False
        else:
            dec=a
    if len(str(a))==2:
        if a//10==6 or a%10==6 or a//10==7 or a%10==7 or a//10==8 or a%10==8 or a//10==9 or a%10==9:
            return False
        else:
            dec= (a//10)*6+a%10
    if len(str(a))==3:
        if 6<=a//10<=9 or 6<=a%10<=9:
            return False
        else:
            dec= (((a//10)-(4*(a//100)))*6)+a%10
    return dec
            
def decimal_to_ndom(a):
    if len(str(a))==1:
        if 6<=a<=9:
            ndom=a+4
        else:
            ndom=a    
    
    if 10<=a<36:
        ndom= (a//6*4) +a
        
    if a>=36:
        ndom= (a//6*4)+a+(40*(a//36))
        
    return ndom

def ndom_add(a,b):
    x=(a%10+b%10)
    x1=x-((x//6)*(6))
    y=((a%100-a%10)+(b%100-b%10)+(x//6)*10)
    y1=y-(y//6)*(6)
    y1=y1*10
    z=((a%1000-a%100)+(b%1000-b%100)+(y//60)*100)
    ans= z+y1+x1
    
    return ans

def ndom_multiply(a,b):
    a= ndom_to_decimal(a)
    b= ndom_to_decimal(b)
    ans=a*b
    ans= decimal_to_ndom(ans)
    return ans
    


