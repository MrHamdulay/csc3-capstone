# Module to calculate number of k-permutations of n items
# Denzel Ncube
# 14 April 2014

# Function to get the two integers
def get_integer(word):
    n = input("Enter " + str(word)+": \n")
    while not n.isdigit ():
        n = input ("Enter " + str(word)+": \n")
    n = eval(n)
    return n
#Function to calculate the factorial
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i 
    return nfactorial
