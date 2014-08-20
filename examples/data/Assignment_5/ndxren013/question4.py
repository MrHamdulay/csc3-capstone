
import math

myin = input('Enter a function f(x):\n')#input

for i in range(10, -11, -1):#grid
   for j in range(-10, 11):#grid
      x = j
      y = round(eval(myin))
      if y == i:#evalauting whether or not y satisfies the function
         print('o', end = '')
      elif i == 0 and x == 0:
         print('+', end = '')
      elif i == 0:
         print('-', end = '')
      elif x == 0:
         print('|', end = '')
      else:
         print(' ', end = '')
   print()
