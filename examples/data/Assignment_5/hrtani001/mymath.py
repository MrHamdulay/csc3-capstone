#combine edit
#Aniq Hartle
#16-04-2014

#get and store user input
n = input ("Enter n:\n")
while not n.isdigit ():
   n = input ("Enter n:\n")
n = eval (n)

k = input ("Enter k:\n")
while not k.isdigit ():
   k = input ("Enter k:\n")
k = eval (k) 

nk = n-k

#method for calculating factorial for entered value n
def calc_factorial (n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial

#method for calculating factoorial value of n-k
def calc_factorial (nk):
   nkfactorial = 1
   for i in range (1, nk+1):
      nkfactorial *= i
   return nkfactorial

#get method
def get_integer (i):
   if i == "n":
      return n
   elif i == "k":
      return k
