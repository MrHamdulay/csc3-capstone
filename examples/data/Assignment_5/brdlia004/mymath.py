import math
    
def get_integer(x):
    if x == "n":
        global n
        n = input("Enter n:\n")
        if not n.isdigit () or int(n) <= 0:
            n = input("Enter n:\n")
            while  not n.isdigit () or int(n) <= 0:
                n = input ("Enter n:\n") 
            n = int(n)
            return n                                
        n = int(n)
        return n
    
    
    elif x == "k":
        global k
        k = input("Enter k:\n")
        if not k.isdigit () or int(k) <= 0:
            k = input("Enter k:\n")
            while  not k.isdigit () or int(k) <= 0:
                k = input ("Enter k:\n")
            k = int(k)
            return k                      
        k = int(k)
        return k
          
def calc_factorial(y):
    if y == n:
        nfactorial = math.factorial(y)
        return nfactorial
    if y == n-k:
        nkfactorial =  math.factorial(y)
        return nkfactorial
 
        
    
    

    
    