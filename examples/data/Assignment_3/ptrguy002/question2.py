h = eval(input("Enter the height of the triangle:\n"))
for i in range(0, h):
    print((h-1-i)*" " + (1+2*i)*"*" + (h-1-i)*" ")
