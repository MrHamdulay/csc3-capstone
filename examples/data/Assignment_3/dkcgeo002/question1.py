__author__ = 'George'
height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))
for a in range(1,height+1):
    for b in range(1,width+1):
        print("*",end="")
    print("")