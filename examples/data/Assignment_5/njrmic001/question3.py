# calculate number of k-permutations of n items
# Michelle Njoroge
# 15 april 2014

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

#creates a function get_integer
def get_integer(n):
   if n=="n":
      return n #store the value of n in the function get_integer
   elif n=="k":
      return k #store the value of k in the function get_integer

#creates a function calc_factorial
def calc_factorial (f):
   if f==n:#store the value of nfactorial in the function calc_factorial
      return nfactorial
   elif f==n-k:
      return nkfactorial #store the value of nkfactorial in the function calc_factorial

print ("Number of permutations:", nfactorial // nkfactorial)