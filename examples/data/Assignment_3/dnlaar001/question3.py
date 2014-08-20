x=input('Enter the message:\n')
y=eval(input('Enter the message repeat count:\n'))
z=eval(input('Enter the frame thickness:\n'))
for p in range(0,z):
    print('|'*(p),end='')
    print('+',end='')
    print('-'*(len(x)+2+2*((z-1)-p)),end='')
    print('+',end='')
    print('|'*(p))
for i in range(0,y):
    print('|'*z,end='')
    print('',x,'',end='')
    print('|'*z)
for e in range(1,z+1):
    print('|'*(z-e),end='')
    print('+',end='')
    print('-'*(len(x)+2+2*(e-1)),end='')
    print('+',end='')
    print('|'*(z-e))
    


