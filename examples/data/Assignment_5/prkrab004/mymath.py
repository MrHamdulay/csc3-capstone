#Assignment 5
#Question 3
#Rabia Parker 
#Due Date: 17/04/14

#calculating number of k permutations for n numbers

import math
def get_integer(i):
    print("Enter ",i,':',sep='')
    num=input()                   #num needs a value for the while loop
    while not num.isdigit():
        print("Enter ",i,":",sep='')
        num=input()
    num=eval(num)
    return num

def calc_factorial(num):
    factorial=1
    for factor in range(1,num+1):
        factorial*=factor
    return factorial