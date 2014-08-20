#MKXTAT001 TATO MOAKI
#ASSIGNMENT 8 question4
#Program to print palindromic primes in an interval

import sys
sys.setrecursionlimit (30000)

def reverseNumber(num):
    """function returns a reversed number"""
   
    if num % 10 == num:
        return str(num)    
    else:        
        return str(num % 10) + reverseNumber(num//10)#reverse string  
    
def check_prime(M, N):
    """function returns boolean value for a prime number"""
    if N == 1:
        return True
    else:
        if M % N == 0:
            return False
        else:
            return check_prime(M , N - 1)    
        
def palindromes(F,M):
    """function prints palindromic primes in an interval"""       
    if F == M:
        if check_prime(M, M//2):
            if str(M) == reverseNumber(M):
                print(M)
    elif F < 3:
        print("2")
        palindromes(F+2, M)
    elif F >= 3:
        if check_prime(F, F//2): #number is prime
            
            if str(F) == reverseNumber(F):                
                print(F)
                return palindromes(F+1, M)#recurse until the interval is reached
            else:
                return palindromes(F+1, M)
        else:
            return palindromes(F+1, M)
    

def main():
    start = int(input("Enter the starting point N:\n"))
    end = int(input("Enter the ending point M:\n"))
    
    print("The palindromic primes are:")
   
    palindromes(start,end)
    
    
if __name__=="__main__":
    main()