"""Program to count palindromic primes between supplied endpoints
thushar hariparsad
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
       
    if num > M:
        return -1
    #if current number is prime refer to is_prime.
    check = check_palindrome(num)
    
    if  check == True:
        div = 2
        return is_prime(num, div)
    #if number is nt a prime check if the next number is a palindrome
    else:
        return refer(num+1)
    
def check_palindrome(num): #check if number is a palindrome
    
    num = str(num) #Convert number to string.
    
    #If a number is a palindrome return True   
    if num[0] == num[len(num)-1] and len(num) <= 3:
        return True
    
    #If the first and last digits of a number are equal when its length is greater than 3,delete the first and last numbers and check the remainder
    elif num[0] == num[len(num)-1]:
        return check_palindrome(num[1:len(num)-1])
    
    #If a number is not a palindrome return False
    else:
        return False
    
def is_prime(num, div): #print number if it is prime
    
    if div <= num**(1/2):
        if num%div == 0:
            return refer(num+1) #If a palindromic number is not a prime find the next palindrome
        else:
            return is_prime(num, div + 1) 
    #If a palindromic number is prime print the number and fine the next palindrome
    else:
        print(num)
        return refer(num+1)
    
if __name__=="__main__":
    refer(num)