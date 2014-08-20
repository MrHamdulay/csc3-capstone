def palchk(x):
    if str(x) == str(x)[::-1]: return True

def primechk(x):
    for i in range (2, x):
        if x % i == 0:
            return False
    else: return True
    
N = eval (input ('Enter the starting point N:\n')) + 1
M = eval (input ('Enter the ending point M:\n'))
print ('The palindromic primes are:')
for i in range (N, M):
    if primechk(i) and palchk(i): print (i)