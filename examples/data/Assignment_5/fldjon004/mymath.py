# mymath.py
# jono field 
# 16 april 2014
# program to define functions that are used to calculate permutations


def get_integer (n): # defines function
    # get choice from user using a print function with variable and then using input function
    print("Enter", n, end="")
    print(":")
    n=input()
    while not n.isdigit ():
        print("Enter", n, end="")
        print(":")
        n=input()               
    n = eval (n) 
    return n 

def calc_factorial (n): # defines function
    fact = 1
    for i in range(2,n+1): # loop to create factorial function
        fact*= i
    return fact
