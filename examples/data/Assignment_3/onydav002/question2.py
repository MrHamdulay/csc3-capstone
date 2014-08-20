# Triangle stuff
a=eval(input("Enter the height of the triangle: \n"))
b=a
for i in range(a):
    gap=' '*(b-1)
    print(gap,end='')
    print('*'*(2*i+1),end='')
    print(gap,end='')
    print()
    b=b-1
