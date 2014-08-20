""" Mymath module re-using code from combine.py
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-14 """

def get_integer(nok):
    """Returns an integer recieved from the user"""
    if nok == 'n':
        n = input('Enter n:\n')
        # checks if n is an integer
        while not n.isdigit():
            n = input('Enter n:\n')
        return eval(n)      
    else:
        k = input('Enter k:\n')
        # checks if k is an integer
        while not k.isdigit():
            k = input('Enter k:\n')
        return eval(k)  

def calc_factorial(n):
    """ Returns the factorial of a given number n"""
    factorial = 1
    for i in range (1, n+1):
       factorial *= i
    return factorial