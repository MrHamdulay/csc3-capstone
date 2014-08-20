import math

x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(x+1,y):
    isprime = True
    a=2
    while(a <= math.sqrt(i)):
        if i%a==0:
            isprime = False
            break
        a+=1
    if isprime and str(i)==str(i)[::-1]:
        print(i)