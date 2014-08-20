def get_integer(n):
    a = input("Enter "+str(n)+":\n")
    while not a.isdigit ():
        a = input ("Enter "+str(n)+":\n")
    a = eval (a)
    return a

def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i    
    return nfactorial
