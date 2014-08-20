import math
n=eval(input("Enter the starting point N: \n"))
m=eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
for i in range(n+1,m):  
    if str(i) == str(i)[::-1]:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            print(i)               
        
     
       