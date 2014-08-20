print('Enter the height of the triangle:')
h=eval(input())
gap=h*2//2-1
for i in range(0,h*2,2):
    print(' '*gap,end='')
    print('*'*(i+1))
    gap=gap-1
    
