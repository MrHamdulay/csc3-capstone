#Amy Bosworth
#ndom 

#converting ndom number to a decimal number
def ndom_to_decimal (a) :
    third=a%10
    b=a//10
    second=b%10
    first=b//10
    return (first*(6**2))+(second*(6**1))+(third*1)
    
#converting decimal number to a ndom number 
def decimal_to_ndom (a) : 
    b=a//6
    last=a%6
    c=b//6
    second=b%6
    d=c//6
    first=c%6
    if second==0 and first==0:
        second=''
    if first==0:
        first=''
    x=str(first)+str(second)+str(last)
    return x
    
#Adding 2 ndom numbers    
def ndom_add(a,b):
    c= ndom_to_decimal (a)
    d= ndom_to_decimal (b)
    ans= d+c 
    answer= decimal_to_ndom (ans)
    return answer
    
    
#Multiplying 2 ndom numbers
def ndom_multiply(a,b):
    c= ndom_to_decimal (a)
    d= ndom_to_decimal (b)
    ans= d*c 
    answer= decimal_to_ndom (ans)
    return answer    


    
    
    
    
    
    
    
        


    

    