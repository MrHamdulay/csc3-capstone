import sys
sys.setrecursionlimit (30000)

def rangpali(N,M):
    if pali(str(N)) == True:
        print('ass')
        if prime(pali(N)) == True:
            print(prime(pali(N)))
    else:
        print('ass2')
        return rangpali(N,M+1)
        

N = int(input('Enter the starting point N:\n'))
M = int(input('Enter the ending point M:\n'))    

def pali(x):
    if len(x) < 2: 
        return True
    elif x[0] == x[-1]:
        return pali(x[1:-1])
    else:
        return False
#x = input('Enter a string:\n')  

def prime(n):
    if n == 0:
        return False
    if n == 1:
        return False
    else:
        val1 = n // prime(n - 1)
        if val1 == 0:
            return False
        else:
            return True

rangpali(N,M)