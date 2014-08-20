def get_integer(j):
    n = input ("Enter %s:\n"%j)
    while not n.isdigit ():
        n = input ("Enter %s:\n"%j)
    n = eval (n)     
    return n
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i    
    return nfactorial