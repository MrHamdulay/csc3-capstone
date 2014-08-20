'''A program that calculate the factorial ang get integer n and k from the user
Jacob Ntesang
13 April 2014'''

from math import*

#get both interger k and n from tthe user
def get_integer(a):
        if a == "n":
        
                n = input ("Enter n:\n")
                while not n.isdigit (): 
                        n = input ("Enter n:\n") 
                n = eval(n)
                return n

        elif a == "k":
                k = input ("Enter k:\n")
                while not k.isdigit ():
                        k = input ("Enter k:\n")
                k = eval (k) 
                return k
def calc_factorial(n):
        '''this function calculates the factorial of perimeter n and factorial of n-k'''

        #n = eval("n")
        #nfactorial = 1
        #for i in range (1, n+1):
        #        nfactorial *= i      
        #k = input ("Enter k:\n")
        #while not k.isdigit ():
        #       k = input ("Enter k:\n")
        #k = eval (k)
        
        nkfactorial = 1
        for i in range (1, n+1):
                nkfactorial *= i 
        return nkfactorial