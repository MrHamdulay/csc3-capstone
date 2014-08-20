"""modules working out permutations
Lorena Dal Maso
16 April 2014"""


def get_integer(vari):
    
    if vari=='n':
        p=""
        while not p.isdigit ():
            p=input("Enter n:\n")
    elif vari=='k':
        p=""
        while not p.isdigit ():
            p=input("Enter k:\n")
    return int(p)

def calc_factorial(vari):
        nfactorial = 1
        for i in range (1, vari+1):
            nfactorial *= i
        return nfactorial
    
    
        