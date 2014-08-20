""" Calculating permutations program
Julian Albert
ALBJUL005
15-04-2014"""

import math
#defines nofk
def get_integer(n_of_k):
    if n_of_k == 'n':
        n = input('Enter n:\n')
        while not n.isdigit(): #accounts for strings in n
            n = input('Enter n:\n')
        n = eval(n)
        return n #users input returned
    else:
        k = input('Enter k:\n')
        while not k.isdigit(): #accounts for strings in k
            k = input('Enter k:\n')
        k = eval(k)        
        return k #users input returned

def calc_factorial(n):
    factorial = 1
    for i in range (1, n+1): #range of calculation
        factorial *= i
    return factorial #returns calculated amount