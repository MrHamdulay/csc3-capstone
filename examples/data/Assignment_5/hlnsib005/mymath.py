"""Name: Sibulele Hlongwane
Date: 13 April 2014
module containing two functions to get an integer and calculate factorial: Assignment 5"""

import mymath
#Function to only get an integer from user input and checks whether it is a valid integer
def get_integer(string):
    a=string
    string = input ("Enter"+ ' '+ a +":\n")
    
    while not string.isdigit ():
        string= input ("Enter"+' '+ a +":\n")
   
    string = eval (string)  
    return(string)
#Calculate factorial by inputted parameter(n)
def calc_factorial(par):
    nfactorial = 1
    for i in range (1, par+1):
        nfactorial *= i
    return(nfactorial)
#print ("Number of permutations:", nfactorial // nkfactorial)