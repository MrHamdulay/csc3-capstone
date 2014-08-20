"""Program that uses modules
Ringo Shima
17/4/14"""

def get_integer (z):
   if z  == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n

   elif z == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

def calc_factorial (y):
   nfactorial = 1
   for i in range (1, y+1):
      nfactorial *= i
   return nfactorial