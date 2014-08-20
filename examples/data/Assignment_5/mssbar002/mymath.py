""""module for calculating k-permutations of n items
Author: Barnett Msiska
Date: 15/04/2014"""

def get_integer(numberString):
    promptString = "Enter " + numberString+":\n"
    n = input (promptString)
    if not n.isdigit():
        while not n.isdigit():
            n = input (promptString)
    n = eval(n)
    return n
def calc_factorial(number):
    numberFactorial = 1
    for i in range (1, number+1):
        numberFactorial *= i  
    return numberFactorial