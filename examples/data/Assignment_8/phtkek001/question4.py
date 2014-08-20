"""kekolo phetla
phtkek001"""

import sys
sys.setrecursionlimit(30000)
start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def palin(string,index):
    if len(string)/2 >=index:
        if string[index]==string[-1-index] and palin(string,index+1) == "Palindrome!":
            return "Palindrome!"
        else:
            return "Not a palindrome!"
        
    else:
        return "Palindrome!"
    
import math

def check_prime(start,prime):
    if prime <2:
        return False
    elif start>math.sqrt(prime):
        return True
    elif prime%start!=0:
        return check_prime(start+1,prime)
    else:
        return False
    
def other(start,end):
    if start<=end:
        palindrome=palin(str(start),0)=="Palindrome!"
        if palindrome:
            if check_prime(2,start)==True:
                print(start)
        return str(other(start+1,end))
    else:
        return " "
    
print(other(start,end))
            
         