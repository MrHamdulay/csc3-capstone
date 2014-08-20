#Assignment 8
#Question 4
#Barry Su
#8 May 2014
#program using recursion to find all palindromic primes between two integers supplied as input

#import system library
import sys
sys.setrecursionlimit(30000)

#get starting and end points
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

def prime(num, count):      #check if the number is a prime
    if num==1:
        return False
    elif count==int(num**(1/2))+1:
        return True
    else:
        if num%count==0:
            return False
        else:
            return prime(num, 1+count)

def reverse(num):               #create a function to reverse the number
    return num if len(num)==1 else num[-1]+reverse(num[:-1])

def palindrome(num):            #check if the number is a palindrome
    if str(num)==reverse(str(num)):
        return True
    else:
        return False

palindromes=""
def palindromePrimes(N, M):
    global palindromes
    if N==M:
        if prime(N, 2) and palindrome(N):
            palindromes+=str(N)
    else:
        if prime(N, 2) and palindrome(N):
            palindromes+=str(N)+'\n'
            palindromePrimes(N+1, M)
        else:
            palindromePrimes(N+1, M)
   
palindromePrimes(N, M)

print("The palindromic primes are:")
print(palindromes)