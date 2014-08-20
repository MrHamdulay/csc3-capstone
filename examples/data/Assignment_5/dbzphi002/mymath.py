#Thembekile Dubazana
#Assignment 5:Q3
#April 2014
""" Revised calculation of permutations"""

#Check if integer
def get_integer(Input):
    if Input == "n":
        while not Input.isdigit():
            Input= input("Enter n:\n")
    else:
        Input = input("Enter k:\n")
        while not Input.isdigit():
            Input= input("Enter k:\n") 
    return eval(Input)

#Calculate the factorial
def calc_factorial (Integers):
    nfactorial = 1
    for i in range (1, Integers+1):
        nfactorial *= i        
    return nfactorial

