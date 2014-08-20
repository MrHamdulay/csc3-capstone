import math
import sys
sys.setrecursionlimit(30000)

def isPrime(n,i):
    if (n%i==0 and n!=2 and n!=i):
        return False
    else:
        if (i<math.sqrt(n)):
            return isPrime(n,i+1)
        else:
            return True
def ispalindrome(n):
    if len(n) == 1:
        return True
    else:
        if len(n) > 1 :
            if  n[0] == n[-1]:
                if len(n[1:-1]) == 0: return ispalindrome(' ')
                else: return ispalindrome(n[1:-1])                
                return ispalindrome(n[1:-1])
            else :
                return False
        else:
            return False

def printValue(start, end):
    if start <= end:
        if ispalindrome(str(start)) == True:
            if isPrime(start,2)  == True:
                print(start)
            printValue(start+1,end)
        else:
            printValue(start+1,end)
    else:
        pass

start = eval(input('Enter the starting point N:\n'))
end   = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
if (end-start) > 5000:
    d = (end - start)//2
    printValue(start,end-d)
    printValue(start+d,end)
else:
    printValue(start,end)