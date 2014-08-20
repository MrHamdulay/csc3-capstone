
#Assignment5 Question2
#MDLCAR002
#module containing functions

def get_integer(x):
    number = input ("Enter "+x+":\n")
    while not number.isdigit ():
        number = input ("Enter "+x+":\n")
    number=eval(number)
    return number

def calc_factorial(x):
    xfactorial = 1
    for i in range (1, x+1):
        xfactorial *= i
    return xfactorial

    
        

    
   
    