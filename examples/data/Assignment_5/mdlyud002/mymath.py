
# Yudhi Moodley
# Assignmnt 5 Question 1 
# 14 April 2014
# Write a code function for perumatation calculator

# string conversion, changes to int and returns
def get_integer(n): 
    integer = input("Enter " + n + ":\n")
    while not integer.isdigit ():
        integer = input("Enter " + n + ":\n")
    integer = eval(integer)
    return integer
        
# Calculate for n        
def calc_factorial (n): 
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial   
