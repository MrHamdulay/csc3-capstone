
def ndom_to_decimal (x):
    d = ((x//100) * 36) +  (((x%100//10) *6) + ((x%100) %10))
    return d



def decimal_to_ndom (x):
    
    answer=((x//36) *100)  + ((x%36//6)*10)  + (x %36)%6
     
     
    return answer    

    
    
def ndom_add (x,y):
    y = ndom_to_decimal (x) + ndom_to_decimal (y)
    answer= decimal_to_ndom(z)
    
    return answer

def ndom_multiply (x,y):
    z= ndom_to_decimal(x) * ndom_to_decimal (y)
    ans = decimal_to_ndom(z)
    
    return ans