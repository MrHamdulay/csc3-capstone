"""calculating number of k permutations
kennedy muranda
16/4/2014"""

#validate input from user
def get_integer(c):
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

#calculating factorial
def calc_factorial (k):
    
    fact = 1
    
    for i in range(k,0,-1):
        fact = fact * i
    
    return fact
        
     