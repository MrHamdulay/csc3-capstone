def ndom_to_decimal(a):
    n = str(a)
    if len(n) == 1:
        print(a)
    elif len(n) == 2 :
        return ((int(n[0])*6)+int(n[1]))
    elif len(n) == 3:
        return ((int(n[0])*36)+(int(n[1])*6)+(int(n[2])))
    
               
def decimal_to_ndom(a): 
    n = str(a)
    if len(n) < 3:
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
    x = ndom_to_decimal(a) + ndom_to_decimal(b)
    return (decimal_to_ndom(x)) 
    
   
   
def ndom_multiply(a,b):
    x = ndom_to_decimal(a)*ndom_to_decimal(b)
    return (decimal_to_ndom(x))
    
