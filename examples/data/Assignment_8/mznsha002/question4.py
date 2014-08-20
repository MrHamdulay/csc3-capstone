# 8 May 2014
# Shaun Muzenda
# A program that uses recursive functions to find all palindrome primes between two integers supplied as input (start and end points are included)

import math
import sys
sys.setrecursionlimit (30000) 

def palindrome(s,test): # checking if the number is a palindrome
    
    if(len(str(s)) != 1): # checks whether the number has more than one character
        d = s%10 
        test = test+str(d) 
        
        return palindrome((s-(s%10))//10,test) 
    else:
        return(test+str(s))

def prime(starting_point,x,p):   #checking whether the number is a prime
    if(starting_point == 1):
        return (p+"Not")
    
    sq = int(math.sqrt(starting_point)) 
    
    if(x != (sq+1)): 
        
        if(starting_point % x != 0):   
            return prime(starting_point,x+1,p) 
        else:
            return (p+"Not") 
            
    
def method(starting_point,ending_point): 
    
    if starting_point <= ending_point: #is      
        tesppalindrome = int(palindrome(starting_point,"")) 
        
        if tesppalindrome == starting_point: 
            testPrime = prime(starting_point,2,"") 
            
            if testPrime != "Not":
                print(starting_point) #prints a list of the palindrome primes
                
        method(starting_point+1,ending_point) 
        
        
if __name__== "__main__":
    
    starting_point = eval(input("Enter the starting point N:\n"))
    ending_point = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    method(starting_point,ending_point)