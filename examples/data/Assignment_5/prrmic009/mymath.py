"""mymath module of get_integer and calc_factorial functions.
Question 3 of Assignment 5
Mick Perring
16 April 2014"""

def get_integer (x): # get_integer function, prompts user to
    if x == "n":     # input values for n and k
        n = "a"
        while not n.isdigit ():  # if n is not a valid digit (positive integer),
            n = input("Enter n:\n") # prompt user to enter n again
        n = int(n)
        return n
    elif x == "k":
        k = "a"
        while not k.isdigit ():  # if k is not a valid digit (positive integer),
            k = input("Enter k:\n") # prompt user to enter n again
        k = int(k)
        return k
    
def calc_factorial (x): # calc_factorial function, calculates 
    fact = 1            # factorial of input value
    for i in range (1, x+1):
        fact *= i
    return fact