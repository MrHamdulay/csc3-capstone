'''This program prints out palindromic primes between two numbers using recursion
Sandile Christopher Mahlangu
5 May 2014'''

import sys
sys.setrecursionlimit (30000)
import question1

import math
divisor=2
def prime(num,divisor):
    '''This function returns True if a number is a prime else false'''
    if num<2:#if the number is less than 2 then it's not a prime
        return False
    elif divisor<=math.sqrt(num):#dividing with numbers upto the square root of that number
        if num%divisor==0:#If there's a remainder then it's not a prime
            return False
        else:
            #if there's no remainder then add one to divisor and recure the function
            divisor+=1
            return prime(num,divisor)
    else: #if no remainders are found return true 
        return True

def pali_prime(N,M):
    '''This function checks if a number between two given numbers is a palindrome, if it is then it checks whther it's a prime or not. If both are true the it prints it out'''
    if N <=M:#Looking at numbers between N and M
        N=str(N)
        check_palindrome=question1.palindrome(N)   #Checking if it is a palindrome using the function from question 1
        if check_palindrome:
            N=eval(N)      #if it's a palindrome then change it back to a number
            
            check_prime= prime(N,divisor)  #Checking if the number is a prime
            if check_prime: #If it is the print that number and recure to the next value
                print(N)
                return pali_prime(N+1,M)
            else:# other wise don't print it but recure to the next number
                return pali_prime(N+1,M)
        else: #If it's not a palindrome the go to the next number
            N=eval(N)
            return pali_prime(N+1,M)
        
if __name__=="__main__":
    N=eval(input('Enter the starting point N:\n'))
    M=eval(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    pali_prime(N,M)