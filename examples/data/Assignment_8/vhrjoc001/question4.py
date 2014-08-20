#vhrjoc
#question4 assignment 8
#a program that uses recursive functions to find all palindromic primes between two integers supplied as input.

import sys
sys.setrecursionlimit (30000)
#copied question one and used its function
def isPalindrome(s):

    # base case: the empty string and the string with # only one character are both palindromes

            if (len(s) <= 1):

                        return True

    # recursive case: a string whose middle section (everything but # its first and last characher) is a palindrome, and whose first # and last characters are equal, is a palindrome

            elif (isPalindrome(s[1:-1]) and s[0] == s[-1]):

                        return True 

            else:

                        return False
            

def prime(n, d): # function created to find the primes in the range of inputed numbers
            if n == 1:
                        return False
            elif n%d == 0 and n>d:
                        return False
            elif n**0.5>d and n>d:
                        return prime(n, d+1)
            return True
def palprime(n, m): #function to then check of the prime numbers which are palindromic
            if n==m:
                        return  
            
            if isPalindrome(str(n)) == True:
                        if prime(n,2) == True:
                                    print(n)
                                    return palprime(n+1,m)
                        else:
                                    return palprime(n+1,m)
            else:
                        return palprime(n+1,m)
            
            
            
n = eval(input("Enter the starting point N: \n"))
m = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
palprime(n, m+1)



#start of question4

