def ndom_to_decimal (a):
    if a<=5: 
        return a 
        
    elif 10<=a<=50:
        x=str(a)[1]
        y=str(a)[0] 
        y=6*int(y)             
        a=int(x)+int(y)
        return a
    elif 100<=a<=500:
        x=str(a)[2]
        y=str(a)[1]
        y=6*int(y)
        z=str(a)[0]
        z=36*int(z)
        a=int(x)+int(y)+int(z)
        return a
        
def decimal_to_ndom (a):

    ndom=""
    whole_number=a
    
    while whole_number>0:
        rem=whole_number%6
        whole_number=whole_number//6
        ndom=ndom+str(rem)
        
        answer=ndom[::-1]
    return answer
    
  
def ndom_add(a, b):        
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x+y
    answer=decimal_to_ndom(z)
    return answer

def ndom_multiply(a, b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x*y
    answer=decimal_to_ndom(z)
    return answer