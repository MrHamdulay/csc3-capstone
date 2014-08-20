#Lauren de Bruyn: DBRLAU003
#Recursive function to search for palindromic primes in a list of numbers
#9 May 2014

import sys
sys.setrecursionlimit(30000)

#prompt user for range
start= eval(input("Enter the starting point N: \n"))
end= eval(input("Enter the ending point M: \n"))

print("The palindromic primes are: ")

#check if range starts above 1
if start>1:
    x=start
else:
    x=2

#check if number is palindromic and prime    
def pal_prime(x):
    if x > end:
        return -1
    palindrome = is_pal(x)
    if palindrome == True:
        d= 2
        return is_prime(x, d)
    else:
        return pal_prime(x+1)
    
#check if number is prime
def is_prime(x, d):
    
    if d <= x**(1/2):
        if x%d == 0:
            return pal_prime(x+1)
        else:
            return is_prime(x, d+1)
    else:
        print(x)
        return pal_prime(x+1)
        
#check if number is a palindrome
def is_pal(x):
    x= str(x)
    if x[0] == x[len(x)-1] and len(x) <= 3:
        return True
    elif x[0] == x[len(x)-1]:
        x=x[1:len(x)-1]
        return is_pal(x)
    else:
        return False

pal_prime(x)