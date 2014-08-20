#sheldon kisten
#9 may 2014
#palindrome prime numbers

import math
import sys
sys.setrecursionlimit (30000) #allows for higher numbers to be dealt with
def pal(s,test): #takes in the variables s and test as parameters
    if(len(str(s))!=1): #if the number hdoesnt have only one digit, come in
        d=s%10 #this gives the last number 
        test=test+str(d) #adds the last number to test
        return pal((s-(s%10))//10,test) #calls the function again of the number - the last digit
    else:
        return(test+str(s))

def prime(n,x,p):
    if(n==1):
        return (p+"Not")
    sq=int(math.sqrt(n)) #gets the sqrt of function
    if(x!=(sq+1)): # if it is not the srqrt
        if(n%x!=0): #if it is divisible
            return prime(n,x+1,p) #call function again
        else:
            return (p+"Not") #return not a prime
            
    
def method(n,m): 
    if n<=m:       #while n not equal to n
        tespPal=int(pal(n,"")) # calls the pal function
        if tespPal==n: #if the number reversed == the number 
            testPrime=prime(n,2,"") #calls the prime function
            if testPrime!="Not":
                print(n) #prints the number
        method(n+1,m) #calls the method of the next number
        
        
if __name__== "__main__":
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    method(n,m)
    
    
    