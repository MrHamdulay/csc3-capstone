"""Program that checks if a complete Sudoku grid is valid or not
Matthew Finlayson - FNLMAT001
11/05/2014"""

grid = []
for i in range(9): 
    line = input("") # gets each row of values
    row = []
    for j in range(9):
        row.append(eval(line[j])) # creates a list of the row of numbers
    grid.append(row) # appends the created list to create a 2d grid

#testing code to print out the grid
#for row in range(9):
#    for col in range(9):
#        print(grid[row][col], end = "")
#    print()

def isValid(grid): 
    valid = True
    
    for row in range(9):
        for col in range(9):
            if grid[0][col] == grid[row][col] and row != 0:
                valid = False
                break
            elif grid[row][0] == grid[row][col] and col != 0:
                valid = False
                break
                
    if valid: # if the previous test was passed
        # goes through each of the 9 smaller grids using different start and end points when referring to the 9x9 grid
        for rowStart, rowEnd, colStart, colEnd in [[0,3,0,3],[0,3,3,6],[0,3,6,9],[3,6,0,3],[3,6,3,6],[3,6,6,9],[6,9,0,3],[6,9,3,6],[6,9,6,9]]:      
            for row in range(rowStart, rowEnd): 
                for col in range(colStart, colEnd): # goes through the grid of 3x3
                    
                    for i in range(rowStart, rowEnd):
                        for j in range(colStart, colEnd): # goes through the same grid as above
                            
                            if (row != i and col != j): # if they don't both refer to the same slot
                                if grid[row][col] == grid[i][j]:  # if there are duplicates                                    
                                    valid = False 
                                    break
                            if not valid: break # stop testing if there are duplicates
                        if not valid: break
                    if not valid: break
                                
    return valid

if isValid(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
    