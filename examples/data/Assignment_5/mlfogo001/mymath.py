

def get_integer(a):
    n = input ("Enter "+a+":\n")
    while not n.isdigit ():
        n = input ("Enter "+a+":\n")
    n = eval (n)
    return n

def calc_factorial(b):
    nfactorial = 1
    for i in range (1, b+1):
        nfactorial *= i
    return nfactorial
