import math
import sys
sys.setrecursionlimit(30000)

start= eval(input('Enter the starting point N:\n'))
end=eval(input('Enter the ending point M:\n'))
checker = 2            

def primecheck(N,checker):
    if N==1:
        return 0
    elif N == checker:
        return True
    elif N%checker == 0:
        return False
    else:
        return primecheck(N,checker +1)
    
def poliprime(start):
    def backward(start):
        start = str(start)
        if start=='':
            return ''
        
        else:
            return backward(start[1:]) + start[0]
        
    if end<start:
        return ''
    

    elif start == 0:
        return ''
        
    else:
        if  str(start)==backward(start) and primecheck(start,2)==True:
            print(start)
        return poliprime(start+1)
    
def main():
    print('The palindromic primes are:')
    poliprime(start)
    
main()