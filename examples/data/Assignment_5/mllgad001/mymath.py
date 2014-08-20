# program that calculates the number of k-permutations of n items
# Gadija Moollagie
# 16 April 2014

def get_integer(x): # defines get_integer function that is used in main program
    if x == 'n':
        n = input ("Enter n:\n") # prompts user to input a number n
        while not n.isdigit (): # while it is not valid, continue to input n
            n = input ("Enter n:\n")
        n = eval (n)
        return n
   
    if x == 'k':
        k = input ("Enter k:\n") # prompts user to input a number k
        while not k.isdigit (): # while it is not valid, continue to input k
            k = input ("Enter k:\n")
        k = eval (k)
        return k 
    
def calc_factorial(n): # defines factorial function used in main program
    for i in range(1): # loops through this once
        nfactorial = 1
        for i in range (1, n+1):
            nfactorial *= i # calculates factorial
        return nfactorial
    
    for i in range(1): # loops through this once
        nkfactorial = 1
        for i in range (1, n-k+1):
            nkfactorial *= i # calculates factorial
    return nkfactorial
    