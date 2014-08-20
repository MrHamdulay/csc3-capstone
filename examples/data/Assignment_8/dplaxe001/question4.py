""" Program to print palindrome prime numbers between a start and end value 
Axel du Plessis
09/05/2014"""

import sys
sys.setrecursionlimit (30000)

def prime(number,divisor):
    if divisor == 0:
        return False
    elif divisor == 1 or divisor == 1:
        return True
    if number%divisor == 0:
        return False
    else:
        divisor -= 1
        return prime(number,divisor)
    
def palindrome(message):
    if len(message)==0 or len(message) == 1:
        return True
    if message[0]==message[-1]:
        return palindrome(message[1:-1])
    else:
        return False

def palinPrime(start, end):
    num = start
    if num == end+1:
        print("",end="")
    else:
        if prime(num,(num-1)) and palindrome(str(num)):
            print(num)
            return palinPrime((start+1),end)
        else:
            return palinPrime((start+1),end) 
        
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palinPrime(start, end)    