x=eval(input("Enter the height of the triangle:\n"))
w=(2*(x-1))+1
for i in range(0,x):
    print(' '*((w-(2*i+1))//2),end='')
    print('*'*((2*i)+1))
