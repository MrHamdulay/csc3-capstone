""" A program that uses recursive functions to find all palindromic primes between two integers supplied as input Katlego Gaveni 6th May 2014"""


import sys  

from math import *

sys.setrecursionlimit(30000)    


def paliprime(bottom_number, max_number):   #Function that returns palindrome primes by calling the functions prime() and palindrome().
    
    
    if (int(max_number) >= int(bottom_number)): # The stopping condition occurs when the bottom number is greater than or equal to the end of the range which is the  amx number. 
        
        if palindrome(bottom_number):  
            
            if prime(int(bottom_number), floor(sqrt(int(bottom_number)))+1):  
                print(bottom_number) # If the current bottom number is both a palindrome and a prime number, print it.
                
                paliprime(str(int(bottom_number) + 1), max_number)  # This part of the recursive function checks whether the next number above the current bottom number is a palindromic prime by inputting it in the same function.
                
            else:
                paliprime(str(int(bottom_number) + 1), max_number) # If the number is not a prime, it still checks whether the next number above the current bottom number is a palindromic prime by inputting it in the same function.
        
        else:
            
            paliprime(str(int(bottom_number) + 1), max_number)  # If the number is not a palindrome or a prime, it still checks whether the next number above the current bottom number is a palindromic prime by inputting it in the same function.
            
            
            
            
def prime(number, current): # function that checks whether a number is a prime. 
    
    if number == 1:   
        return False
    
    elif current <= 2: # The stopping condition when the current  reaches 2. 
        
        return True 
    
    else:   
        
        if number % (current-1) != 0:   
            
            return prime(number, current-1) 
        else:
            
            return False   #return False if the current is not a prime.


def palindrome(string):  # function checks whether or not the number is a palindrome
    
    if len(string) <= 1: #the stopping condition is when there are less than two characters in the number
        return True 
    
    else: #The return statement makes use of Boolean statements.
       
        return string[:1] == string[len(string)-1:len(string)-2:-1] and palindrome(string[1:len(string)-1]) 
    
   
def main():
    
    start = input("Enter the starting point N:\n")   
    
    end = input("Enter the ending point M:\n")   
    print("The palindromic primes are:")   
    if (start == "" or start == " ") or (end == "" or end == " "): # if input is blank return blank
        print("")
    
    else:
        
        paliprime(start, end)   # The main function that finds the palindromic primes is called with the start and end points of the range inputted as arguements.
  



main()