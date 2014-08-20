import math
def palindromic_prime():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    
    for i in range(N+1,M):
        y=i
        r=""
        while y!=0:
            r+=str(y%10)
            y=y//10
            if i==int(r):
                for divisor in range(2,i):
                    if i%divisor==0:
                        break
                    if divisor==i-1:
                        print(i)
palindromic_prime()