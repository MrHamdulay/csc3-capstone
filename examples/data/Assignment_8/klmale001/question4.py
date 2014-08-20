"""Palindrome counter
Alexi Kalamoudacos
8 May 2014"""

#Importing sys
import sys
sys.setrecursionlimit (30000)

#ask for endpoints
x = eval(input("Enter the starting point N:\n"))
y = eval(input("Enter the ending point M:\n"))
if x > 1:
    z = x
else:
    z = 2
print("The palindromic primes are:")

def refer(z):
    """Program to refer palindromic numbers to is_prime."""
    
    #end recursion when endpoint is met   
    if z > y:
        return -1
    
    #check if its a plindrome
    tcheck = check_pal(z)
    
    if  tcheck == True:
        div = 2
        return is_prime(z, div)
    #- check if the following number is a palindrome
    else:
        return refer(z+1)
    
def check_pal(z):
    #defining check_pal a palindrome checker
    
    z = str(z) #Convert number to string.
    
    #return true if the number is a palindrome
    if z[0] == z[len(z)-1] and len(z) <= 3:
        return True
    
    #process for palindrome checking
    elif z[0] == z[len(z)-1]:
        return check_pal(z[1:len(z)-1])
    
    #return false if it's not
    else:
        return False
    
def is_prime(z, div):
    #defining prime function
    
    #end recursion if the divisor is greater than 50% the number
    if div <= z**(1/2):
        if z%div == 0:
            return refer(z+1) #looking for prime palindrome
        else:
            return is_prime(z, div + 1) #check if number is divisble by divisor
    #checking if palidromes are prime
    else:
        print(z)
        return refer(z+1)
    
if __name__=="__main__":
    refer(z)