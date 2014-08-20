"""Assignment 5 question 3
Jadon Thomson
2014-04-14"""

def get_integer(a):
   if a == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)       
      return n
   elif a == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)      
      return k
   

def calc_factorial (b):
      factorial = 1
      for i in range (1, b+1):
         factorial *= i
      return factorial


