"""MyMath get the integer, with 2 functions in python 
Assignment 5
Nandani Birjanund
16/04/14"""

def get_integer(s): #function 1
    x = 'hsd'
    while x.isdigit() == False:
        x = input('Enter ' + s + ':\n')
     #Return integer   
    return eval(x)


def calc_factorial(s): #function 2
    n = 1
    for i in range(1, s + 1):
                                   # Finds the factorial
        n *= i
    return n