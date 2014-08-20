#Assignment 3
# Question4
import math

def prime(x):
    prime=True
    for i in range(2,x//2+1):
        if x%i==0:
            prime=False
            break
    return prime
def palindrome(x):
    x=str(x)
    if x==x[::-1]:
        return True
    else:
        return False
    
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M):
    if i==1:
        continue
    if palindrome(i) == True:
        if prime(i) == True:
            print(i) 
        
        
                                        
                        
                        
                                
                                        

        
        
                                
