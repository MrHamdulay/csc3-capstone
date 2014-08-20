#THRIANKA NAIDOO
#NDXTHR005
#Assignment 4
#question 2

#converts nos with base 6 to base 10
def ndom_to_decimal(x): 
    h = x//100 
    t = (x%100)//10
    d = (x%100)%10
    return (h*36)+(t*6)+d


#converts nos with base 10 to base 6
def decimal_to_ndom(x): 
    h = x//36 
    t = (x%36)//6
    d = (x%36)%6
    return (h*100)+(t*10)+d

#adds two base 6 nos
def ndom_add(a,b):  
    c = ndom_to_decimal(a)+ndom_to_decimal(b) 
    ans = decimal_to_ndom(c) 
    return ans

# * two base 6 nos
def ndom_multiply(a,b): 
    c = ndom_to_decimal(a)*ndom_to_decimal(b) 
    ans = decimal_to_ndom(c) 
    return ans    
    