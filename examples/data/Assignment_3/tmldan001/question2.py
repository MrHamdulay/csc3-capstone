x=eval(input('Enter the height of the triangle:\n'))
y='*'
z=1
gap=x-1
for i in range(x):
        print(' '*gap,end='') 
        print(y*(z))
        gap-=1
        z=z+2
