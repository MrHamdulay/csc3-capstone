def get_integer (x):
    l="Enter "+x+":\n"
    n = input (l)
    while not n.isdigit ():
        n = input (l)
    n = eval (n)     
    return n

def calc_factorial (n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
