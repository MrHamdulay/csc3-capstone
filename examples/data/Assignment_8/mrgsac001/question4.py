"""Palindromic Primes
Sachin Murugan
9/5/2014"""
import sys
sys.setrecursionlimit (30000)#increases limits
sys.setrecursionlimit (30000) 


def PalindromePrime(x,check): 
#create a base case
    if(len(str(x))!=1): 
        m=x%10 
        check=check+str(m) 
        return PalindromePrime((x-(x%10))//10,check) 

    else:
        return(check+str(x))



#determine prime numbers


def PrimeNumber(n,q,r):
    if(n==1):
        return (r+"Not")

    sqroot = int(math.sqrt(n)) 
    if(q!=(sqroot+1)): #checks to see if integer is a prime
        if(n%q!=0): 
            return PrimeNumber(n,q+1,r)
        else:
            return (r+"Not") 
            
#run through start and end points   
def Run(n,t): 
    if n<=t:      
        CheckPalindrome=int(PalindromePrime(n,"")) 
        if CheckPalindrome==n:
            CheckPrime=PrimeNumber(n,2,"") 
            if CheckPrime!="Not":
                print(n) 
        Run(n+1,t) 
        
        
if __name__== "__main__":
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    Run(n,t)
