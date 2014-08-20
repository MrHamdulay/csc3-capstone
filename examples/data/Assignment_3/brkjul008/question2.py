h=eval(input("Enter the height of the triangle:\n"))

gap=h-1
for i in range(0,h*2,2):
    print(' '*gap, end='')
    print('*'*(i+1))
    gap=gap-1