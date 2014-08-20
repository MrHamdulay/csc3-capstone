#Author: NLXALE001
#Date: 15 April 2014
#Assignment 5

#first function adapting for any value inputted
def get_integer(b):
    print ("Enter ", b, ":", sep="")
    a = input ()
    while not a.isdigit ():
        print ("Enter ", b, ":", sep="")
        a = input ()
    a = eval (a)
    return a

#second funtion adapting for any input value 
def calc_factorial(c):
    nfactorial = 1
    for i in range (1, c+1):
       nfactorial *= i 
    return nfactorial
    