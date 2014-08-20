def get_integer(st):
    if st == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n) 
        return n
    if st == "k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k) 
        return k
    
    
def calc_factorial (num):
    if len(str(num)) == 1:
        nfactorial = 1
        for i in range (1, num+1):
            nfactorial *= i  
        return nfactorial
    else:
        nkfactorial = 1
        for i in range (1, num+1):
            nkfactorial *= i        
        return nkfactorial