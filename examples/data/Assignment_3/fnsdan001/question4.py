import math
n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))





prime = [1]*(m+1)



    
for i in range(2, int(math.sqrt(m) +1)):
    if prime[i] == 1:
        
            
        for j in range(i, m):
                if i*j<=m:
                    prime[i*j] = 0
prime[0] = 0
prime[1] = 0
prime[n] = 0
prime[m] = 0
print("The palindromic primes are:")
for i in range (n, m+1):
    if prime[i] == 1 and str(i) == str(i)[::-1]:
        print (i)
            
            
    



    
