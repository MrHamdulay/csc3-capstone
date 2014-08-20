#Assignment 5, Question 
#LYLON002
#15 April 2014

def get_integer(x):
        k = input ("Enter " + x + ":\n")
        while not k.isdigit ():
                k = input ("Enter " + x + ":\n")        #get the integer until valid answer
        k=eval(k)
        return k

def calc_factorial(z):
        factorial = 1
        for i in range(1,z+1):
                factorial = factorial*i                 #calculate the factorial
        return factorial
        