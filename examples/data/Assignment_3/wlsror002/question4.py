N=eval(input('Enter the starting point N:\n'))
M=eval(input('Enter the ending point M:\n'))


def prime(x):
    count=0
    if x==1:
        return 'true'
    for i in range (x+1):
        if i==0:
            continue
        if x%i==0:
            count=count+1
    if count ==2:
        return 'true'
    else:
        return 'False'
    
def pal(x):
    a=str(x)
    b=str(x)[::-1]
    if a==b:
        return 'true' 
    
print('The palindromic primes are:')
for x in range(N,M+1):
    a=prime(x)
    b=pal(x)
    if a=='true' and b=='true':
        print(x)