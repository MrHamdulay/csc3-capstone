#Math.py
#Kelly Goosen
#2014/04/16

def get_integer (n): #defining function to return n or k
    if n == 'n': #string not nr.
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        return eval (n)   
    
    elif n == 'k':
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        return eval (k) 

def calc_factorial (m): #defining function to return n factorial
    nfactorial = 1
    for i in range (1, m+1):
        nfactorial *= i
    return nfactorial