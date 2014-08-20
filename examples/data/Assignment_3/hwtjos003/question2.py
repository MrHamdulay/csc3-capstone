y = eval(input("Enter the height of the triangle:\n"))
for i in range(0,y):
    print(" " * (y - i - 1), end = "")
    print("*" * (i*2 +1))