import math

a=eval(input("Enter the starting point N:"'\n'))
b=eval(input("Enter the ending point M:"'\n'))
print("The palindromic primes are:")
for i in range(a+1,b):
   isprime = True
   k=2
   while(k <= math.sqrt(i)):
      if i%k==0:
         isprime = False
         break
      k+=1
   if isprime and str(i)==str(i)[::-1]:
      print(i)

            