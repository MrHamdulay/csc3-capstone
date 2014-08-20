# SLLMOG004
#Question 1 of Assignment 3

import math 

starting_point=eval(input("Enter the starting point N:\n"))
ending_point=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def prime(number):
    if number%2==0 and number>2:
        return False
    for i in range(3,number,2):
        if number%i==0:
            return False
    return True

for k in range(starting_point+1,ending_point):
    x=str(k)
    y=x[-1::-1]
    if (x==y):
        if prime(k)==True:
            print(k)