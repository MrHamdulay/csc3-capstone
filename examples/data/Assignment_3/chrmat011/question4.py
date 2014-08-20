import math

n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
p=[1]*(m+1)

for i in range(2,math.ceil(math.sqrt(m))):
    for ii in range(i,m//2):
        if i*ii<=m:
            p[i*ii]=0

p[0]=0
p[1]=0
p[n]=0
p[m]=0
print("The palindromic primes are:")
for i in range(n,m):
    if p[i] and str(i) == str(i)[::-1]:
        print(i)
