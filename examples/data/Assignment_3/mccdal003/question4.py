#Pragram to find the palindromic primes
#Palesa Tshabalala
#20 March 2012


import math
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for palin in range(N+1,M):
    prime= True
    for i in range(2,int(math.sqrt(palin)+1)):
        if (palin%i==0):
            prime=False
    if prime:
        palin= str(palin)
        RevPalin=palin[::-1]
        if RevPalin==palin:
            print(palin)
    