# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

def get_integer (x):
   if x=="n":
      x = input ("Enter n:\n")
      while not x.isdigit ():
         x = input ("Enter n:\n")
   else:
      x = input ("Enter k:\n")
      while not x.isdigit ():
         x = input ("Enter k:\n")      
   x = eval (x)
   return x

def calc_factorial(x):
   factorial=1
   for i in range (1, x+1):
      factorial *= i
   return factorial

