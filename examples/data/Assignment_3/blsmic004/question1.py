# Draw rectangle with given height and width
# Michele Balestra BLSMIC004
# 23 March 2014

height = eval(input("Enter the height of the rectangle:\n"))
length = eval(input("Enter the width of the rectangle:\n"))

for i in range(height):
    print("*"*length)
    