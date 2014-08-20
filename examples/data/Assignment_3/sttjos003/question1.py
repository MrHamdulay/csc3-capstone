i=0
j=0
x=eval(input("Enter the height of the rectangle:\n"))
y=eval(input("Enter the width of the rectangle:\n"))

while i<x:
    while j<y:
        print("*", end="")
        j=j+1
    i=i+1
    j=0
    print()