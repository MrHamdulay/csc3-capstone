#Recursion to find palindromic primes
#Devaksha Pillay
#4 May 2014

#to use the square root function
import math
#increase recursion limit
import sys
sys.setrecursionlimit (30000)

start = input ("Enter the starting point N:\n")
end = input ("Enter the ending point M:\n")

start = eval(start)
end = eval(end)

def is_palindrome(word):
    #check if a word is a palindrome
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            #remove first and last letter of the string
            return is_palindrome(word[1:-1])
        else:
            return False

def is_prime(number,factor):
    #function to determine whether a number is a prime number
    if number <=1:
        return False
    if factor>math.sqrt(number):
        #if the factor is larger than half the number, it must be a prime number
        return True
    if number%factor == 0 and number > factor:
        #the number would have more than two factors
        return False
    else:
        #continue to check for possible factors
        return is_prime(number, factor + 1)

    
def palindromic_primes(start,end):
    if start == end:
        #check for palindrome
        if is_palindrome(str(start)) == True:
            #check for prime number
            if is_prime(start, 2) == True:
                print(start)
    else:
        if is_palindrome (str(start)) == True:
            if is_prime(start,2) == True:
                print(start)
        #checks for each number within the given range
        return palindromic_primes(start + 1, end)

print("The palindromic primes are:")    
palindromic_primes(start,end)   