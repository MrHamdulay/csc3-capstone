"""Question 3 of Assignment 5: Permutation Calculating Functions
Shaheel Kooverjee
17th April 2014"""

def get_integer(number): 
    
    if number == "n": #inputting n
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n) 
        return n
    
    if number == "k": #inputting k
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)  
        return k
    
def calc_factorial(x): 
    
    nfactorial = 1
    for i in range (1, x+1):
        nfactorial *= i 
    return nfactorial