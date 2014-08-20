height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))
for i in range(0,height,1):
    for j in range(0,width,1):
        print("*",end="")
    print()
