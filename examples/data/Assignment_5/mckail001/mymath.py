#Ailsa Mackay: MCKAIL001
#Assignment 5 
#Question 1: Program to simulate BBF
#2014-04-15

import math
def get_integer(nofk):
    if nofk=="n":
        n=input("Enter n:\n")
        while not n.isdigit(): #accounts for strings in n
            n=input("Enter n:\n")
        n=eval(n)
        return n #users input returned
    else:
        k=input("Enter k:\n")
        while not k.isdigit(): #accounts for strings in k
            k=input("Enter k:\n")
        k=eval(k)        
        return k #users input returned

def calc_factorial(n):
    factorial=1
    for i in range(1, n+1): 
        factorial*=i
    return factorial #returns calculated permutations