#THOMAS WHITEHEAD
#WHTBAS001
#15-04-2014
#CSC1015F 
#ASSIGNMENT 5
#QUESTION 3

#get_integer receives a name for a specific prompt and returns an inputted
#integer 

def get_integer(a): 
    a = eval(input(str("Enter " + a + ":\n")))
    return a

#loop to calculate a factorial n! (a definite loop multiplying itself from 1 to n)
#it returns the factorial of said number. 
def calc_factorial(x):
    xfactorial = 1
    for i in range (1, x+1): #shift up one from 0 index
        xfactorial *= i #multiplies each successive term
    return xfactorial #output of function is the factorial of the input x