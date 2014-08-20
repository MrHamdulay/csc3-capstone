#Aniq Hartle
#09/05/2014
#find palindromic primes between two int

import sys
import math
sys.setrecursionlimit (30000)

'''reverses input string'''
def reverse(word):
    word = str(word)
    if word == "":    #if the function has reached the end of the input string
        return word
    else:
        return (reverse(word[1:])+word[0])
    
'''determines prime or not prime'''    
def isPrime(n,div=2):
    if n==1:
        return False
    elif div>math.sqrt(n):
        return True
    elif (n%div)==0:
        return False
    else:
        div+=1
        return isPrime(n,div)

'''determines and returns palindromic primes between two int'''
def palinPrime(start, end):
    if start!=end:       #if there is more than 1 character present
        if start==int(reverse(start)) and isPrime(start):#if the number is a palindrome
            return str(start) + "\n" + palinPrime(start+1,end)
        else:
            return palinPrime(start+1,end) 
        
    else:
        if isPrime(start) and start==int(reverse(start)):
            return str(start)
        else:
            return ""
        
#take in input from user and enter into palinPrime method, print result                
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
print(palinPrime(N,M))