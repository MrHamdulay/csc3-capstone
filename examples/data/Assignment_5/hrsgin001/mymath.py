
def get_integer(st1):
    if (st1 == "n"):
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        value = eval (n)   
    elif(st1 == "k"):
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        value = eval (k)
    return value
        
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i        
    value = nfactorial
    return value