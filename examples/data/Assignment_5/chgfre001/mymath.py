def get_integer(term):
    a = input ("Enter "+str(term)+ ":\n")
    while not a.isdigit ():
        a = input("Enter "+str(term)+ ":\n")
    a = eval (a)   
    return a


def calc_factorial(fact):
    pfactorial = 1
    for i in range (1, fact+1):
        pfactorial *= i  
    return pfactorial    