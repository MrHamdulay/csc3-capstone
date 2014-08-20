"""CHTGEN002
09/05/2014
Palindromic Primes"""

import sys
sys.setrecursionlimit (30000)

count = 2

def pal(int_input): #function if its a palindrome
    if(int_input==""):
        return True
    else:
        if(int_input[len(int_input)-1] == int_input[0]):
            return pal(int_input[1:len(int_input)-1])
        else:
            return False

def prime(int_input):#function to determine if its prime
    global count
    
    if(int_input==0):
        return True
    
    if(int_input==1):
        return False
    
    if(int_input==count//2):
        return True
    
    else:
        if(count!=int_input and int_input%count==0):
            return False
        else:
            count+=1
            return prime(int_input)
              
def palindromic_prime(n,m): #determine if its both palindrome and prime
    global count
    count=2
    
    if(m<n):
        return 0
    
    elif(pal(str(n)) and (prime(n))):
        print(n)
        return palindromic_prime(n+1,m)
    
    else:
        return palindromic_prime(n+1,m)
    
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

palindromic_prime(n,m)
    
    