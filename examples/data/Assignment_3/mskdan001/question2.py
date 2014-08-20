a=eval(input("Enter the height of the triangle:\n"))
gap=a-1
for i in range(0,a):
    print(' '*gap,end='')
    print(('*'*(i+1))+('*'*i))
    gap=gap-1