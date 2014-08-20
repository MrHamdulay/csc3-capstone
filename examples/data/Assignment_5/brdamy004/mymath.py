# Assignment 5 question 3
# Amy Brodie
# 16/04/2014

# get the integer from user input
def get_integer(t):
    n_k = input("Enter " + t + ":\n")
    while not n_k.isdigit():
        n_k = input("Enter " + t + ":\n")
    return eval(n_k)

# calculate the factorial of given integer    
def calc_factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i
    return fact