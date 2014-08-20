
#palindrome
#Tofunmi Olagoke
#OLGMOF001
import math

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def ifprime(x):
    ifprime=True
    for i in range(2,x//2+1):
        if x%i==0:
            ifprime=False
            break
    return ifprime
def ifpalindrome(a):
    a=str(a)
    if a==a[::-1]:
        return True
    else:
        return False
    
for y in range(N+1,M):
    if y==1:
        continue
    if ifpalindrome(y) == True:
        if ifprime(y) == True:
            print(y) 
        
        
                                        
                        
                        
                                
                                        

        
        
                                
