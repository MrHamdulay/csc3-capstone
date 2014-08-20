"""nasha somoina meoli
program to check for palindroic primes
9th may 2014"""
import sys
sys.setrecursionlimit (30000)

def reverse(string):
    #reverse the string
    string=str(string)
    if string == "":
        return string
    else:
    
        return reverse(string[1:]) + string[0]
together=[]    
 
    
import math
def divisibility(M):
    #use Fermat's Little Theorem for Primality
    if M==2:
        return 1

    if (2**(M-1))%M != 1:
        return 0
    
    else:
        return 1
def prime_numbers(M,N):
    # print numbers that are prime and palindromic
    M= int(M)
    N= int(N)
    x = 2
    if M > N:
        return
    else:
        y = divisibility(M)
        if y == 1 :
            
            z = int(reverse(M))
            if z == M:
                print(M)
            
        prime_numbers(M+1,N)
            
            
        #return divisibility
#check if the reversed value is equal to the previous one
M = input("Enter the starting point N:\n")
N = input("Enter the ending point M:\n")
print("The palindromic primes are:")
prime_numbers(M,N)