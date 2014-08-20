"""assignment 9 question 4
shannon clacey
8 may 2014"""

import math
import sys #import functions to be used in program

sys.setrecursionlimit(300000)

start = eval(input("Enter the starting point N:\n"))#get starting and end points
end = eval(input("Enter the ending point M:\n"))

def prime(a,b): #function to check prime numbers
      if a==2: #2 is a prime number
            return True
      else:
            if a < 2: #number less than 2 cant be a prime 
                  return False
            elif a==2:
                  return True #as above
            else:
                  if a%b == 0: #not prime because divisle by number other thsan 1 or itself
                        return False
                  elif a%b!= 0 and b!= 2: # above statement doesnt hold,check against number 1 less than y
                        return prime(a,b-1)
                  elif b%a!= 0 and b==2: #number is prime
                        return True
def palindrome(string): #creates funciton (this has been imported from question 1)
    if len(string) == 1 or len(string) == 0: #checks for single character or empty string
        return True #returns true if it is 
    elif string[len(string) -1]==string[0]: # checks if first and last letters are the same
        return palindrome (string[1:len(string)-1])
    else: #checks if neither of the above cases hold and the string is as a result not a palindrome 
        return False

def palindromeprime(start,end): #function to check if both other functions return true
      if start > end:
            return "" #return empty string when "N" gets to M (always adding 1)
      else:
            if palindrome(str(start))==True: #checking palindrome
                  if prime(start,int(math.sqrt(start))+1)==True: #checking prime
                        return '\n' + str(start) + palindromeprime(start+1,end)
                  else:
                        return palindromeprime(start+1,end) #above indented statement not met, check next number (n+1)
            else:
                  return palindromeprime(start+1,end) #original statement not met return (n+1)
                      
print("The palindromic primes are:",palindromeprime(start,end),sep='',end='')

    

