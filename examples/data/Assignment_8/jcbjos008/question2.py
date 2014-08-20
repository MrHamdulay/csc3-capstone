'''Joshen Credelio Jaocb
08/05/2014
Pairs'''

x=input('Enter a message:\n')
y=0
def pairs(x):
    if len(x) < 2:
        return 0
    else:
        if x[-1]==x[-2]:
            return pairs(x[:-2]) + 1
        else:
            return pairs(x[:-1])
        

y=pairs(x)
print('Number of pairs:',y)