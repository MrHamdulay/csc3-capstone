"""ASSIGNMENT 8 QUESTION 4- PRINT PALINDROMIC PRIMES RECURSIVELY
EMMA JORDI
8 MAY 2014"""

import sys
sys.setrecursionlimit(30000)


#define prime function
import math
def prime(number, divisor=2):
        
        if number== 1:
                return False
        
        if divisor>math.sqrt(number):
                return True
        
        if number % divisor==0:
                return False
        else:
                return prime(number, divisor+1)

#copy palindrome function
def palindrome(string):
        
        if len(string) < 1:
                return True
        else:
                if string[0] == string[-1]:
                        return ( palindrome (string[1:-1]))
                else:
                        return False           


start=0
end=0
#function that returns palindromic primes. takes prime(number) and palindrome(number)
def numbers(start, end):
                 
        if prime(start)!= False and palindrome(str(start))==True:
                print(start) #prints out the palindromic primes
        if start==end:
                return        
        numbers(start+1,end)
        
def main():
        start= eval(input("Enter the starting point N:\n"))
        end = eval(input("Enter the ending point M:\n"))

        print("The palindromic primes are:")
        numbers(start, end)
main()
            