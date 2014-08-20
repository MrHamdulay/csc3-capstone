"""Palindromic prime finder
Charlie Shang
9 May 2014"""

#Increase the recursion limit in python
import sys
sys.setrecursionlimit (30000)

#Ask for start and end points
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

if N > 1: 
    num = N
else:
    num = 2 #if starting point is less than 2, set as 2 because 1 is not prime

print("The palindromic primes are:")
    
def is_palindrome(num):
    """Determines palindromity of a number (T/F)"""
    
    num = str(num) #Converts a number to a string.
    
    #if the length is < 3 and first character = last character, return true 
    if num[0] == num[-1] and len(num) <= 3:
        return True
    
    #If length > 3, and begin and end matches, delete the first and last character and re-evaluate if it is a palindrome
    elif num[0] == num[-1]:   
        return is_palindrome(num[1:-1])
    
    #Return False if not palindrome.
   
    else:
        return False

def send(num):
    """Sends palindromic numbers to 'is_prime.' """   
      
    if num > M: #Recursion ends when end point is reached 
        return -1
    
    #Check if the current number is a palindrome. If it is, send to is_prime.
    Check = is_palindrome(num)
    if  Check == True:
        div = 2
        
        return is_prime(num, div)
    
    else: #else check if the next num is a palindrome if 'num' is not...
        return send(num+1)
    
def is_prime(num, div):
    """Finds if a number is prime"""
    
    #only repeat if divisor is smaller than num**(1/2)
    if div <= num**(1/2):
       
        if num%div == 0:
            return send(num+1) #if a palindrome is not a prime, return the next palindrome
        
        else:
            return is_prime(num, div + 1) #If number cannot be divided through, increase divisor and repeat.
    
    
    else:#If palindrome and prime, print and find the next palindromic prime by recursion..
        
        print(num)
        return send(num+1)
    
if __name__=="__main__":
    send(num)