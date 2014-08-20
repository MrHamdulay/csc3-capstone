"""Daniel Schwartz
mymath module for q3
april 2014"""


def get_integer(s):
    """Asks the user for an integer, called s, and keeps asking until it receives a proper integer.
    Then returns that integer"""
    n = input ("Enter " + s +":\n")
    while not n.isdigit ():
        n = input ("Enter " + s+ ":\n")
    n = eval (n)
    return n


def calc_factorial(n):
    """Calculates the factorial of the number n, and returns it"""
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
