import math
numS=eval(input("Enter the starting point N:\n"))
numE=eval(input("Enter the ending point M:\n"))          
print("The palindromic primes are:")
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True     

for j in range(numS+1, numE):
    x=str(j)
    #print(x)
    l=len(x)
    y=x[-1::-1]
    if(x==y):
        Valid=is_prime(j)
        if Valid==True:
            print(j)
    
  

