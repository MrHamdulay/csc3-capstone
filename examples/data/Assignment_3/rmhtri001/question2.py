Height = eval(input("Enter the height of the triangle:\n"))
for i in range(1,Height+1):
    gap = Height-i
    print(" "*gap,"*"*i, sep="", end="")
    print("*"*(i-1))