"""Question 4: Prints a list of palindromic prime numbers between two numbers
Galya Wolov
9 May 2014"""


#import functions and libraries needed
import sys
import math
sys.setrecursionlimit(300000)
def palindrome (x): #just reusing question 1: look at previous comments
    if len(x) == 0 or len(x) ==1:
        return True
    
    if x[0] == x[len(x)-1]:
        return  palindrome(x[1:(len(x)-1)])

    else:
        False
      

def prime(n,m):
    if n <=1: #less than or = 1 not prime
        return False
    elif n==2:#2 is prime
        return True
    elif n%m== 0:#they would be divisble ther4 cannot happen not prime
        return False
    elif n%m !=0 and m!=2:
        return prime(n,m-1) #is prime because no matter what not giving divisble by other and not even either
    elif (n % 2 != 0): #not even could be prime 
        return True
    elif n%m == 0: #would have divisor
        return False
        
N=eval(input("Enter the starting point N:\n")) #starting and end points
M=eval(input("Enter the ending point M:\n"))
def paliprime(N,M):
   if N > M:
    return '' #Starting point is greater than end point does not work returns empty string and recursion breaks down.
    
   else: 
        if prime(N,int(math.sqrt(N))+1)== True and palindrome(str(N))== True:#checks if true 4 both statements if so then it is palindormic prime
                return '\n' +str(N) + paliprime(N+1,M) #recursive goes onto next number in I
        else:
            return paliprime(N+1, M) #continues recursion to find one
        
    
print("The palindromic primes are:", paliprime(N,M), sep='', end='') #print statement
    
