
"""Tofunmi Olagoke
5 May 2014
Programme  that finds all palindromic primes between two integers supplied as input"""
import math
import sys
sys.setrecursionlimit (30000)

def tester(N,M,count):
    
    if N == M+1 :
        return False
    elif N==2 or N==3:
        answer(N)
        return tester(N+1,M,2)
    elif N<2:
        return tester(N+1,M,2)
    elif N>3:
        if N % count !=0:
            if count<=math.sqrt(N):
                return tester(N,M,count+1)
            else:
                answer(N)
                return tester(N+1,M,2)
        
        elif N%count==0:
            return tester(N+1,M,2)
    
def answer(innput):
    ans=palin(innput)
    if ans:
        print(innput)
    
    
    
def palin(phrase):
    phrase=str(phrase)
    
    if len(phrase)%2!=0:
        if len(phrase) == 1:
            return True
        elif phrase[0] == phrase[len(phrase)-1]: 
            return palin(phrase[1:len(phrase)-1])
        else:
            return False
    else:
        if len(phrase) == 0:
            return True
        elif phrase[0] == phrase[len(phrase)-1]: 
            return palin(phrase[1:len(phrase)-1])
        else:
            return False

N = eval(input("Enter the starting point N:\n"))        
M = eval(input("Enter the ending point M:\n"))


        
print("The palindromic primes are:")
tester(N,M,2)