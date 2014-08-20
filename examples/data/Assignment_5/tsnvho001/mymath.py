# number of k-permutations of n items
# Tsanwani Vhonani
# 15 April 2014

def integer():
   n=input("Enter n: \n")
   while not n.isdigit():
      n=input("Enter n: \n")
   n =eval(n)

def factorial():
   nfactorial= 1
   for i in range (1,n+1):
      nfactorial*=i
   return nfactorial   
