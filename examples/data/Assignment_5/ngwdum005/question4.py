"""Dumisani Ngwenza
NGWDUM005
13/04/2014
Assignment 5 Question 4"""

import math
f = input("Enter a function f(x):\n")

   
plus = '+'
minus = '-'
times = '*'
divide = '/'
x=0
split = int(f.find(plus))
increment = 0
split_minus = f.find(minus)
y = 0
if split !=0:
   #t = f[:split]
   #t = eval (t)
   increment = f[split:]
   increment = eval(increment)
   for i in range(-10,11):
      y = i+increment
      x = y

if split_minus !=0:
   #t = f[:split_minus]
   #t = eval (t)
   increment = f[split_minus+1:]
   increment = eval(increment)
   for i in range (-10,11):
      y = i-increment
      x = y
else:
   for i in range (-10,11):
      y = i
      x = y

def graph (x):
   for i in range(10,-11,-1):
      for j in range(-10,11):
         x = j
         if(eval(f)==i):
            print("o",end="")
         elif(i==0 and j==0):
            print("+",end="")        
         elif(j==0):
            print("|",end="")
         elif(i==0):
            print("-",end="")
         else:
            print(" ",end="")
      print()

if __name__=='__main__':
   graph(6)