# mymath.py
# camilla craven
# 15 april 2014
# program to create functions that can calculate the number of k-permutations of n items

def get_integer(s): # defines function
    
    print("Enter ", s, ":", sep = "") # print input statement (cannot use "s" in input function)
    s = input() # create user input
    
    while not s.isdigit():
        print("Enter ", x, ":", sep = "")
        s = input()
    
    s = eval(s) # change string into number
    return s

def calc_factorial(s): # create function
    
    fact = 1
    for i in range(2,s+1): # loop to calculate factorial of a number
        fact = fact*i
        
    return fact

 
