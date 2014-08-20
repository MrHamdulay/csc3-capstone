def get_integer(schar):
    x = input ("Enter "+schar+":\n")
    while not x.isdigit ():
        x = input ("Enter "+schar+":\n")
    return eval(x) 
    
def calc_factorial(x):
    nfactorial = 1
    for i in range (1, x+1):
        nfactorial *= i    
    return nfactorial