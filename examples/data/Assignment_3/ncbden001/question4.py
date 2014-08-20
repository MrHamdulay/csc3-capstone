import math
lower = eval(input("Enter the starting point N: \n"))
upper = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
def prime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True
for j in range(lower+1,upper):
    forwards = str(j)
    backwards = forwards[::-1]
    checker = prime(j)
    if forwards == backwards and checker == True : print(forwards)                           

    
  
        
    
    
   

