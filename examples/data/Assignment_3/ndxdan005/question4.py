N=eval(input("Enter the starting point N:\n"))

M=eval(input("Enter the ending point M:\n"))
       
print("The palindromic primes are:")

import math
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def reverse(n):
    n=str(n)
    n_2=n[::-1]
    if n==n_2:
        return True
    else:
        return False

K=N

while N<M:
    
    reverse(N)
    is_prime(N)

    if reverse(N) and is_prime(N) and N!=K:
        print(N)
    
    N+=1