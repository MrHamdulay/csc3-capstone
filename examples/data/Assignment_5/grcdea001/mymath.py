"""Program to get integers and calculate factorials Prac 5 Question 3
Dean Gracey
4/15/2014"""


def get_integer(n): # gets an integer
    toreturn = input ("Enter "+ n + ":\n")
    while not toreturn.isdigit ():
        toreturn = input ("Enter "+ n + ":\n")   
    return int(toreturn)
    
    
def calc_factorial(n):# calculates integers factorial
    n = int(n)
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i    
    return nfactorial
    

