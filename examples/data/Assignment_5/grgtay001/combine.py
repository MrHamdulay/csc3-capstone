""" k-permutations of n items
 tayla george
 17 april 2014"""

n = input ("Enter n:\n")
while not n.isdigit (): #converting a string into a number
   n = input ("Enter n:\n")
n = eval (n)   

k = input ("Enter k:\n")
while not k.isdigit (): #converting a string into a number
   k = input ("Enter k:\n")
k = eval (k)

nfactorial = 1
for i in range (1, n+1): #calculating factorial
   nfactorial *= i

nkfactorial = 1 #calculating factorial
for i in range (1, n-k+1):
   nkfactorial *= i

print ("Number of permutations:", nfactorial // nkfactorial)
