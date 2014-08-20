#Description: More readable and space efficient version of combine.py
#Name: Paul Roux - RXXPAU008
#Date: 15 April 2014

def get_integer(s):#Gets an integer from the user
    num = input("Enter "+s+":\n")
    while not num.isdigit ():
        num = input("Enter "+s+":\n")
    return eval(num)

def calc_factorial(s):#Calculates the factorial of an integer
    factorial = 1
    for i in range (1, s+1):
        factorial*=i
    return factorial
    
    