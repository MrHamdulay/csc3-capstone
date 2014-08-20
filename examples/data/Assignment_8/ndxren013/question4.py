"""reneshan naidoo
ndxren013
7 May 2014"""
import sys, math
sys.setrecursionlimit (30000)

def pal(s):
    s = str(s) #converts the number intoa string
    if len(s) <= 1: #checks the length to see if it is 1 or 0
        return True
    if s[0] != s[-1]: #checks the first and last letters of the string
        return False
    return pal(s[1:len(s) - 1])#cuts off the first and last letters of the string

def prime(n,x):
    if(n==1):
        return False
    if(x <= math.sqrt(n)): # if it is not the srqrt
        if(n%x!=0): #if it is divisible
            return prime(n,x+1) #call function again
        else:
            return False #return not a prime
            
    
def method(n,m): 
    if n<=m:       #while n not equal to n
        if pal(n): #if the number reversed == the number 
            if prime(n, 2)!=False:
                print(n) #prints the number
        method(n+1,m) #calls the method of the next number
        
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
method(n,m)
    
    
    
