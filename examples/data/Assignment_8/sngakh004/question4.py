"""Program to count palindromic primes between supplied endpoints.
Akhil Singh
SNGAKH004
7 May 2014"""

import sys

sys.setrecursionlimit (30000)


starting_point= eval(input("Enter the starting point N:\n"))
ending_point = eval(input("Enter the ending point M:\n"))
if starting_point > 1:
    number = starting_point
else:
    number = 2
print("The palindromic primes are:")

def reference(number):
    if number > ending_point:
        return -1
    
    full_check = check_palindrome(number)  

    if  full_check == True:
        divisor = 2
        return is_prime(number, divisor)
            #- if not, check if the next number is a palindrome.
    else:
        return reference(number+1)     
    
def check_palindrome(number):
    """Function to determine if a number is a palindrome."""
    
    number = str(number) #Converting a number to a string.
    
    #If the number is a palindrome then it will return True   
    if number[0] ==number[len(number)-1] and len(number) <= 3:
        return True
     #If the first and last digits of a number are equal when its length is > 3,
       #strip the end digits away analyse the resulting number.
    elif number[0] == number[len(number)-1]:
        return check_palindrome(number[1:len(number)-1])
       
    #If a number is not a palindrome, return False
    else:
        return False
        
    

def is_prime(number, divisor):
    """Function to print a number if it is prime."""
    
    #Set recursion to terminate if the divisor is more than half palindromic number
    if divisor <= number**(1/2):
        if number%divisor == 0:
            return reference(number+1) #If a palindromic number is not a prime, find the
        #next palindrome.
        else:
            return is_prime(number, divisor + 1) #If number is not divisible by the divisor,
    #increase the divisor and recurse.
    #If a palindromic number is prime, print the number and fine the next palindromic
    #number.
    else:
        print(number)
        return reference(number+1)
    


        
  
    
                
if __name__=="__main__":
    reference(number)            