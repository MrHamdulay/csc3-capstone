#Konrad Hugo HGXKON001
#Question3 Assignment 5


def get_integer(nork): #Returns an inputed or inserted integer from user
    if nork == 'n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval(n) #Checks whether or not 'n' is an integer
        return n
    if nork == 'k':
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k) #Checks whether or not 'k' is an integer
        return k


def calc_factorial(t):
#returns factorial of a number t    
    nkfactorial = 1

    for i in range (1, t+1):
        nkfactorial *= i
    return nkfactorial

    
        