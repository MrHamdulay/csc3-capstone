"""making a program that will run in question 3
   kevin kumasamba 
   15 April 2014"""

# define get_integer(a) which has to return a number by having n as a parameter
# get_integer(a) has to return a number that someone has typed in
# get_integer has to be the function that asks for the input 
# if you create an input assignment function that runs outside the functions
# then it runs continuosly and overwrites n and k
def get_integer(a):
    if a=="n":
        b = input ("Enter n:\n")
        while not b.isdigit ():
                b = input ("Enter n:\n")
        return eval(b)
    elif a=="k":
        c = input ("Enter k:\n")
        while not c.isdigit ():
                c = input ("Enter k:\n")    
        return eval(c)  
    
# working out the factorial of the numbers n and k
def calc_factorial(a):
        nfactorial = 1
        for i in range (1, a+1):
            nfactorial *= i
        return nfactorial
            

          
    



