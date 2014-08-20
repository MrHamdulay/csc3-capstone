
#program to calculate factorial

def get_integer(c):
    n = input ("Enter "+c+":\n")
    while not n.isdigit ():
        n = input ("Enter "+c+":\n")
    n = eval (n)      
    return n

def calc_factorial (b):
    nfactorial = 1
    for i in range (1, b+1):
        nfactorial *= i  
    return nfactorial
