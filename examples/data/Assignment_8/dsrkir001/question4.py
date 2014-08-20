#Program that uses recursive functions to find all palindromic primes between two integers supplied as input 
#Kiran Desraj - DSRKIR001
#5 May 2014

import math 

#increase the amount of recursion that Python will allow

import sys
sys.setrecursionlimit (30000)

#function to determine if prime

def prime_number(a,b,c):
    if(a==1):
        return (c+"Not")
    number = int(math.sqrt(a)) 
    
    if(b!=(number+1)): 
        
        if(a%b!=0): 
            
            return prime_number(a,b+1,c) 
        else:
            return (c + "Not") 

#function to determine if palindrome

def palindrome(x,y): 
    
    if(len(str(x))!=1):
        
        last=x%10 
        
        y=y+str(last) 
        
        return palindrome((x-(x%10))//10 , y) 
    else:
        return(y+str(x))




#function that combines palindrome and prime to produce required output

def calc(N,M): 
    if N <= M:       
        pal = int(palindrome(N,'')) 
        
        if pal == N: 
            
            prime = prime_number(N,2,'') 
            if prime != "Not":
                
                print(N) 
        calc(N+1,M) 




if __name__== "__main__":
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print('The palindromic primes are:')
    calc(N,M)