import math
def primepalindrome():
#palindrome    
    N=eval(input('Enter the starting point N:\n'))
    M=eval(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    for i in range(N+1,M):
        reverse=str(i)[::-1]
        reverse=int(reverse)
        if reverse==i:
#prime number
            for divisor in range(2,i):
                if i%divisor==0:
                    break
                if divisor == i-1:
                    print(i)
primepalindrome()                    