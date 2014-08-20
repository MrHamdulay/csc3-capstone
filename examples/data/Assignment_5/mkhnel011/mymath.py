"""a program to get integer inputs from a user
nelisile mkhwebane
assignment 5
question 3"""

#get input integers

def get_integer(x):
    if x=="n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n") 
        n=eval(n)
        return n
    if x=="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k=eval(k)
        return k
 
#calculating the factorial of a number

def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial

  
    
    
    
    
    