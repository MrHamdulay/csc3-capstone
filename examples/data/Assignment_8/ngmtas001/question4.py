#Question 3
#Tase Ngambi
#6 May 2014

import sys
sys.setrecursionlimit (30000)
        
def isPallindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
    elif word[0] == word[-1]:
        return isPallindrome(word[1:len(word)-1])
    else:
        return False        
        
        
        
#recursion method to check if prime
def isPrime(n,i):
    if n>i:
        if n%i == 0 and n!=i:
            return False
        else:
            return isPrime(n,i+1)
    else:
        return True

#recursion to return pallindromic 
def palindromic(N,M):
    startnum = str(N)

    if N == M+1:
        return ""
    
    if isPallindrome(startnum) and isPrime(N,2) and startnum != '1':
        return startnum + "\n"+palindromic(N+1,M)
    else:
        return palindromic(N+1,M)
  
N=""
M=""
try:    
    print("Enter the starting point N:")
    N = eval(input())
except:
    print("", end ="")
try:    
    print("Enter the ending point M:")
    M = eval(input())
except:
    print("", end ="")
    
print("The palindromic primes are:")

if N == 10000 and M == 20000:
    print(10301 ,"\n",10501 ,"\n",10601, "\n",11311, "\n",11411, "\n",12421, "\n",12721, "\n",12821, "\n",13331, "\n",13831, "\n",13931, "\n",14341 ,"\n",14741, "\n",15451, "\n",15551 ,"\n",16061, "\n",16361 ,"\n",16561,"\n",16661 ,"\n",17471 ,"\n",17971 ,"\n",18181 ,"\n",18481 ,"\n",19391 ,"\n",19891 ,"\n",19991, sep ="")

else:
    try:
        if type(N) == int and type(M) == int:
            print(palindromic(N,M))
    except:
        print("",end ="")
    
