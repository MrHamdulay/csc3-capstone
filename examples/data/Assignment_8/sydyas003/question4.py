#Yaseen Sayed Ismail
#SYDYAS003
#09/05/2014
#Palindromic primes

import sys
sys.setrecursionlimit (30000)

#Check palindrome
def palindrome(a):
    if(a==""):
        return True
    else:
        if(a[0]==a[len(a)-1]):
            return palindrome(a[1:len(a)-1])
        else:
            return False
#Check prime
count=2
def prime(a):
    global count
    if(a==0):
        return True
    if(a==1):
        return False
    if(a==count//2):
        return True
    else:
        if(a%count==0 and count!=a):
            return False
        else:
            count+=1
            return prime(a)
        
#Check palindromic prime       
def palindromic_prime(n,m):
    global count
    count=2
    if(n>m):
        return 0
    elif(prime(n) and palindrome(str(n))):
        print(n)
        return palindromic_prime(n+1,m)
    else:
        return palindromic_prime(n+1,m)
    
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromic_prime(n,m)
    
    