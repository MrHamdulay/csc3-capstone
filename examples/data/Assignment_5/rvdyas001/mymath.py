"""Permutations
Yashna Ravidas
17 April 2014"""


import math# import math functions
n=eval(input("Enter n:\n"))
k=eval(input("Enter k:\n"))

nfactorial = math.factorial (n)# calc n factorial
nkfactorial = math.factorial (n-k)# calc factorial of n-k
print ("Number of permutations:", nfactorial // nkfactorial)
   
