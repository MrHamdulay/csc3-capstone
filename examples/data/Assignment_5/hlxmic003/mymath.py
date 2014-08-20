# Michaela Heale
# Assignment 5 Question 3
# Factorial Methods

def calc_factorial(a):
    newfac = 1
    for z in range(a,0,-1):
        newfac *= z
    return newfac
        
def get_integer(t):
    n = input("Enter {}:\n".format(t))
    while not n.isdigit ():
        n = input("Enter {}:\n".format(t))  
    n = eval (n) 
    return n
