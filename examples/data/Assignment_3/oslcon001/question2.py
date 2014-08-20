height = int(input("Enter the height of the triangle:\n"))
for x in range(height):
    print(" "*(height-(x+1)) + "*"*(x*2 + 1))