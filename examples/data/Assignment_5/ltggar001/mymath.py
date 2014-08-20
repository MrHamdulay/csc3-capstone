# calculate number of k-permutations of n items
# gareth lategan
# 17 april 2014

def get_integer(x):
   if x == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n) 
      return n
      
   elif x == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k
   
def calc_factorial(a):
   q = 1
   for i in range (1, a+1):
      q *= i 
   return q