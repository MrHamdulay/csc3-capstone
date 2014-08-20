#Ariel Rubin
#RBNARI001
#program to calculate palindrome prime numbers recursively
#9 May 2014

#import functions that will be used in program
import sys 
import math
sys.setrecursionlimit(300000)

#get starting and end points of numbers
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

#function that checks for prime numbers
def primenumber(x,y): 
#2 is a prime number      
      if x==2: 
            return True
      else:
            #any number less than 2 cant be a prime 
            if x < 2: 
                  return False
            elif x==2:
                  return True 
            else:
                  #not a prime because divisle by a number other than 1/itself
                  if x%y == 0: 
                        return False
                  #statement doesnt hold, check against number 1 less than y
                  elif x%y!= 0 and y!= 2: 
                        return primenumber(x,y-1)
                  #number is a prime
                  elif y%x!= 0 and y==2: 
                        return True

#function to check if both other functions are true
def ispalindromeprime(N,M): 
#returns an empty string when N gets to M (always adding 1)     
      if N > M:
            return "" 
      else:
            #checking palindrome
            if isPalindrome(str(N))==True: 
                  #checking prime
                  if primenumber(N,int(math.sqrt(N))+1)==True: 
                        return '\n' + str(N) + ispalindromeprime(N+1,M)
                  else:
                       #above indented statement not met, check next number (n+1) 
                        return ispalindromeprime(N+1,M) 
            else:
                  #original statement not met return (n+1)
                  return ispalindromeprime(N+1,M) 

#function to determine if a string is/is not a palindrome
def isPalindrome (word):
      if len (word) == 1 or len (word) == 0:
            return True
      #check to see if 1st and last letters are equal
         #if yes then checks runs the function again for 2nd letter and 2nd last letter
         #will continue to run until each letter has beenchecked correctly      
      if word[0] == word[-1]:
            if isPalindrome (word[1:-1]) == True:
                  return True
            else:
                  return False            
      else:
            return False
            #prints out all the palindromic primes
print("The palindromic primes are:",ispalindromeprime(N,M),sep='',end='')
