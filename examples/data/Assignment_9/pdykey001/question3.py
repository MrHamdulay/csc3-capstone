"""
Check Sudoku
Keyoolin Padayachee
15 May 2014
"""

grid = []
for i in range(9):
    grid.append(list(input())) # Creates the Sudoku grid

valid = True
def Check(grid):
    for i in range(9):
        for j in range(9):
            if grid[i].count(grid[i][j]) > 1: # Checks if like numbers in the row
                return False
copy = []            
def copy_grid(grid):
    for i in range(9):
        copy.append([])
        for j in range(9):    
            copy[i].append(grid[i][j])
    return copy

def rotate90r(grid):
    gridcopy = copy_grid(grid)
    for i in range(9):
        for j in range(9):    
            grid[i][j] = gridcopy[8-j][i]
    return grid

def rotate90l(grid):
    gridcopy = copy_grid(grid)
    for i in range(9):
        for j in range(9):    
            grid[i][j] = gridcopy[j][8-i]    
    return grid

valid = Check(grid)
grid = rotate90r(grid)
valid2 = Check(grid)
grid = rotate90l(grid)

r = 0
c = 0
# Checks in the 3x3 blocks for like numbers
valid3 = True
for i in range(9):
    check = []
    for i in range(r,+r):
        for j in range(c,3+c):
            check.append(grid[i][j]) #Temps list to store values in 3x3 grid
    for i in check:
        if check.count(i)>1: #Checks for like values
            valid3 = False
            break
    r+=3    #Moves the 3x3 block right by 3
    if r == 9:
        r = 0
        c+=3 # Moves the 3x3 block down by 3
           
if valid != False and valid2 != False and valid3 != False:
    print("Sudoku grid is valid")
else: print("Sudoku grid is not valid")