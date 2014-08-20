# Question 4 | Assignment 3
# Author: Julius Stopforth (STPJUL004)
# Date: 20/03/2014

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

def chk_prime(number):
    if number%2 == 0 and (number != 2):
        return False
    for i in range(2,round(number**0.5)+1):
        if number%i == 0:
            return False
    return True

print("The palindromic primes are:")

for i in range(N+1,M):
    if str(i) == str(i)[::-1] and chk_prime(i):
        print(i)
