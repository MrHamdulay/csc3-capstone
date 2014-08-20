"""Assignment 8, Question 4
Tejasvin Bagirathi BGRTEJ001
program to find palindromic primes between two integers"""

import sys
sys.setrecursionlimit (30000)

#Prompt user for start and end point
start_pt = eval(input('Enter the starting point N:\n'))
end_pt = eval(input('Enter the ending point M:\n'))

#Special case in the event 1 is selected as the start point, as one is not a prime
if start_pt > 1:
    x = start_pt
else:
    x = 2


print("The palindromic primes are:")

def pal_to_prime (x):
    #Function which uses prime check and is_pal in conjunction to check if palindrome and prime
    if x > end_pt:
        return -1
    #Check if the number is a palindrome; if palindrome, check if it's prime
    check = is_pal(x)
    if  check == True:
        divisor = 2
        return prime_check(x, divisor)
    #If not prime, check if next number is a palindrome
    else:
        return pal_to_prime(x+1)    
    
def prime_check(x, divisor):
    #Function to check if the number is prime
    #If the divisor is greater than half the number, stop the recursion
    if divisor <= x**(1/2):
        if x%divisor == 0:
            #If the number is not prime, check the next palindrome
            return pal_to_prime(x+1) 
        else:
            #If the number is not divisible by the given divisor, increase the divisor
            #And recurse again
            return prime_check(x, divisor + 1)
    #If the number is prime, print the number and move to next number
    else:
        print(x)
        return pal_to_prime(x+1)    

def is_pal(x):
    #Function to check if number is palindrome
    #Convert num to string
    x = str(x)
    #If the first and last charcter are the same and the length is less than 3
    #then it must be a palindrome
    if x[0] == x[len(x)-1] and len(x) <= 3:
        return True
    #If the first and last charcter are the same and the length is greater than 3
    #then strip away the first and last characters and recurse the function
    elif x[0] == x[len(x)-1]:
        x = x[1:len(x)-1]
        return is_pal(x)
    #If not a palindrome, return false
    else:
        return False
    
pal_to_prime(x)    
    
    
    