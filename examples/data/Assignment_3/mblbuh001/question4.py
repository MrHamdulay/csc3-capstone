# question4.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 23 March 2014

z = eval(input("Enter the starting point N:\n"))
y = eval(input("Enter the ending point M:\n"))
x = z+1

print("The palindromic primes are:")
while x<y:
   if str(x)==str(x)[::-1]:
      for i in range(2,x):
         if x%i==0:
            break
      else:
         if x>1:
            print(x)
   x+=1