"""Module to simplify program that calculates number of k-permutations of n items
Kemeshan Naicker
16 April 2014"""

#Create program get_integer which stores an integer supplied by the user.
def get_integer(x):
    prompt_msg = "Enter "+str(x)+":\n"
    integer = input (prompt_msg)
    while not integer.isdigit ():
        integer = input (prompt_msg)
    integer = eval (integer)
    return(integer)
          
#Create program calc_factorial which calculates the factorial of a supplied integer
def calc_factorial(y):
    factorial = 1
    for i in range (1, y+1):
        factorial *= i
    return(factorial)