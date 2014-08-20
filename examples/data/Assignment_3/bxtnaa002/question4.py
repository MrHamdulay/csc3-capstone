# quetsion4.py
# find all palindromic primes between two integers supplied as input
# author: bxtnaa002

import math
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(N+1,M):
    num = str(i)
    rev = (str(i)[::-1])
    if rev == num:
        test=False
        j=2
        while j < i:
            if i%j==0: 
                test=False
                break
            
            else:
                test=True
            j+=1
        else:
            test=True
        if test==True:
            print(i)
    else:
        continue    
        
    