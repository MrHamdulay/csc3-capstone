def get_integer(s):
    n = input ("Enter " + s+ ":\n")
    while not n.isdigit ():
        n = input ("Enter " + s+ ":\n")
    return eval (n)

def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
    


