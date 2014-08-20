height = eval(input("Enter the height of the triangle:\n"))
x=1
for i in range(height,0,-1):
    print(' '*(i-1),end='')
    print('*'*x)
    x+=2