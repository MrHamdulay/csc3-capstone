""" calculates the number of k-permutations of n items
Tim Hardie
16-4-14"""

def get_integer(var):
    print ("Enter ", var, ":", sep = '')
    input_str = input('')
    while not input_str.isdigit ():
        print ("Enter ", var, ":", sep = '')
        input_str = input('')
    input_int = int (eval (input_str))
    return input_int

def calc_factorial(num):
    factorial = 1
    for i in range (1, num+1):
        factorial *= i
    return factorial