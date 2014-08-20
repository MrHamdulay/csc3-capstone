#question 3 assignment 5 functions to be imported in to question3.py
#Shane Horsley
#15 April 2014

#function to get integer using method from given program combine
def get_integer(c):
    if c=='n': #if input is "n"
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return n     
    else:
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k) 
        return k

def calc_factorial (v): #function to calculate the factorial of a number
    factorial=1
    for i in range (1, v+1):
        factorial *= i    
    return factorial
    