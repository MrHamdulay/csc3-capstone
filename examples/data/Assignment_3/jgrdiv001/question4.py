#program to find palindromes and primes
from math import *
def pal():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    #number=str(number)
    #rpal=number[::-1]
    print("The palindromic primes are:")
    for number in range(N+1,M):
        number=str(number)
        rpal=number[::-1]
        if rpal==number and prime(int(number)):
            print(number)
            
def prime(number):
    if number==2:
        return True
    for i in range(2,number+1):
        if number%i==0: #if it is divisible by i (any number)
            return False
        if (i>=sqrt(number)):
            return True
            
pal()
#i=2
#while i <=number:
#    if number%i!=0:
    