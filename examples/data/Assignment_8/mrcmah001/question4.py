#mahdi marcus

import math 
import sys 
sys.setrecursionlimit (30000) #make the limit greater


def pa(a,b): #variables to see if it works
    if(len(str(a))!=1): #checking if the string has more than one char
        c=a%10
        b=b+str(c)
        return pa((a-(a%10))//10,b)     
    else:
        return(b+str(a))
    
def pr(n,q,p): #prime function
    if n==1:
        return (n,"not")
    sqrt=int(math.sqrt(n))
    if (q!=(sqrt+1)):
        if (n%q !=0):
            return pr(n,q+1,p)
        else:
            return (p+"not")
        
def both(n,m):
    if n<=m:
        fetchPa=int(pa(n,""))
        if fetchPa==n:
            fetchPr=pr(n,2,"")
            if fetchPr!="not":
                print(n)
        both(n+1,m)
            
if __name__=="__main__":
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    both(n,m)
      
 