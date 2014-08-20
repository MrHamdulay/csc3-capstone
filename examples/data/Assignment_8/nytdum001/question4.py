"""Program to find all palindromic primes between two integers
Dumisani J Nyathi 
09-05-2014"""

import sys
sys.setrecursionlimit(10000000)

def prime_check(A,B):
    if B==A:
        return True
    elif B<2:
        return False
    elif B%A==0:
        return False
    else:
        return prime_check(A+1,B)#recalls prime_check

#function checks if palin is prime    
def palin_primes(string):
    if string == '':
        return True
    elif (ord(string[0]) == ord(string[len(string)-1])):
        return palin_primes(string[1:len(string)-1])#recalls palin_primes
    else:
        return False

#function to check for palindrome
def palin_check(N,M):
    if M+1==N:
        print("")
    else:
        if prime_check(2,N):#invokes function to check if number is prime
            if palin_primes(str(N)):#invokes function to check if palin is prime
                print(N)
            return palin_check(N+1,M)
        else:
            return palin_check(N+1,M)#recalls palin_check
        
def main():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palin_check(N,M)
    #main function will run and then invokes function which will check for palindrome
main()