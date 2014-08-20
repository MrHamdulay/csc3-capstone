import math

start = eval(input('Enter the starting point N:\n'))
end = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')

prime_cap = math.sqrt(end)

primes = [2]
prime_pals = []

#generate necessary prime numbers
for x in range(2,int(prime_cap)+1):
    is_prime = True
    for p in range(0,len(primes)):
        if x%primes[p]==0:
            is_prime = False
    if is_prime:
        primes.append(x)
        
for x in range(start+1,end):
    if str(x)[::-1]!=str(x):
        continue
#'''
    prime_cap = int(math.sqrt(x))
    is_prime = True
    for i in range(0,len(primes)):
        if primes[i]>prime_cap: break
        if x%primes[i]==0:
            is_prime = False
    if is_prime:
        prime_pals.append(x)
#'''
        
#'''        
for i in range(len(prime_pals)):
    print(prime_pals[i])
#'''