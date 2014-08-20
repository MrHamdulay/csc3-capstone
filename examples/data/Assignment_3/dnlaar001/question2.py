x=eval(input('Enter the height of the triangle:\n'))
for i in range(0,x):
    print(' '*((x-1)-i),end='')
    print('*'*(2*i+1))