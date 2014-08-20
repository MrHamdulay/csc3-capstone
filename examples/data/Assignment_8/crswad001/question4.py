'''Wade Cresswell
Question 4'''
import sys
import math
sys.setrecursionlimit(300000)
SP = eval(input("Enter the starting point N:\n"))
EP = eval(input("Enter the ending point M:\n"))

def checkpalinprime(sp,ep): #function to check if palindromic and prime
   if sp > ep:
      return '' #return empty string when the starting point = ending point
   else:
      if checkpalindrome(str(sp))==True: #if number palindromic
         if checkprime(sp,int(math.sqrt(sp))+1)==True: #and number prime
            return '\n' + str(sp) + checkpalinprime(sp+1,ep) # return the number and then check the next number with same endpoint
         else:
            return checkpalinprime(sp+1,ep) #else check next number
      else:
         return checkpalinprime(sp+1,ep) #else check next number
               
def checkprime(x,z): #function to check if number is prime
      if x==2:
         return True
      else:
         if x < 2: #if number less than 2, number is not prime 
            return False
         elif x==2:
            return True
         else:
            if x%z == 0: #if number divisible y number less than it, not prime
               return False
            elif x%z!= 0 and z!= 2: #if number is not divisible by checker number, check x against next checker number (z)
               return checkprime(x,z-1)
            elif z%x!= 0 and z==2: #if all recursion conditions are met, number prime
               return True
def checkpalindrome(x): #function to check if input string is a palindrome
      if len(x) == 1 or len(x) ==0:
         return True #return true if palindrome
      elif x[0]==x[len(x)-1]:
         return checkpalindrome(x[1:len(x)-1]) #if first character equal to last, splice and return cut string
      else:
         return False  #if it doesnt succeed, is not palindrome
print('The palindromic primes are:',checkpalinprime(SP,EP),sep='',end='') #print numbers