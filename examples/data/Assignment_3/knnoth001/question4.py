# Program that prints all the Palindromic Primes between two given number included them. 
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 20/03/2014

import math

'''Function that prints every palindromic primes between two numbers which are not included'''

def checkPalindromicPrimes(n,m):
    for nber in range(n+1,m):
        d = math.ceil(math.sqrt(nber))#We ensur that the sart root of the number is an integer
        #If none of the numbers between 2 and the sqrt(number) are divisors of the number then that number is prime
        for i in range(2,d+1): #Take all number between 2 and the square root of the number. 
            if nber%i == 0 and nber!= i: #If we found one divisor of the number it means that it is not a prime number then we go to the next number.   
                break
            if i!=d:#If It's not a divsor, we check if we are at the end of the list, if not we go to the next possible divisor
                continue
            #This line is interpreted only if the number is prime so now we need to check if it's a palindrome
            nber = str(nber)#Convert into string
            if nber[:] == nber[::-1] :#Check if the number is a palindrome and if it's bigger than 9
                print(nber)
                    
n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))            
print('The palindromic primes are:')
checkPalindromicPrimes(n,m)