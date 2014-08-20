"""program to find all palindromic primes between two intergers supplied as input using recursion
vicky stark
8 may 2014"""

import sys
sys.setrecursionlimit (30000) #given by instructions for assignemnt- it increases amount of recusion allowed

def palindrome_and_prime(start, finsih):
    if start>finsih:
        return ""
    else:
        if real_prime(start) and palindrome(start):
            return str(start) + '\n'+ str(palindrome_and_prime(start+1, finsih))
        else:
            return str(palindrome_and_prime(start+1, finsih))

def real_prime(number):
    
    if number<=1:
        return False
    else:
        return prime(number, number-1)
    
def prime(number_,number): 
   
    if number==1:
        return True
    else:
        if number_%number == 0:
            return False
        else:
            return prime(number_,number-1)
        
def palindrome(strings): 
    strings=str(strings)
    if len(strings) == 1 or len(strings) ==0: 
        return True
    elif strings[0]==strings[len(strings)-1]: 
        return palindrome(strings[1:len(strings)-1])
    else:
        return False 



start=eval(input("Enter the starting point N:\n"))
finish=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:\n"+palindrome_and_prime(start, finish))