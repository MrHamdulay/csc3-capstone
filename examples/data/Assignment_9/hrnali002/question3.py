"""A program to check that a sudoku grid is valid
Alison Hoernle
HRNALI002
11 May 2014"""

def sudoku(grid):
            
    #check through the rows
    for row in grid:
        checked = []
        for item in row:
            if item in checked:
                return False
            else:
                checked.append(item)
    
    # check through the columns
    c = 0
    checked = []
    for col in range(9):
        for row in grid: # go through each row in the grid once for each column number 
            if row[c] in checked: 
                return False
            else:
                checked.append(row[c])
        
        c += 1
        checked = []
        
    # check the 3 x 3 sub-grids
    sub_grid_1 = []
    sub_grid_2 = []
    sub_grid_3 = []

    # first three rows
    for row in range(3):

        # column 1 - 3
        for col in range(3):
            if grid[row][col] in sub_grid_1:
                return False
            else:
                sub_grid_1.append(grid[row][col])
        
        # column 4 - 6    
        for col in range(3, 6):
            if grid[row][col] in sub_grid_2:
                return False
            else:
                sub_grid_2.append(grid[row][col])
        
        # 7 - 9    
        for col in range(6, 9):
            if grid[row][col] in sub_grid_3:
                return False
            else:
                sub_grid_3.append(grid[row][col])                
                
    sub_grid_1 = []
    sub_grid_2 = []
    sub_grid_3 = []    
    
    # now for the next three rows
    for row in range(3, 6):
        for col in range(3):
            if grid[row][col] in sub_grid_1:
                return False
            else:
                sub_grid_1.append(grid[row][col])
                            
        for col in range(3, 6):
            if grid[row][col] in sub_grid_2:
                return False
            else:
                sub_grid_2.append(grid[row][col])
                            
        for col in range(6, 9):
            if grid[row][col] in sub_grid_3:
                return False
            else:
                sub_grid_3.append(grid[row][col]) 
    
    sub_grid_1 = []
    sub_grid_2 = []
    sub_grid_3 = [] 
    
    # for the last three rows
    for row in range(3, 6):
        for col in range(3):
            if grid[row][col] in sub_grid_1:
                return False
            else:
                sub_grid_1.append(grid[row][col])
                
        for col in range(3, 6):
            if grid[row][col] in sub_grid_2:
                return False
            else:
                sub_grid_2.append(grid[row][col])
                                
        for col in range(6, 9):
            if grid[row][col] in sub_grid_3:
                return False
            else:
                sub_grid_3.append(grid[row][col])    
    
    # if in all of those checks, it did not return false, then return true            
    return True

grid = []
x = input() # input their first line
grid.append(x)
for i in range(8): # for the next 8 lines of input, append each line to the grid
    x = input()
    grid.append(x)

sud = sudoku(grid)
if sud is True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

    