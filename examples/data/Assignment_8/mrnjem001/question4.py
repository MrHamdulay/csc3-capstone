"""Question 4 - check for palindrome prime
Jembe Moran
11 May 2014"""
import sys
sys.setrecursionlimit (30000) #increase recursion limit
       
def check_palindrome(n):
        global primes
        global m
        global i
        i=2 #reset i
        if n==(m+1): #if lower bound > upper bound, stop
                return primes
        if str(n)==reverse(n) and (check_prime(n) is True): #check if n reversed is n and n is a prime
                primes+=str(n)+"\n" #add prime to list
                check_palindrome(n+1) #check next number
        else: check_palindrome(n+1)


def check_prime(n):
        global i
        if n==i: #end recursion
                return True
        if (n % i == 0 and n>i): #therefore not a prime
                return False
        if n>i:
                i = i + 1
                return check_prime(n) #continue check for prime
        
def reverse(n): #reverse string
        n=str(n)
        if n=="":
                return n
        else:
                return(reverse(n[1:])+n[0])
i=2        
primes=""
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
check_palindrome(n)
print("The palindromic primes are:\n", primes, sep="")