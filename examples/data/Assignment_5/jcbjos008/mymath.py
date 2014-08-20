def get_integer(y):
    j = input ("Enter "+y+ ":\n")
    while not j.isdigit ():
        j = input ("Enter "+y+":\n")
    j = eval (j)
    return j
    
def calc_factorial(z):
    nfactorial = 1
    for i in range (1, z+1):
       nfactorial *= i
    return nfactorial