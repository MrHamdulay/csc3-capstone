# A program to find all the palindromic primes between two integers supplied as input
# Author: Afika Nyati
# Date: 21 March 2014

def paliprime(N,M):
    
    print("The palindromic primes are:")
    
    N = int(N) + 1 # This makes sure the starting number is excluded as required by the question
    
    while N < M: # This loop checks all numbers in the range of N and M (excluding M)
        
        N = str(N)# Converts N into a string
        reverse = N[::-1] # Reverses the number as a string
        
        if reverse == N: # This is the check for a palindrome. If not a palindrome, it won't check whether its a prime number.
            N = int(N)
                          
            if N < 2: # A prime is not 0 or 1
                N+=1
                continue                           
            elif N == 2: # 2 is a prime number
                print(N, end = "\n")
                N+=1
            if N == 3: # 3 is a prime number
                print(N, end = "\n")
                N+=1                 
            elif N % 2 == 0: # Checks for even numbes. No even number is a prime.
                N+=1
                continue
            else:            
                
                for i in range(3, int(N**0.5) + 2, 2): # Checks to see if number has any factors
                    if N % i == 0: break
                else: # This is only done if a number gets through the factor check loop without a break
                    print(N, end = "\n")
        N = int(N) + 1
                        

def main():
    
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    
    paliprime(N,M)
    
    
main()