message=input('Enter the message:\n')
repeat=eval(input('Enter the message repeat count:\n'))
thick=eval(input('Enter the frame thickness:\n'))
a=len(message)+2
b=a+2*thick
gap=0
for i in range(b,a,-2):
    print('|'*gap,end='')
    print('+',end='')
    print('-'*(i-2),end='')
    print('+',end='')
    print('|'*gap)
    gap+=1
    
for j in range(repeat):
    print('|'*thick,message,'|'*thick)
gap=thick-1
for k in range(a,b,2):
        print('|'*gap,end='')
        print('+',end='')
        print('-'*(k),end='')
        print('+',end='')
        print('|'*gap)
        gap-=1    
    