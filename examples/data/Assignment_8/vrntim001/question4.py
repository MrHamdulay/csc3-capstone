'''' palindromic primes (recursion)
Tim Mostert
06.05.14'''

import sys
sys.setrecursionlimit (30000)

# turns N into a string and checks for palindrome using recursion
def palindrome(N,M,Plist,rate):
    K = str(N)[rate:(len(str(N))-rate)]
    if N != M+1:
        if len(K) < 2:
            Plist.append(N)
            rate = 0
            palindrome(N+1,M,Plist,rate)
        elif K[0] != K[-1]:
            rate = 0
            palindrome(N+1,M,Plist,rate)
        elif K[0] == K[-1]:
            palindrome(N,M,Plist,rate+1)
    return Plist 

# checks remainder of number from 2 to (number -1), if none of them = 0 prints number
# has exceptions for 0,1, and auto makes 2 a prime
def prime(number,counter):
    if number == 0 or number == 1:
        False
    elif number == 2:
        print(number)
    elif number%counter != 0 and counter == number-1:
        print(number)
    elif number%counter == 0:
        False
    else:
        prime(number,counter + 1)

# checks if both palindrome and prime        
def Palindromeprime(Plist):
    if len(Plist) == 0:
        return
    prime(Plist[0],counter)
    Palindromeprime(Plist[1:])
    
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
rate = 0
Plist = []
counter = 2
palindrome(N,M,Plist,rate)
Palindromeprime(Plist)





