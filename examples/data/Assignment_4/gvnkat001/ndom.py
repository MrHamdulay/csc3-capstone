def ndom_to_decimal(a):
    x = str(a)
    
    if len(x) == 1:
        print(a)
        
    elif len(x) == 2 :
        return ((int(x[0])*6)+int(x[1]))
    
    elif len(x) == 3:
        return ((int(x[0])*36)+(int(x[1])*6)+(int(x[2])))
    
               
def decimal_to_ndom(a): 
    y = str(a)
    if len(y) < 3:
        l = a%6
        nex = a//6
        s = nex%6
        f = nex//6
        return int(str(f)+str(s) + str(l))        
            
    else: 
        l = a%6
        nex = a//6
        s = (nex%6)*10
        nex= nex//6
        f = (nex%6)*100
        return (f+s+l)
    
def ndom_add(a,b):
    x = int(ndom_to_decimal(a))
    y = int(ndom_to_decimal(b))
    
    ADD= x+y
    sumNdom = decimal_to_ndom(ADD)
    
    return sumNdom

def ndom_multiply(a,b):
    x = int(ndom_to_decimal(a))
    y = int(ndom_to_decimal(b))
    
    times= x*y
    product = decimal_to_ndom(times)
    
    return product
    
       
   


    