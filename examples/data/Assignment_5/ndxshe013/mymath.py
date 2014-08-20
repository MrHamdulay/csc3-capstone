
def get_integer (x):
    n = input ("Enter "+x+":\n")
    while not n.isdigit ():
        n = input ("Enter "+x+":\n")
    n = eval (n)    
    return n
def calc_factorial (y):
    nfactorial = 1
    for i in range (1, y+1):
        nfactorial *= i
    return nfactorial

