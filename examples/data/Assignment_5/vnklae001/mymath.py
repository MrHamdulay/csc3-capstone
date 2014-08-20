# Question 3 - Assignment 5
# A program that calculates the number of permutations in 2 given functions
# Written by: Laene van Niekerk

def get_integer(x):
    if x == "n":                        # Checks if the input is "n"
        n = (input("Enter n:\n"))
        while not n.isdigit():          # If the string entered is not a number
            n = input("Enter n:\n")
    else:
        n = (input("Enter k:\n"))       # Checks if the input is "k"
        while not n.isdigit():          # If the string entered is not a number
            n = input("Enter k:\n")
    n = eval(n)     # Evaluates n as a number that we can use to calculate the factorial
    return n        # Returns the number to be used

def calc_factorial(n):  # Calculating the factorial of a given number
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i 
    return nfactorial