"""This program finds the palindromic primes between two integers
Hebert Tema
TMXTHA006
04 May 2014"""


import sys
sys.setrecursionlimit(30000)

def reverse(N):
    """recursive function that reverse number"""
    string=str(N)
    if string=="": return ""
    elif len(string)==1:
        return string[0]
    else:
        return  reverse(string[1:]) + string[0]
    
def palindrome2(N):
    """checks for palindromic numbers not divisible by 2 and grater than or equal to 2"""
    if N>=2 and N==int(reverse(N)) and N%2==1 or N//2==1:   #the palindome returned is not divisible by 2 and is more than or equal to 2
        return N
        
def divisible(N, divisor=3):
    if N//2>=divisor:                                   #possible values to divide are in the lower half
        if N%divisor: return divisible(N, divisor+2)
        else:
            return True

def palin_prime(N, M):
    """retuns all the prime numbers from the supplied list of palindromes"""
    if N<=M:                  
        call=palindrome2(N)        
        if call:                  #N is palindromic, not divisible by 2(except 2)
            if not divisible(N):  #N is palindromic prime
                print(N)          
        return palin_prime(N+1,M) #check a value afre N


#get the input from the user
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

#call the palindrome and palin_prime functions
if N<=M:
    print("The palindromic primes are:")
    palin=palin_prime(N, M)