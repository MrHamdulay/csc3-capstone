#kennedy
import math
m=eval(input("Enter the starting point N:\n"))
n=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range (m+1,n):
    for z in range(2,round(math.sqrt(i)+1)):
        if i%z==0: break
    else:
        if str(i)==str(i)[::-1]:
            print(i)
    
    



    