import math
def isPrime(n):
     for i in range(2,int(math.sqrt(n))+1):
          if (n%i==0):
               return False
     return True
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(n+1,m,1):
     z=str(i)
     r=z[::-1]
     if r==z :
          if isPrime(i):
               print(i)