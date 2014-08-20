""""program that uses recursive functions to find all palindromic primes between two integers supplied as input 
JP Lanser
3 May 2014"""

import sys
sys.setrecursionlimit (30000)


#First create a function to determine whether a number is prime or not and use recursion
#Use two parameters

# a --> the number that I want to determine whether it is prime or not
# b --> possible factors of the number, starting with 3.
#When using the function, b must initially equal 3. Then it increases by 1 every time. 


import math

def prime(a,b):
    
    if a ==1 or a==0:
        return False
    elif a==2: 
        return True
    
    elif a%2 == 0: #If it is divisible by two it is obviously not prime(besides for two itself)
        return False 
     
    
         
    
    elif b > math.sqrt(a): #Once b gets up to the square root of a, any other value greater than that cannot be a factor, except the number itself obviously       
        return True              
    elif a%b ==0:
            return False     
    else: return prime(a, b+1)
    
 #This is an adaptation to function in question1 to determine whether a number/string is a palindrome
    
def palindrome(string):
    if len(string)<2:
        return True
    if string[0] == string[len(string)-1]:
        return palindrome(string[1:len(string)-1])
    else: return False
  

    
def prime_palindrome(x,y):
    
   
    
    string_x = str(x) #create variable to check if x is a palindrome by converting it to a string
    if x > y:  #If x is greater than y, the whole range between x and y has been covered. It is the base case.
        return
    
    elif prime(x, 3) and palindrome(string_x): #this checks that the number is prime and that it is a palindrome (using above functions). 
                print(x)  #If the above 'if' statement is true print x, as it is a prime palindrome
          #return number 1 greater than x  to prime_palindrome function and keep checking for prime palindromes          
    
    return prime_palindrome(x+1,y) 
            
            
    
    
N= eval(input("Enter the starting point N:\n")) 
M= eval(input("Enter the ending point M:\n")) 
print("The palindromic primes are:")
prime_palindrome(N,M)
    
        
    
    
    
    
    
    
    