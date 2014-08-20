x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))

c=0
print("The palindromic primes are:")
for i in range(x+1,y):
   for j in range(2,y):
      if(i%j == 0):
         c+=1
   if(c == 1):
      f=str(i)
      if f==f[::-1]:
         print(i)
   c=0  

