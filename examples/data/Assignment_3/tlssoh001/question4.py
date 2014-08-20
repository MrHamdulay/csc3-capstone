# Sohail Tulsi TLSSOH001
# 24/03/2014
# finding palindromic primes

n= eval(input('Enter the starting point N:\n'))
m= eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
for i in range(n+1,m):
        x=str(i)
        reverse= x[::-1]
        if x==reverse:
                count=0
                for p in range(i,0,-1): 
                        if i%p==0:
                                count+=1
                if count==2:
                        print(i)
                        