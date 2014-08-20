#Mymath: Use of functions
#Galya Wolov
#16 April 2014

#creating a function that gets an integer to use in later functions
def get_integer(arg):
    n= input("Enter" +" "  +arg + ":\n") #this is used so that no matter the literal, called upon later arg is replaced
    while not n.isdigit ():
            n = input ("Enter" + " "+ arg + ":\n")
    n = eval (n) #returns as a number!
    return n

#creating a function that calculates the factorial 
def calc_factorial (arg):
    n = int(arg) #this ensures that what is placed is actually an integer
    nfactorial=1
    for i in range (1, n+1): #loop creates the active making of the basis of the factorial 
        nfactorial *= i 
    return nfactorial #returns the factorial 
        
    