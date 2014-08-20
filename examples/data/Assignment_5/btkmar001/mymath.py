# combines the different parts of combine.py into seperate functions for external use
# Martin Batek
# 15 april 2014

def get_integer(a):
    # A function that asks the user for a number value and returns it
    x = input ("Enter "+a+":\n")
    while not x.isdigit ():
        # Ensures that x is a number
        x = input ("Enter "+a+":\n")
    x = eval (x)
    # converts x into an integer
    return x


def calc_factorial(a):
    # A function that calculates the factorial of a number provided by the user
    factorial = 1
    for i in range (1, a+1):
        factorial *= i
      
    return factorial