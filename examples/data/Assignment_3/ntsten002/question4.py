#Tendani Netshitenzhe
# question 4
import math
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for j in range(start+1, end):
    n= 2    
    while n< j :
        if (j%n) == 0: break
        n+=1
    else:
        if j==1: continue
        j=str(j)
        if j==j[::-1]:
            print(j)      