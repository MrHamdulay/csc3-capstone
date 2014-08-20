def ndom_to_decimal(num):
    d=0
    num=str(num)
    l=len(num)
    i=0
    for j in num[::-1]:
        p=(6**i)*int(j)
        i=i+1
        d+=p
        
    return d

def decimal_to_ndom(num):
    n=''
    d=num
    while d!=0:
        r=str(d%6)
        n=n+r
        d=d//6
    return n[::-1]
    
    
decimal_to_ndom(32)        
        
        
    
    