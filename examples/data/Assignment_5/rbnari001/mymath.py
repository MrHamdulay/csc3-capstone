#Ariel Rubin
#RBNARI001
#16 April 2014
#Calculating factorials

#creates the function get_integer(n)
#n is a parameter in the functiion
def get_integer (n):
#if statement asks the user to enter a digit
# the while loop will continue to run until the user enters a number >=0
    if n == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n) 
        return n
#if statement asks the user to enter a digit
# the while loop will continue to run until the user enters a number >=0
    elif n == "k":    
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return k
#creates the function calc_factorial(n)
#n is a parameter in the functiion
#the function performs a calculation for a factorial
def calc_factorial (n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
    
     
   