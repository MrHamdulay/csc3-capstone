"""Calculating number of permutations
Kumaran Reddy
16 APRIL 2014"""

#get integers
n=(input("Enter n:\n"))
while not n.isdigit ():
    n=input("Enter n:\n")
n=eval(n)
k=(input("Enter k:\n"))
while not k.isdigit ():
    k=input("Enter k:\n")
k=eval(k)
    
#get permutations
nfactorial=1
for i in range(1,n+1):
    nfactorial*=i
    
n_kfactorial=1
for x in range(1,(n-k)+1):
    n_kfactorial*=x
number_of_permutations=nfactorial//n_kfactorial
print("Number of permutations:",number_of_permutations)
