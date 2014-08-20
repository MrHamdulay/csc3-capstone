height = eval(input("Enter the height of the triangle:\n"))
count = 1
length = 1
while count <= height:
    print(" " * (height - count), end = "")
    print("*" * length)
    count += 1
    length += 2