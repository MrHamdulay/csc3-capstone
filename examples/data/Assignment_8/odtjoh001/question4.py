import sys
import math
sys.setrecursionlimit (30000)

def prime(n,i):
    if n < 2:
        return False
    else:
        if i >= round(math.sqrt(n))+1:
            return True
        elif n > 1:
            if n % i == 0:
                return False
            else:
                return prime(n,i+1)
        else:
            return False
        
def palindrome(num):
    
    if len(num) == 1 or len(num) == 0:
        return True
    elif len(num) == 2 and num[0] == num[len(num)-1]:
        return True
    elif num[0] == num[len(num)-1]:
        return palindrome(num[1:len(num)-1])
    else:
        return False
    
def palindromicPrimes(l, u):
    num = l
    if prime(num,2) == True:
        if  num <= u :
            if palindrome(str(num)) == True:
                print(num)
                return palindromicPrimes(num+1,u)
            else:
                return palindromicPrimes(num+1,u)
    else:
        return palindromicPrimes(num+1,u)
            
        
                                
N = eval(input("Enter the starting point N:\n"))         
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:") 
palindromicPrimes(N ,M )