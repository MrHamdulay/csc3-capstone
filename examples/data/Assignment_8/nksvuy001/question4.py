"""program that uses recursive functions to find all palindromic primes between two integers supplied as input (start and end points are included)
vuyolwethu nkosi
4 may 2014"""

import sys
sys.setrecursionlimit (30000)

s_point=eval(input("Enter the starting point N:\n")) #get input from user
e_point=eval(input("Enter the ending point M:\n")) #get input from user
print("The palindromic primes are:") #getting ready to print the palindromic primes
    
import question1 #import question 1 on identifying palindromes, so as to use the same method here, after identifying the prime numbers
import math #will be using math functions
    
def if_prime(s_point,prime_num): #need to define parameters
    if prime_num <2: #if the prime number is less than the number 2 then it is not a prime number ie.False
        return False    
    elif s_point>math.sqrt(prime_num): #if the starting number is greater than the squareroot of the prime number, carry on
        return True
    elif prime_num%s_point!=0: #if the division of the prime number by starting point is not equal to 0, start the function again
        return if_prime(s_point+1,prime_num) #recursive step: eliminating the first number and starting from the next number
    else:
        return False #if conditions are not met, do not execute anything
    
def palindromic_primes(s_point,e_point): #defining the palindromes from the output received from above
    if s_point<=e_point: #if the starting point is less than the ending point ie. Valid range, therefore our Base case
        palindrome=question1.palindrome(str(s_point),0)=="Palindrome!" #defining variable
        if  palindrome: #if it is therefore a palindrome
            if if_prime(2,s_point)==True: 
                print(s_point) #want to print the output for the case each time
        return str(palindromic_primes(s_point+1,e_point)) #recursive step: defining new parameters ie. from the next number
    else:
        return " " #if the string is empty, print an empty string
                    
print(palindromic_primes(s_point,e_point)) #calling function
            

