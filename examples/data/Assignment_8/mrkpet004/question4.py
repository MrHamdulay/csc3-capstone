"""program that uses recursive functions to find all palindromic primes between two integers supplied as input (start and end points are included)
peter m muriuki
9/5/14"""

import sys
sys.setrecursionlimit (30000)

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print ("The palindromic primes are:")

#reverse the numbers
def reverse(string):
    string=str(string) #convert the numbers to strings
    if len(string)==0:
        return string
    else:
        return reverse(string[1:]) + string[0]

#determine whether selected number is a prime using remainder-%
def prm(x):
    if x<2:
        return False 
    else:
        a=(2**x) % x
        b=2 % x    
        if a!=b:
            return False
        else:
            return True    
     
#check for palindromic primes
def pal_prm(N,M):
    # Base case-when starting point is greater than the ending point
    if N>M:
        return 
    # recursive step 
    else:
        get=prm(N) # check for primes in the range given
        if get==True:
            a=int(reverse(N))  #check for reversed prime numbers which are similar to their unreversed values
            if a==N:
                print (N)
        pal_prm (N+1,M) 


pal_prm(N,M)   