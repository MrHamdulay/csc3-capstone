# Program for generating palindromic prime numbers in a given range
# SHZLWA001 CSC1015F

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(N+1,M):
        for j in range(2,i):
                if i%j==0:
                        continue
                else:
        
                        s=str(N)
                        y=s[::-1]
                        a=int(y)
                        if N==a:
                                print(N)
      
        