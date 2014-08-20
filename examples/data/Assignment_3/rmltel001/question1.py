#Output a rectangle

height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))

for i in range(height):
    for j in range (width):
        print("*", end = "")
    print()
    