height = eval(input("Enter the height of the triangle:\n"))
numStars = 1
spaces = height
for i in range (height):
    print(" "*(spaces-1)+"*"*numStars)
    numStars = numStars+2
    spaces = spaces-1
    