height = eval(input("Enter the height of the triangle:\n")) - 1
Height = height
for i in range(1,(Height+2)):
     print(' '*(height),'*'*((i*2) -1), sep='')
     height -= 1