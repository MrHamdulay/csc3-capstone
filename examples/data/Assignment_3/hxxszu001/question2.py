x=eval(input("Enter the height of the triangle: \n"))
y=-1

for i in range(x):
    y=y+2
    print(" "*(x-(i+1))+"*" * (y))
    