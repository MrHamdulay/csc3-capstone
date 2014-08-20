height = eval(input("Enter the height of the triangle:\n"))
x = height - 1
y = 1
for i in range(height):
    print(x*" ", end = "")
    print("*"*y)
    x= x- 1
    y = y + 2