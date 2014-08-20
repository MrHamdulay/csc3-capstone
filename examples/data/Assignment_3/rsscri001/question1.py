y = eval(input("Enter the height of the rectangle: \n"))
x = eval(input("Enter the width of the rectangle: \n"))
for i in range (1,y+1):
    for j in range (1,x+1):
        print('*'*x)
        break