""" A program that uses recursive functions to find all palindromic primes between two integers supplied as input (start and end points are included).
Author: Afika Nyati
Date: 5th May 2014"""


import sys  # This library is included to increase the amount of recursion that Python will allow.

from math import *

sys.setrecursionlimit(30000)    # This sets the recursion limit to 30 000.



def paliprime(bottom_number, max_number):   # A recursive function that finds all palindromic primes between two integers supplied as input (start and end points are included). It takes in two arguements, the start and end point of the range.
    
    
    if (int(max_number) >= int(bottom_number)): # The stopping condition occurs when the bottom number reaches the top number. The bottom number is changed throughout the function.
        
        if palindrome(bottom_number):  # Checks whether the number is a palindrome by placing it in a recursive function that checks for palindromes.
            
            if prime(int(bottom_number), floor(sqrt(int(bottom_number)))+1):   # Check whether is it also a prime by placing it in the recursive function that checks whether a number is a prime. It requires one to input the number and the square root of the number (plus 1).
                
                print(bottom_number) # If the current bottom number is both a palindrome and a prime number, print it.
                
                paliprime(str(int(bottom_number) + 1), max_number)  # This part of the recursive function checks whether the next number above the current bottom number is a palindromic prime by inputting it in the same function.
                
            else:
                paliprime(str(int(bottom_number) + 1), max_number) # If the number is not a prime, it still checks whether the next number above the current bottom number is a palindromic prime by inputting it in the same function.
        
        else:
            
            paliprime(str(int(bottom_number) + 1), max_number)  # If the number is not a palindrome or a prime, it still checks whether the next number above the current bottom number is a palindromic prime by inputting it in the same function.
            
            
            
            
def prime(number, current): # A recursive function that checks whether a number is a prime. It takes wo arguements. The first arguement is the number that we are checking for a prime number status. The second arguement is the square root of the number, which is used to determine is any number under it is a factor of the number.
    
    
    if number == 1:    # The number one is not a prime number.
        return False
    
    if current <= 2: # The stopping condition occurs when the current number reaches two. It will only reach two if it has not found a factor from all the checks of numbers it has had.
        
        return True # If it reaches two, the number is a prime and it returns True.
    
    else:   # This is where the number checked against all the numbers under it to see if it has any factors.
        
        if number % (current-1) != 0:   # If the current number is not a factor of the original number:
            
            return prime(number, current-1) # Check whether the number under the current number is a factor of the original number, by recalling the function.
            
        else:
            
            return False   # If the current number is a factor of the original number, the original number is not a prime number. Therfore return False.


def palindrome(string):  # A recursive function that checks whether in input is a palindrome. It returns True or False.
    
    if len(string) <= 1: # The stopping condition occurs when there are ony two letters left in the string.
        
        return True # True is always returned once the stack reaches this point.
    
    else: # This is is where the main part of the function occurs. The return statement makes use of Boolean.
       
        return string[:1] == string[len(string)-1:len(string)-2:-1] and palindrome(string[1:len(string)-1]) 
    
    # This section of the function returns back a Boolean result depending on the condition. The condition check whether the first letter of the string is equal to the last letter. If they are equal, it evaluates True, and the rest of the string is sliced and placed in the function. Once all the conditions of the end letters of the string are evaluated, there will be a long Boolean operation of Boolean results, using 'and'. AND is equivalent to multiplication, therefore if there is one False (equivalent to zero) in the operation, the final Boolean will return False, but if all the letters matched, it will return True.
    
    
    
    
def main():
    
    start = input("Enter the starting point N:\n")    # Asks user for the start point of the range.
    
    end = input("Enter the ending point M:\n")    # Asks user for the end point of the range.
    
    print("The palindromic primes are:")    # Prints out a heading
    
    if (start == "" or start == " ") or (end == "" or end == " "): # If the input is only a blank space or nothing: Do nothing.
        print("")
    
    else:
        
        paliprime(start, end)   # The main function that finds the palindromic primes is called with the start and end points of the range inputted as arguements.
  



main()