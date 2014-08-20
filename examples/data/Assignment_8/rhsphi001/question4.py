'''Phillip Ruhesi
05/05/2014
program to check palindrome and prime'''
import math
import sys
sys.setrecursionlimit (30000)
def palindrome(N):
    N=str(N)
    if len(N)<2:
        return True
    elif N[0]==N[-1]:
        return palindrome(N[1:-1])         
    else:
        return False
    
def checkall(N,M):
    if N==M+1:
        return
    elif N==1:
        N=2
        if palindrome(N)==True:         #Check if palindrome then prime and print the number using the other functions
            if prime(N,2)==True:
                print(N)
                return checkall(N+1,M)        
    else:
        if palindrome(N)==True:
            if prime(N,2)==True:
                print(N)
        return checkall(N+1,M)

def prime(N,dividor):    
    if dividor>math.sqrt(N):            #Run until the dividor is greater then the square root of the number
        return True
       
    elif N%dividor==0:
        return False                    #When N%dividor=0  the number has a factor
    else:
        return prime(N,dividor+1)
    
    



def main():
    N=eval(input('Enter the starting point N:\n'))
    M=eval(input('Enter the ending point M:\n'))    
    print('The palindromic primes are:')
    checkall(N,M)
    
main()

