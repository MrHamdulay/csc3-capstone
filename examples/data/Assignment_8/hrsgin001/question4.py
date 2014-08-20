#Gina Horscroft
#Question 4
#find all palindromic primes between two integers supplied as input (include start and end points)
import math
import sys
sys.setrecursionlimit(30000)

def reverse(n):
    """reverses a number"""
    n = str(n)
    if len(n)<1:
        return ""
    else:
        return n[len(n)-1] + reverse(n[:len(n)-1])
 
def prime(n, x):
    """checks if number is prime"""
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    else:
        if x < (math.sqrt(n) + 1):
            if n%x == 0:
                return False
            else:
                return prime(n, x+1)
        return True
    
def both(num):
    """checks if number is a palindrome and prime"""
    if (num == int(reverse(num))) and (prime(num, 2)):
        return True
    else:
        return False
    
def pprime(start, end):
    #if start != end:
    if start < end:
        #if number is a palindrome AND if number is prime
        if (both(start)):
            print(start)
        return pprime(start+1, end)
    elif (start == end):#if start equals end
        if (both(start)):
            print(start)
        return pprime(start+1, end)
    else:
        return ""

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
print(pprime(n,m))

