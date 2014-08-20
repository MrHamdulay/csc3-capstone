x = eval(input('Enter the height of the triangle: \n'))
gap = " "
num = x-1
for i in range(1,x+1):
    print(gap * num, end="")
    print('*' *((2*i)-1))
    num -=1

 