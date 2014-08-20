starting = eval(input("Enter the starting point N:\n"))

ending = eval(input("Enter the ending point M:\n"))

import math
  
def prime(n):
    Is_prime = True
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            Is_prime = False
    if Is_prime == True:
        if str(n)[::-1]==str(n):
            print(n)

print( "The palindromic primes are:")

for i in range(starting+1,ending):
    prime(i)