#Display triangle

height = eval(input("Enter the height of the triangle:\n"))
j = 1
for i in range(height, 0, -1):
    print(" "*(i-1), '*'*j, sep = "")
    j+=2
