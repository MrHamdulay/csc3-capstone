#Question 4
#Palindromic prime numbers
#By: Dean de Haast

import sys
import math
sys.setrecursionlimit (30000)
global count
count =1

N = input("Enter the starting point N:\n")
M =input("Enter the ending point M:\n")
# Adding one to the end point so that it is included
M=eval(M) + 1
print("The palindromic primes are:")

def reversal(N):
  if N=="":
    return N

  return reversal(N[1:]) + N[0]

# The function that checks if it is a palindrome
def palindrome(N,M):
  global count
  count = 1
  #Convert to a string for the slicing
  N=str(N)
  M=str(M)
  
 
  if N == M:  #Checking if the values are equal if yes it must stop the program 
    return print("", end="")
  elif N == reversal(N):  #Checking if the number is the same backwards as forwards
    prime(N)  #Only checks if it is a prime number if it is a palindrome
        
  N=int(N)
  M=int(M)
  return palindrome(N+1,M) # Recursive step sends a new N with the value of one more

# The function that checks if it is a prime number
def prime(N):
  N = int(N)
  global count
  if N == 1:
    print("", end ="")
  elif N ==2:
    print(N)
    
  elif N%2 == 0:  #Checks if it is divisable by two.
    print("", end ="")  
  
  elif count < (math.sqrt(N)): # Checks to see that the count is smaller than the square root of the number
    count+=1
    if N%count == 0:  # Checks if N is divisable by count
      print("", end ="")
    else:
      prime(N)  # Calls the function again until N is divisable by count or until count is = square root of N
   
  else:
    print(N)
  
palindrome(N,M)  