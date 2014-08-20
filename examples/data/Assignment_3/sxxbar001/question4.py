#Assignment 3
#Question 4
#Barry Su
#25 March 2014
#Program to find all palindromic primes between two integer inputs

N=eval(input("Enter the starting point N: \n"))
M=eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")

import math

def palindrome(number):
    number=str(number)
    if number==number[::-1]:
        return True
    else:
        return False
    
def prime(number):
    prime=True
    for i in range(2,number//2+1):
        if number%i==0:
            prime=False
            break
    return prime

for j in range(N+1,M):
    if j==1:
        continue
    if palindrome(j)==True:
        if prime(j)==True:
            print(j)