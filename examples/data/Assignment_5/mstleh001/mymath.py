#Lehlogonolo Masetla

def get_integer(value):
    
    l = input ("Enter "+value+":\n")
    while not l.isdigit ():
        l = input("Enter "+value+":\n")
    l = eval (l)
    return l
    
def calc_factorial(l):
    nfactorial = 1
    for i in range (1, l+1):
        nfactorial *= i
    return nfactorial