#Kovlin Perumal

def get_integer(c): #Define get_integer() function to recieve input 
    valid = False
    
    while(not valid) :
        
        if(c=="n"):
            
            n = input("Enter n:\n")
            if n.isdigit() : #Validate input to see whether its a positive digit
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

def calc_factorial (k):
    
    fact = 1
    
    for i in range(k,0,-1): #Use a for loop to calculate factorial
        fact = fact * i
    
    return fact
        
     