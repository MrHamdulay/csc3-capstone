"""program that uses recursive functions to find all palindromic primes between two integers supplied as input 
Thiloshni Moodley
9 May 2014"""

import sys
sys.setrecursionlimit (50000)

#User asked for boundry values
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
if N > 1:
    number = N
else:
    number = 2
print("The palindromic primes are:")

def link(number): #function to link palindromic number to function is_prime   
    if number > M: #recursion ends when ending point reached
        return -1
    check = check_palindrome(number) #If number is palindrome, link to function is_prime
    
    if  check == True:
        divisor = 2
        return is_prime(number, divisor)
    else:
        return link(number+1)
    
def check_palindrome(number): #Function to check if number is a palindrome
    number = str(number) #Convert number to string.
      
    if number[0] == number[len(number)-1] and len(number) <= 3:
        return True #Returns true if the number is a palindrome
    
    elif number[0] == number[len(number)-1]:
        return check_palindrome(number[1:len(number)-1])
    
    else:
        return False #Return false if number is not a palindrome
    
def is_prime(number, divisor): #Function that prints number if it is a prime number
    if divisor <= number**(1/2): #recursion ends when divisor is more than half palindromic number
        if number%divisor == 0:
            return link(number+1) #If a palindromic number is not a prime, find the next palindrome
        else:
            return is_prime(number, divisor + 1) 
    else:
        print(number)
        return link(number+1)
    
if __name__=="__main__":
    link(number)