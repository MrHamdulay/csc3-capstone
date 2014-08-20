#Assignment 9, Question 3
#James Nevin
#13 May 2014

import string

grid = []
for x in range(9):
    grid.append(input()) #Getting user's grid

is_valid = True #Assume is valid
for x in range (9):
    already_present = []
    for y in range (9): #Go through rows and check if already in row and correct number
        if grid[x][y] in already_present or grid[x][y] not in '987654321':
            is_valid = False #If invalid
            break
        else:
            already_present.append(grid[x][y]) #Add number to list of already present
if is_valid:
    for x in range (9): #Same as above, going by column
        already_present = []
        for y in range (9):
            if grid[y][x] in already_present or grid[y][x] not in '987654321':
                is_valid = False
                break
            else:
                already_present.append(grid[y][x])
if is_valid:
    for x in range (3):
        already_present = []
        for y in range (x*3, (x+1)*3):
            for z in range (x*3, (x+1)*3): #Going through 3x3 squares
                if grid[y][z] in already_present or grid[y][z] not in '987654321':
                    is_valid = False #Same as above
                    break
                else:
                    already_present.append(grid[y][z])

if is_valid:
    print ("Sudoku grid is valid")
else:
    print ("Sudoku grid is not valid") #Printing result