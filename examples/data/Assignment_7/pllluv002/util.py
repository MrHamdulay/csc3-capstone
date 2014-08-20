grid = []
def create_grid(grid):
    """create a 4x4 grid"""
    height = 4
    for i in range (height):
        grid.append ([0] * 4)      
    return(grid)

def print_grid (grid):
    """ print out a 4x4 grid"""
    height = 4
    print('+--------------------+')    
    for i in range (height):
        print("|", end="")  
        for j in range(height):  
            if grid[i][j] is 0:
                print("{0:>5}".format(""),end="")
                
            else:
                 print(grid[i][j], (5-len(str((grid[i][j]))))*" ", sep="", end="")
        print('|')
    print('+--------------------+')    
    
    
def check_won (grid):
     """return True if a value>=32 is found in the grid; otherwise False"""
     for i in range(4):
        for j in range(4):
            if grid[i][j]==32 or grid[i][j]>32 :
                return True
     return False

            

    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    height=4
    for i in range(height):
        for j in range(height):
                if grid[i][j] is 0:
                    return False
                
                if j!=3:
                    if grid[i][j] is grid[i][j+1]:
                        return False
                if i!=3:
                    if grid[i][j] is grid[i+1][j]:
                        return False
                 
                 
    return True 


def copy_grid (grid):
    """return a copy of the grid"""
    copy_grid=[]
    for i in range(4):
        new_grid=[]
        
        for j in range(4):
            new_grid.append(grid[i][j])
        copy_grid.append(new_grid)
    
    return copy_grid
    
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j]is not grid2[i][j]:
                return False
    return True