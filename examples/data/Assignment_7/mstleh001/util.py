# Lehlogonolo Masetla


height = 4
def create_grid(grid):
    """create a 4x4 grid"""
    
    for j in range(height):
        grid.append([0]*height)
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    print("+--------------------+")
    for row in range(height):
        print('|',end='')
        for column in range(height):
            if grid[row][column] == 0:
                print(' '*5,end='')
            else:
                space = 5 - len(str(grid[row][column]))
                print(grid[row][column],' '*space,sep='',end='')
        print('|')
    print("+--------------------+")
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    for r in range(height):
        #check zeros in each row
        if 0 in grid[r]:
            return False
        else:
            #check values next to each other
            for c in range(height):
                if (c+1) < height and (r+1) < height:
                    if grid[r][c] == grid[r][c+1] or grid[r][c] == grid[r+1][c]:
                        return False
    #else
    return True
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    
    for row in range(height):
        for column in range(height):
            if grid[row][column] >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    copy = []
    for r in range(height):
        copy.append([" "]*height)
        for c in range(height):
            copy[r][c] = grid[r][c]
    return copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False