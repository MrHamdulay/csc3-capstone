height = eval(input("Enter the height of the triangle:\n"))
gap = height - 1
for i in range(height):
    print(gap*" ",end="")
    print(((2*i)+1)*"*")
    gap=gap-1
    