"""Program to count palindromic primes between supplied endpoints.
Kemeshan Naicker
7 May 2014"""

#Increase number of recursions that python will allow
import sys
sys.setrecursionlimit (30000)

#Prompt user for endpoints
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
if N > 1:
    num = N
else:
    num = 2
print("The palindromic primes are:")

def refer(num):
    """Program to refer palindromic numbers to is_prime."""
    
    #Set recursion to terminate when the specified ending point is reached.    
    if num > M:
        return -1
    
    #Check if the current number is a palindrome. If it is, refer to is_prime.
    tcheck = check_pal(num)
    
    if  tcheck == True:
        div = 2
        return is_prime(num, div)
    #- if not, check if the successive number is a palindrome.
    else:
        return refer(num+1)
    
def check_pal(num):
    """Function to determine if a number is a palindrome."""
    
    num = str(num) #Convert number to string.
    
    #If a number is a palindrome, rreturn True   
    if num[0] == num[len(num)-1] and len(num) <= 3:
        return True
    
    #If the first and last digits of a number are equal when its length is > 3,
    #strip the end digits away analyse the resulting number.
    elif num[0] == num[len(num)-1]:
        return check_pal(num[1:len(num)-1])
    
    #If a number is not a palindrome, return False
    else:
        return False
    
def is_prime(num, div):
    """Function to print a number if it is prime."""
    
    #Set recursion to terminate if the divisor is more than half palindromic number
    if div <= num**(1/2):
        if num%div == 0:
            return refer(num+1) #If a palindromic number is not a prime, find the
        #next palindrome.
        else:
            return is_prime(num, div + 1) #If number is not divisible by the divisor,
        #increase the divisor and recurse.
    #If a palindromic number is prime, print the number and fine the next palindromic
    #number.
    else:
        print(num)
        return refer(num+1)
    
if __name__=="__main__":
    refer(num)