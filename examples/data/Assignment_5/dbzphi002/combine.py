# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

n = input ("Enter n:\n")
while not n.isdigit ():# if n is not a number, keep looping until a number is entered
   n = input ("Enter n:\n")
n = eval (n) #put eval at the beginning

k = input ("Enter k:\n")
while not k.isdigit ():
   k = input ("Enter k:\n")
k = eval (k)#change to eval

nfactorial = 1
for i in range (1, n+1):
   nfactorial *= i

nkfactorial = 1
for i in range (1, n-k+1):
   nkfactorial *= i

print ("Number of permutations:", nfactorial // nkfactorial)
