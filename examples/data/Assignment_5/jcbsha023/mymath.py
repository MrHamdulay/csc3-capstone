#program to create math module to be imported into another program
#Anthony Jacob
#16b April 2014

def get_integer(c):   #asking user for input
    valid = False
    while(not valid) :
        if(c=="n"):
            n = input("Enter n:\n")
            if n.isdigit() :
                if eval(n) >= 0 :
                    return eval(n)
                else:
                    continue
            else:
                continue
            
        if(c=="k"):
            k = input("Enter k:\n")
            if k.isdigit() :
                if eval(k) >= 0 :
                    return eval(k)
                else:
                    continue
            else:
                continue  
    
        
             
    
def calc_factorial (k):    #calculation factorial
    
    fact = 1
    
    for i in range(k,0,-1):
        fact = fact * i
    
    return fact
