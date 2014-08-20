h=eval(input("Enter the height of the triangle:\n"))
gap=h-1
for i in range(0,h):
    print(' '*gap,end='')
    print('*'*(2*i+1))
    gap-=1
