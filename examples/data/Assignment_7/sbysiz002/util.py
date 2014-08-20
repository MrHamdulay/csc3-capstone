height = 4    
def create_grid(grid):
    """create a 4x4 grid"""
    for s in range(height):
        grid.append([0]*height)
        
def print_grid(grid):
        """print out a 4x4 grid in 5-width columns within a box"""
        print('+--------------------+')
        for row in range(height):
            print('|',end='')
            for column in range(height):
                if grid[row][column] == 0:
                    print(' '*5,end='')
                else :
                    space = 5 - len(str(grid[row][column]))
                    print(grid[row][column],' '*space,sep='',end='')
            print('|')
        print('+--------------------+')
            
def check_lost(grid):
    """return true if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for f in range(height):      #checks 0's in row
        if 0 in grid[f]:
            return False
        else:                    #checks the adjacent values
            for t in range(height):  
                if (t+1)<height and (f+1)<height:
                    if grid[f][t] == grid[f][t+1] or  grid[f][t] == grid[f+1][t]:
                        return False
    return True                    

def check_won(grid):
    """return True if a value>=32 is found in the grid"""
    for row in range(height):
        for column in range(height):
            if grid[row][column]>=32:
                return True
    return False

def copy_grid(grid):
    """return a copy of the grid"""
    copy = []
    for r in range(height):
        copy.append([' ']*height)
        for j in range(height):
            copy[r][j] = grid[r][j]
    return copy

def grid_equal(grid1, grid2):
    """check if 2 grid are equal - return boolean value"""
    if grid1 == grid2 :
        return True
    else :
        return False
    
