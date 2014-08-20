# Shane Horsley
# Program to check whether numbers are palindromic primes
# 5 May 2014
import sys #import functions to be used in program
import math
import question1
sys.setrecursionlimit(300000)
N = eval(input("Enter the starting point N:\n"))#get starting and end points
M = eval(input("Enter the ending point M:\n"))

def prime(x,y): #function to check prime numbers
      if x==2: #2 is a prime number
            return True
      else:
            if x < 2: #number less than 2 cant be a prime 
                  return False
            elif x==2:
                  return True #as above
            else:
                  if x%y == 0: #not prime because divisle by number other thsan 1 or itself
                        return False
                  elif x%y!= 0 and y!= 2: # above statement doesnt hold,check against number 1 less than y
                        return prime(x,y-1)
                  elif y%x!= 0 and y==2: #number is prime
                        return True

def palindromeprime(N,M): #function to check if both other functions return true
      if N > M:
            return "" #return empty string when "N" gets to M (always adding 1)
      else:
            if question1.palindrome(str(N))==True: #checking palindrome
                  if prime(N,int(math.sqrt(N))+1)==True: #checking prime
                        return '\n' + str(N) + palindromeprime(N+1,M)
                  else:
                        return palindromeprime(N+1,M) #above indented statement not met, check next number (n+1)
            else:
                  return palindromeprime(N+1,M) #original statement not met return (n+1)
                      
print("The palindromic primes are:",palindromeprime(N,M),sep='',end='')

    
