from math import sqrt, ceil

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:") 

for i in range(N+1,M):
    if i%2 == 0 and  i != 2:
        continue    
    else:
        for j in range(2,ceil(sqrt(i))+1):
            if i%j == 0 and i!=2:
                break
        else:
            a=str(i)
            if a[:]==a[::-1]:  
                print(a)
                
           