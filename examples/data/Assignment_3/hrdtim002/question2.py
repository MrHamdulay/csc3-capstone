y = eval(input("Enter the height of the triangle:\n"))
for i in range(y):
    print(' '*(y-(i+1)),'*'*((2*(i+1))-1), sep='')