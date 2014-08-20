h = eval(input("Enter the height of the triangle:\n"))
spaces = h-1
stars = 1

for i in range (h):
    print (" "*spaces, sep = "", end = "")
    print ("*"*stars)
    stars += 2
    spaces -= 1
    