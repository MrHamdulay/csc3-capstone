"""permutations
Keyoolin Padayachee
16 April 2014
"""

#get variable n
n = input ("Enter n:\n")
while not n.isdigit ():
    n = input ("Enter n:\n")
n = eval (n)

#get variable k
k = input ("Enter k:\n")
while not k.isdigit ():
    k = input ("Enter k:\n")
k = eval (k)

#Return the integers
def get_integer(a):
    if a == "n":
        return n
    if a == "k":
        return k

#Calculate the factorials
def calc_factorial (b):
    if b == n:
        nfactorial = 1
        for i in range (1, n+1):
            nfactorial *= i
        return nfactorial
    if b == (n-k):
        nkfactorial = 1
        for i in range (1, n-k+1):
            nkfactorial *= i
        return nkfactorial
