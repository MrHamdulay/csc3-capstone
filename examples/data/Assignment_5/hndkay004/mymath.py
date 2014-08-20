#calculating number of k permutations for n numbers
#Kayla Hendricks
#14 April 2014

import math

def get_integer(x):
    print("Enter ",x,":",sep="")
    n=input()                   #so that n fulfills while loop below
    while not n.isdigit():
        print("Enter ",x,":",sep="")
        n = input()
    n=eval(n)                   #so that n can be evaluated as a number for calc_factorial 
    return n

def calc_factorial(n):
    fact = 1
    for factor in range(1,n+1):        #starting with 1 and ending in n, counting in "1"s
        fact*= factor                  #starting at 1, multiply by each number you're working your way through
    return fact
    
