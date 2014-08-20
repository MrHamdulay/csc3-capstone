h=eval(input("Enter the height of the triangle:"'\n'))
a=1
for i in range(h):
    print(' '*(h-1),end='')
    print('*'*a)
    h=h-1
    a=a+2
    