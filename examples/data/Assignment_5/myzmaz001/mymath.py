"""" 
Mazwi Myeza
16 April 2014
Assignment5
Question3
"""
# Function to get integers from user
def get_integer(k):
    if k == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
           n = input ("Enter n:\n")
        n = eval (n)
        return n
    elif k == "k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
           k = input ("Enter k:\n")
        k = eval (k) 
        return k
    #Function to calculate factorial
def calc_factorial(n):
    nfactorial = 1
    nkfactorial = 1
    for i in range (1, n+1):
       nfactorial *= i 
       nkfactorial *= i
       
    return nfactorial
    return nkfactorial
   
 