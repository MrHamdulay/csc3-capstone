x=eval(input('Enter the height of the triangle:\n'))

def tri(x):
    gap=x*2//2-1
    for i in range(0,x*2,2):
        print(' '*gap,end='')
        print('*'*(i+1))
        gap-=1
tri(x)