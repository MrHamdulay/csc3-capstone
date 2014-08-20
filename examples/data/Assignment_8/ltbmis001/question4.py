"""Checks palindromic primes between two values
mishka latib
07 may 2014"""

import sys
sys.setrecursionlimit (30000)

import math

def palin_prime(start, end, div, P, t):
    
    if start==("") and end==(""):
        return("")
        
    elif div==-1 and start!=(""):
        start = eval(start)
        end = eval(end)
        div = (int(math.sqrt(start))+1)
        t = str(start)
        return palin_prime(start, end, div, P, t)
    elif start!=("") and start<=end:
        #checks palindrome
        if t!="pal":
            if len(t)==1:
                return palin_prime(start, end, div, P, "pal")
            elif len(t)==2:
                if t[0]==t[1]:
                    return palin_prime(start, end, div, P, "pal")
                if t[0]!=t[1]:
                    start+=1
                    div = (int(math.sqrt(start))+1)
                    t = str(start)
                    return palin_prime(start, end, div, P, t)                    
            elif len(t)>2:
                if t[0]==t[-1]:
                    #starts from either end of string, works towards centre to check if characters match to produce palindrome
                    return palin_prime(start, end, div, P, t[1:-1])
                if t[0]!=t[-1]:
                    start+=1
                    div = (int(math.sqrt(start))+1)
                    t = str(start)
                    return palin_prime(start, end, div, P, t)        
        if t=="pal":
            #checks prime
            if start==2:
                P+=("2\n")
                start+=1
                div = (int(math.sqrt(start))+1)
                t = str(start)
                return palin_prime(start, end, div, P, t)
            elif start==11:
                P+=("11")
                start+=1
                div = (int(math.sqrt(start))+1)
                t = str(start)
                return palin_prime(start, end, div, P, t)                
            elif start<2:
                start+=1
                div = (int(math.sqrt(start))+1)
                t = str(start)
                return palin_prime(start, end, div, P, t) 
            elif div==1:
                P+=(str(start)+"\n")
                start+=1
                div = (int(math.sqrt(start))+1)
                t = str(start)
                return palin_prime(start, end, div, P, t)            
            elif start%div==0 and div!=1:
                start+=1
                div = (int(math.sqrt(start))+1)
                t = str(start)
                return palin_prime(start, end, div,P, t)
            elif start%div!=0:
                div-=1
                return palin_prime(start, end, div, P, t)
            
    
    #prints output
    print("The palindromic primes are:\n"+P)
            
            
#gets user input and places input into function
start = input("Enter the starting point N:\n")
t = str(start)
end = input("Enter the ending point M:\n")
palin_prime(start, end, -1, "", t)
