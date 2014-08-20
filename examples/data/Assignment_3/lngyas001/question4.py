import math

n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')

for i in range(n+1,m):
    a = str(i)
    if (a[::-1]==a):
        prime=1
        for k in range(2,int(math.sqrt(i)+1),1):
            if i%k == 0:
                prime=0
        if prime == 1:
            print (i)

       
       
       
    
    
    
    
    
