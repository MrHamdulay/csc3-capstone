"""question4.py :- print palindromic primes in a given range
Author : Musa Xakaza
Date : 07/05/2014"""
import math
import sys
import question1
sys.setrecursionlimit (30000)
def isPrime(n,i):
    #check whether a number is a prime number by dividing it with numbers from 2(var i)
    if (n%i==0 and n!=2 and n!=i):
        return False
    else:
        if (i < math.sqrt(n)):
            return isPrime(n,i+1)
        else:
            #if factor is greater than the square root of the number; then the number is a prime
            return True
def isPalindrome(n):
    #convert int to string
    string = str(n)
    #reverse string and compare
    if question1.isPalindrome(string) == "Palindrome!":
        return True
    else:
        return False

def printPalindromicPrimes(x,y):
    #skip one
    if x == 1:
        x += 1
    if x <= y:
        if isPalindrome(x) and isPrime(x,2):
                print(x)
        printPalindromicPrimes(x+1,y)

def main():
    n = eval(input("Enter the starting point N:\n"))
    m = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")    
    dif = m-n
    if dif > 5001:
        u = dif//2
        printPalindromicPrimes(n,m-u)
        printPalindromicPrimes(n+u,m)
    else:
        printPalindromicPrimes(n,m)
    
if __name__=="__main__":
    main()