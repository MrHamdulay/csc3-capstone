# the mymath program
#Wandile Lesejane
#15 April 2014

    
def calc_factorial(w):
    nfactorial = 1
    for i in range (1, w+1):
        nfactorial *= i    
    return nfactorial

def get_integer(i):
    if i=="n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return n
    elif i=="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return k
        
 