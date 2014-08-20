# krwane001

import math

n=int(input("Enter the starting point N:\n"))
m=int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(n+1,m):
    s=str(i)
    if all(i%j!=0 for j in range(2,int(math.sqrt(i))+1)):      
        if (s == s[::-1]):
            print(s) 
    
    