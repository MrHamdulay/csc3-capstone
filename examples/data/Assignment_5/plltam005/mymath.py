""" Calculating permutations
Tameryn Pillay
16 April 2014 """

# Getting n and k

def get_integer(number):
    integer = input ("Enter " + number + ":\n")
    while not integer.isdigit ():
        integer = input ("Enter " + number + ":\n")
    number = eval (integer) 
    return number

# calculating factorials of n and k    

def calc_factorial(number):   
    nfactorial = 1
    for i in range (1, number+1):
        nfactorial *= i
    return nfactorial
