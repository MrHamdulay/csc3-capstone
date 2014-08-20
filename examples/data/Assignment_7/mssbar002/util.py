def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+" + "-"*20 + "+")
    for row in range(4):
        print("|", end="")
        for col in range(4):
            printString= str(grid[row][col]) + " "*(5 - len(str(grid[row][col])))
            if grid[row][col] == 0:
                print(" "*5, end="")
            else:
                print(printString, end="")
        print("|", end="")
        print()
    print("+" + "-"*20 + "+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    zeroValues = True
    adjacentValues = True
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                zeroValues = False
            if col < 3:
                if grid[row][col] == grid[row][col+1]:
                    adjacentValues = False
            if row < 3:
                if grid[row][col] == grid[row+1][col]:
                    adjacentValues = False                
    if zeroValues and adjacentValues:
        return True
    else: 
        return False
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    found = False
    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:
                found = True
    if found == True:
        return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    grid2 = []
    for i in range(4):
        grid2.append([0]*4) 
        
    for row in range(4):
        for col in range(4):
            grid2[row][col] = grid[row][col]
    
    return grid2

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal = True
    for row in range(4):
        for col in range(4):
            if grid1[row][col] != grid2[row][col]:
                equal = False
                break
        if equal == False:
            break
    return equal