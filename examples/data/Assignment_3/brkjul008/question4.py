n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

import math

for i in range(n+1,m):
    for r in range (2,round(math.sqrt(i))+1):
        if i%r==0: break
    else: 
        if str(i)==str(i)[::-1]:
            if i!=1:
                print(i)
            else: continue
        else: continue
        