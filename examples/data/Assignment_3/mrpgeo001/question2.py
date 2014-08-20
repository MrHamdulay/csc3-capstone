height = eval(input("Enter the height of the triangle:\n"))

star = 1 #initial number of stars
minus = height - 1 #The number of spaces at each line


for i in range(height):
    
    print((minus)*" ",star*"*",sep = "")
    star += 2 #Adds to the number of the stars to be printed
    minus -= 1