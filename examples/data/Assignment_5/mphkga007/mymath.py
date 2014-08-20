

import math
def get_integer(n):
    integer=input("Enter "+n+":\n")
    while not integer.isdigit():
        integer=eval(input("Enter "+n+":\n"))
    integer=eval(integer)
    return integer

def calc_factorial(n):

    
    f=math.factorial(n)
    
    return f
#calc_factorial(3)

#def calc_factorial(n):

  #  number = 1
    #while n >= 1:
       # number = number * n
       # n = n - 1
    #return number