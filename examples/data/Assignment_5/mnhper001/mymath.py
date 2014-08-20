def get_integer(a):
    n = input ("Enter "+a+":\n")
    while not n.isdigit ():
        n = input ("Enter "+a+":\n")
    return eval(n)
def calc_factorial(b):
    bfactorial = 1
    for i in range (1, b+1):
        bfactorial *= i
    return bfactorial