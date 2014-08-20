#Program to calculate the number of k-permutations of n items
#Keanon Fell
#15 April 2014

import math

#Defining the modules that would help to calculate the amount of permutations
def get_integer(p):
    print('Enter ',p,':',sep='')
    n = input()
    while not n.isdigit():
        print("Enter ",x,":",sep="")
        n = input()
    n=eval(n)                   
    return n 
    
def calc_factorial (x):
    product = 1
    for i in range(1,x+1):
        product = product * i
    return product