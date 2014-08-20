# This module contains functions
# get_integer ("n"), asks a user to enter number
# calc_factorial(n), calculates the factorial of the integer n

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 15 April 2014

# This function asks the user to enter an integer named "numstr"
def get_integer(numstr):
    
    print("Enter ",numstr,":",sep='')
    num = input() # waits for user to enter an integer
    
    # Loop until a user stops entering strings
    while not num.isdigit():
        print("Enter ",numstr,":",sep='')
        num = input()
    
    return eval(num)
       
    
    
# This functions calculates the factorial of a number    
def calc_factorial(n):    
    n = int(n) # passes parameter to a local variable & convert to integer
    facto = 1 # default factorial
    
    for i in range (n,1,-1):
        facto *= i    
        
    return facto


# Sample I/O:

# Enter n:
# 4
# Enter k:
# 2
# Number of permutations: 12