#Tato Moaki MKXTAT001
#Module re-using combine
#Assignment5 question3

def get_integer(n):
    k = input ("Enter {}:\n".format(n))
    while not k.isdigit ():
        k = input ("Enter {}:\n".format(n))
    k = eval (k) 
    return k
    
    
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i 
    return nfactorial