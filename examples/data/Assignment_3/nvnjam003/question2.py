height = eval(input("Enter the height of the triangle:\n"))
for x in range (0, height):
    print ((height-1-x)*" " + (2*x+1)*"*")