import math

n=eval(input('Enter the starting point N:\n'))
m=eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')

n=n+1
for c in range(n,m):
    c=str(c)
    revc=c[::-1]
    if c==revc:
        if c[-1]=='0' or c[-1]=='4' or c[-1]=='6' or c[-1]=='8':continue
        else:
            c=int(c)
            if c%3==0 and c!=3:continue
            elif c%2==0 and c!=2:continue
            for j in range(4,c):
                if c%j == 0:break
            else:
                print(c)
            
                   