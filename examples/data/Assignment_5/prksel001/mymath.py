"""permuations
20/01/2014
limpho parkies"""
def get_integer(n):
    if n=="n":
        while not n.isdigit():
            n= input ("Enter n:\n")
    if n=="k":
        while not n.isdigit():
            n= input ("Enter k:\n")
    n = eval (n) 
    return n
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
    