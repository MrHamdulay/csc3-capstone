'''Jason Pietersen'''
x=input('Enter a space-separated list of marks:\n').split(' ')
y={'F':0,'1':0,'2+':0,'2-':0,'3':0}


for i in x:
    i=eval(i)
    if (i<50):
        y['F']+=1
    elif (50<=i<60):
        y['3']+=1
    elif (60<=i<70):
        y['2-']+=1
    elif (70<=i<75):
        y['2+']+=1
    else:
        y['1']+=1
print('1 |'+'X'*y['1'])
print('2+|'+'X'*y['2+'])
print('2-|'+'X'*y['2-'])
print('3 |'+'X'*y['3'])
print('F |'+'X'*y['F'])