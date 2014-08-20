#Prime number that is a palidrome, in that range
import math
n = eval(input('Enter the starting point N:\n'))
m=eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
for i in range (n+1,m):
    prime = True
    for k in range(2,int(math.sqrt(m))+1):
        if(i%k==0 and not i==k ):
            prime = False
            break
            #Then its a prime number
    pali = str(i)
    
    if(prime== True):
        
        #print(pali)
        if(pali[::-1]==pali):print(pali)