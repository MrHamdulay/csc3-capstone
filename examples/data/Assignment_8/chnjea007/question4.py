# A8Q4
import sys
sys.setrecursionlimit (30000)
import math

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
index = 0
primeIndex = 2

def isPrime(i):
    global primeIndex
    if i == 2:
        return True
    if i % primeIndex == 0 or i == 1:
        return False
    primeIndex += 1
    if primeIndex <= math.ceil(math.sqrt(i)):
        return isPrime(i)
    return True


def isPalindrome(s, index):
    
    if len(s) == 1:
        return True
    if (index >(len(s)//2)-1):
        return True
    else:
        if s[index] == s[len(s) - 1 - index]:
            return isPalindrome(s, index+1)
        else: 
            return False
           

def main():
    global n
    
    global primeIndex
    primeIndex = 2
    
    
    if isPrime(n) == True:
        if isPalindrome(str(n), 0) == True:
            print(n)
    n+=1
    if n<=m:
        main()
print("The palindromic primes are:")
main()