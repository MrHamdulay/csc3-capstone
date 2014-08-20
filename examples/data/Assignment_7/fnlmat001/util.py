# Matthew Finlayson - FNLMAT001
# Assignment 7 question 2 
# 01/05/14

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)


def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    for row in range(6):
        for col in range(22):
            if (row == 0 and col == 0) or (row == 0 and col == 21) or (row == 5 and col == 0) or (row == 5 and col == 21):
                print("+", end = "")
            elif (row == 0 or row == 5):
                print("-", end = "")
            elif (col == 0 or col == 21):
                print("|", end = "")
            elif (col%5==1):
                if (grid[row-1][col//5] == 0):
                    print(" "*5, end = "")
                else:
                    print(str(grid[row-1][col//5]) + " "*(5-len(str(grid[row-1][col//5]))), end = "")
        print()
        
        
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range (4):
        for col in range (4):
            if grid[row][col] == 0:
                return False
            if col < 4 and row < 4:
                if (row == 3 and col!=3): # if checking in the last row, must not retrieve grid[row+1]
                    if grid[row][col] == grid[row][col+1]: return False
                elif (col == 3 and row!=3): # if checking in the last column, must not retrieve grid[row][col+1]
                    if grid[row][col] == grid[row+1][col]: return False
                elif (row!=3 and col!=3): # if not checking the bottom corner box
                    if grid[row][col] == grid[row+1][col]: return False
                    if grid[row][col] == grid[row][col+1]: return False
    return True


def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    return False
                
                
def copy_grid(grid):
    """return a copy of the grid"""
    newGrid = []
    for i in range (4):
        newGrid.append([" "]*4)
        
    for row in range (4):
        for col in range (4):
            newGrid[row][col] = grid[row][col]
    return newGrid


def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if (grid1 == grid2):
        return True
    else:
        return False
        
        
#grid = [[2,0,2,0],[0,4,0,8], [0,16,0,128], [2,2,2,2]]