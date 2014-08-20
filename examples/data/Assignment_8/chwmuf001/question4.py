import math
import sys
sys.setrecursionlimit (30000)

def testprime(N,M,count):
    
    if N == M+1 :
        return False
    elif N==2 or N==3:
        answer(N)
        return testprime(N+1,M,2)
    elif N<2:
        return testprime(N+1,M,2)
    elif N>3:
        #print('hjgjh',N)
        if N % count !=0:
            if count<=round(math.sqrt(N)) +1:
                return testprime(N,M,count+1)
            else:
#return testprime(N+1,M,2) + palindrome(N) 
                answer(N)
                return testprime(N+1,M,2)
        
        elif N%count==0:
            return testprime(N+1,M,2)
    
def answer(value):
    #if type(value)!='str':
    #    value=str(value)
    ans=palindrome(value)
    if ans:
        print(value)
    
    
    
def palindrome(phrase):
    phrase=str(phrase)
    
    if len(phrase)%2!=0:
        if len(phrase) == 1:
            return True
        elif phrase[0] == phrase[len(phrase)-1]: 
            return palindrome(phrase[1:len(phrase)-1])
        else:
            return False
    else:
        if len(phrase) == 0:
            return True
        elif phrase[0] == phrase[len(phrase)-1]: 
            return palindrome(phrase[1:len(phrase)-1])
        else:
            return False

N = eval(input("Enter the starting point N:\n"))        
M = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
testprime(N,M,2)