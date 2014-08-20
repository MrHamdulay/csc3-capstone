def get_integer(letter):
    l = input ("Enter "+letter+":\n")
    while not l.isdigit ():
        l = input("Enter "+letter+":\n")
    l = eval (l)
    return l
    
def calc_factorial(l):
    nfactorial = 1
    for i in range (1, l+1):
        nfactorial *= i
    return nfactorial