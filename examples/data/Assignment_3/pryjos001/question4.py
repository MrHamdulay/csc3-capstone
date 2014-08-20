#Program to output palindromic prime numbers

import math

n = eval(input("Enter the starting point N:\n"))

#while n<11:
#    n = eval(input("Enter your starting point:\n"))

m = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for num in range(n+1,m):
    prime = True
    for i in range (2,round(math.sqrt(num))+1):
        if num%i==0:
            prime=False
    if prime==True:
        if str(num)==(str(num)[::-1]):
            print (num)