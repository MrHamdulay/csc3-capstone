"""  find all palindromic primes between two integers supplied as input
barak setton
05/05/2014"""

import math
import sys
sys.setrecursionlimit (30000)

def paltest(s):
    
    s = str(s)
    if len(s)==1: # telling when to stop
        return s
    else:
        return (paltest(s[1:])+s[:1]) # making issue smaller

def F(n,e):
   
    def f(m,count):            # function that checks if the number is a prime number
        if count>math.sqrt(m): # making the numbers to check smaller. reduce amount of recurtion
            return True
        elif m%count ==0:      # checking if the number is devisibal by a nother number
            return False
        else:
            return f(m,count+1)# returning the next number to check
    
    if n>e:                    # stoping the recurtion
        print("",end="")       # doing nothing
    elif n==1:
        return F(n+1,e) 
    elif f(n,2) and n == eval(paltest(n)): # sending number to function that checks if its a palidrom and if it a prime number
        print(n)                 # print the number if it is
        return F(n+1,e) 
    else:
        return F(n+1,e)   # returning the next number if it is not 
        
        
s = eval(input("Enter the starting point N: \n"))
e = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
F(s,e)
