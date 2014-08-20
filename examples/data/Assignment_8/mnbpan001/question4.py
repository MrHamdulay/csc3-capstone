"""Program to check for palindromic prime numbers within a range (uses 3 recursive functions)
Pankaj Munbodh
7 May 2014"""

import sys
sys.setrecursionlimit (30000)
import math                   #to perform square root
def palprime(a,b):
    global counter            #Use a global variable to avoid error in prime(n,x). When prime executes the first time, the appropriate range is assigned to x.
    counter=0
    if a==b:                    # Stopping case for palprime (the last number of range is reached).
        if prime(a,1)=='prime':   #Note prime can have an arbitrary value as its second argument since it will be re-assigned when prime is executed.
            if palindrome(str(a))==str(a):
                pass                        #Since number is already printed when prime is executed, a 'pass' statement is used (nothing more needs to be printed)
                
    else:
        prime(a,1)
        palprime(a+1,b)       #recurse over whole range of numbers
counter=0
n=100000                      #create variable n to avoid NameError when calculating range for x
def prime(n, x):              #To check if a number n is prime.  
    global counter
    if counter==0:
        x=range(2,round(math.sqrt(n))+1)
    if n==2:                       #Exception case when n is 2
        print(n)
        return 'prime'
    if len(x)==0:                  #Stopping case: n has been divided by all numbers in the required range except by its rounded square root.  
        counter=1
        z=n%round(math.sqrt(n)) 
        if z==0:
            
            return 'not prime'
        else:
            if palindrome(str(n))==str(n):           #To check if number is palindromic, use palindrome function
                print(n)
            return 'prime'
            
    else:
        counter=1
        y=n%x[0]
        if y==0:
            
            return 'not prime'
        else:
            return prime(n,x[1::])

def palindrome(string):
    if string=='':
        return''              #stopping case
    rev_str=string[len(string)-1]+palindrome(string[:-1])   #take last character and put it at beginning. Continue recursing to add characters.          
    
    return rev_str    
        
#Input from user. Here exception handling is used to avoid getting errors if user does not type anything as input.
try :
    c=int(input("Enter the starting point N:\n"))
    d=int(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palprime(c,d)    
except ValueError:
    try :
        d=int(input("Enter the ending point M:\n"))
    except ValueError:
        pass
    



