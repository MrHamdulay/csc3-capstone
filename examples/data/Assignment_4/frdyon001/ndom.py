# Name: Yonela Ford
# Student Number: FRDYON001
# Programme using Ndom
# Date: 29 March 2014

def ndom_to_decimal(a):
    x=str(a)
    y=x[::-1]
    j=0 
    result=0
    
    for i in y:
        k=(eval(i))*(6**(j))
        j+=1
        result+=k
    return result


# Converting decimal to Ndom*
def decimal_to_ndom(a):
    ans=a
    out=" "
    quotient=0
    while quotient>=0:
        quotient=ans//6
         
        x=ans%6
        y=str(x)
        out+=y
        ans=quotient
        if quotient==0: break
    return out[::-1]

    
#adding to Ndom* numbers
def ndom_add(a,b):
    #First convert numbers to decimal
    l=ndom_to_decimal(a)
    n=ndom_to_decimal(b)
    #Add decimals
    s=(l+n)
    #Convert sum back to Ndom*
    p=decimal_to_ndom(s)
    return p

# Mulitplying two Ndom* numbers
def ndom_multiply(a,b):
    #First convert each number to a decimal
    e=ndom_to_decimal(a)
    f=ndom_to_decimal(b)
    #Mulitply the decimals
    g=(e*f)
    #convert back to Ndom*
    h=decimal_to_ndom(g)
    return h

    

    
    

        
    
    
    