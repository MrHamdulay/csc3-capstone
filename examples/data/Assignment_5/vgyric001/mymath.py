# calculate number of k-permutations of n items
# Richard van Gysen
# 15 april 2014

# get integer

def get_integer(x):
   n = input ("Enter "+x+":\n")
   while not n.isdigit ():
      n = input ("Enter "+x+":\n")
   n = eval (n)
   return n

# calculate factorial

def calc_factorial(x):
   factorial = 1
   for i in range (2, x+1):
      factorial *= i
   return factorial