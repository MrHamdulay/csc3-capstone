height = eval(input('Enter the height of the triangle:\n'))
gap = height - 1
for i in range(height):
    print(" " * gap, end = "")
    print("*" * (1+i), end = "")
    print("*" * i)
    gap-=1