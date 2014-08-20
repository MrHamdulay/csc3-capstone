height = eval(input("Enter the height of the triangle:\n"))
x = 1
for i in range(height):
    gap = height - (i+1)
    print(" " *gap, end = "")
    print("*" * (x))
    x += 2
    