

def calc_factorial (n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i 
    return nfactorial
def nkfactorial(k):
    nkfactorial = 1
    for i in range (1, n-k+1):
        nkfactorial *= i 
def get_integer (n):
    if n =='n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return int(n)
    if n =='k':    
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)  
        return int(k)

