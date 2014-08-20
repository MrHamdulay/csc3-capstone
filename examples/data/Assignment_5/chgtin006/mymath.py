"""Program which contains functions to calculate the number of k-permutations of n items
by Tinashe Choga
15 april 2015"""

#defining the variables n
n = input ("Enter n:\n")
while not n.isdigit ():
   n = input ("Enter n:\n")
n = eval (n)   

#defining the variable k
k = input ("Enter k:\n")
while not k.isdigit ():
   k = input ("Enter k:\n")
k = eval (k)

#Calculating nfactorial
nfactorial = 1
for i in range (1, n+1):
   nfactorial *= i
   
#calculating nkfactorial
nkfactorial = 1
for i in range (1, n-k+1):
   nkfactorial *= i
   
#creating function to store the values of n and k   
def get_integer(x):
   if x=="n":
      return n
   if x=="k":
      return k
   
#creating function to store the calculated values of the nfactorial and nkfactorial
def calc_factorial (y):
   if y==n:
      return nfactorial
   if y==n-k:
      return nkfactorial
   