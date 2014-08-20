n = input ("Enter n:\n")
while not n.isdigit ():
   n = input ("Enter n:\n")
n = eval (n)   

k = input ("Enter k:\n")
while not k.isdigit ():
   k = input ("Enter k:\n")
k = eval (k)

nfactorial = 1
for i in range (1, n+1):
   nfactorial *= i

nkfactorial = 1
for i in range (1, n-k+1):
   nkfactorial *= i
   
def get_integer(x):
   if x=="n":
      return n
   if x=="k":
      return k
   
def calc_factorial(y):
   if y==n:
      return nfactorial
   if y==n-k:
      return nkfactorial
   
   