

import sys
sys.setrecursionlimit (30000)
sys.setrecursionlimit (30000) 



def palindrome(t,test): 
    if(len(str(t))!=1): 
        d=t%10 
        test=test+str(d) #palindrome fnctn
        return palindrome((t-(t%10))//10,test) 
    else:
        return(test+str(t))


import maths 



def primenumber(n,x,p):
    if(n==1):
        return (p+"Not")
    sq=int(math.sqrt(n)) #prime num fnctn
    if(x!=(sq+1)): 
        if(n%x!=0): 
            return primenumber(n,x+1,p)
        else:
            return (p+"Not") 
            
    
def process(n,m): 
    if n<=m:      
        tespPal=int(palindrome(n,"")) 
        if tespPal==n:
            testPrime=primenumber(n,2,"") 
            if testPrime!="Not":
                print(n) 
        process(n+1,m) 
        
        
if __name__== "__main__":
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    process(n,m)