'''Program to encrypt messages using recursion
Tinotenda Chemvura CHMTIN004
03 May 2014'''

import sys
sys.setrecursionlimit (30000)

#__________________________Program Starts Here__________________________________

#check if ita a palindrome
#if palindrome, check if prime
#if prime, print

#function that returns True if the number is a palindrome, similar to the function in question 1
def check_Palindrome(number):
    number = str(number)
    if len(number) == 1 or len(number) == 0:
        return True
    #the recursive step, if the 1st digit of the number == last digit, return the number with the 1st and last digit sliced off
    elif number[0] == number[-1]:
            return check_Palindrome(number[1:-1])
    #if the number does not meet the above conditions, return false
    else:
        return False

#Function that checks if the number is a prime number and returns 0 if its not and 1 if it is
def check_prime(number):
    global i
    if number == 0:
        i = 2
        return False
    if number == 1:
        i = 2
        return False
    elif i < number and number % i == 0:
        i = 2
        return False
    elif i <= number and number % i != 0:
        i += 1
        return check_prime(number)
    else:
        i = 2
        return True
    
#funtion to print the palinndromic primes

def print_numbers(number,stop):
    if number == stop+1:
        return False
    elif check_Palindrome(number):
        if check_prime(number):
            print(number)
            return print_numbers(number+1,stop)
        else:
            return print_numbers(number+1,stop)
    else:
        return print_numbers(number+1,stop)    

i = 2 # to be used by the check_prime function
start = eval(input("Enter the starting point N:\n"))
stop = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
print_numbers(start,stop)

#___________________________Program Ends Here___________________________________