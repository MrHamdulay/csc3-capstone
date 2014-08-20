# permutations
# Jonathan Nathan
# 12 April 2014

def get_integer(x):
    if x == 'n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return n
    elif x == 'k':
        n = input ("Enter k:\n")
        while not n.isdigit ():
            n = input ("Enter k:\n")
        n = eval (n)  
        return n
        
def calc_factorial(x):
    nfactorial = 1
    for i in range (1, x+1):
        nfactorial *= i  
    return nfactorial