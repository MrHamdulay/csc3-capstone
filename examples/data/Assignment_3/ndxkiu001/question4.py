#question4
import math

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))

l =[]

for x in range(n+1,m):
    if str(x) == str(x)[::-1]:
        t = True
        for i in range(2,int(math.sqrt(x))+1):
            if x % i is 0:
                t =False
                break
        if t is True:
            l.append(x)

print("The palindromic primes are:")
for x in l:
    print (x)

    

    
