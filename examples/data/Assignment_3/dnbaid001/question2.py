height = eval(input("Enter the height of the triangle:\n"))

char = 1 #initialise the number of *s in first row
space = height - 1 # initialise the number of spaces before the row as height - 1 

for i in range (height): #iterates for number of rows
    print (" "*space, "*"*char, sep = "") # prints space and characters with no separator
    char += 2 #number of charactes in next row reduced by 2
    space -= 1 #number of spaces before next row increased by 1
    