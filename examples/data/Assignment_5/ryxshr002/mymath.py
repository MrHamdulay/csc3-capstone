"""Shriya Roy
16 April 2014
factorial program"""

def get_integer(s):
    x = 'abc'
    #evaluating whether it's a digit or not
    while x.isdigit() == False:
        x = input('Enter '+ s + ':\n')
    return eval(x)

def calc_factorial(n):
    #computing factorial
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans
