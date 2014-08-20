# Triangle

height = eval (input ("Enter the height of the triangle:\n"))
spaces = height - 1
stars = 1
for i in range (height):
    for j in range (spaces):
        print (" ", end = "")
    for k in range (stars):
        print ("*", end = "")
    spaces-=1
    stars+=2
    print()