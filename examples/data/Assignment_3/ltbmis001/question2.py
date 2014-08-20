x=eval(input("Enter the height of the triangle:\n"))
s=1
y=x
for i in range(x):
    print(' '*(y-1),end='')
    print('*'*s)
    s+=2
    y-=1