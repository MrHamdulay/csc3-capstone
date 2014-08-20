x= input('Enter the starting point N:\n')
m= input('Enter the starting point N:\n')
x=int(x)
m=int(m)

def f(x):
    if x=='' or x==' ':
        return''
    elif x==m:
        return''
    else:
        return x+1+p(num)
    
num=f(x)

def p(num):
    if x=='' or x==' ':
        return''
    else:
        return x[-1] + p(x[0:len(x)-1])
mic=p(x)

print(mic)
