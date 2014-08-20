x=eval(input('Enter the height of the triangle:\n'))
t=x+1
space=(2*(x)-1)//2
for i in range(1,t,1):
    row=2*i-1
    print(' '*space,end='')
    print('*'*(2*i-1))
    space-=1
   
        
    