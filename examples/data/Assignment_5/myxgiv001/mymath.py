def get_integer(z):
    n = input ("Enter "+z+":\n")
    while not n.isdigit ():
        n = input("Enter "+z+":\n")
    n = eval (n)
    return n
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
    