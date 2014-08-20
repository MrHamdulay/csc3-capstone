""" manipulate 2-dimensional arrays of size 4x4
kamogelo mphela
27 april 2014"""



def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    print("+--------------------+")
    for y in range(4):
        print("|",end='')
        for x in range(4):
            
            if grid[y][x] ==0:
                # print " " instead of 0
                print ("{0:<5}".format(" "),end='')
                
            else:
                print("{0:<5}".format(grid[y][x]),end='')
            
        print("|")
    
    print("+--------------------+")           
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for y in range(3):
        for x in range(3):
            if grid[y][x]==grid[y][x+1] or grid[y][x]==grid[y+1][x] or grid[3][x]==grid[3][x+1] or grid[2][3]==grid[3][3] or grid[x][y] ==0 or grid[y+1][x] ==0 or grid[y][x+1] ==0:
                return False
    
    else:
        return True
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for y in grid:
        for x in y:
            if x >=32:
                return True
    else:
        return False
    
def copy_grid (grid):
    """return a copy of the grid"""
    import copy
    new_grid= copy.deepcopy (grid)
    return new_grid
            
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    k=0
    for y in range(4):
        for x in range(4):    
            if grid1[y][x] != grid2[y][x]:
                k+=1
    if k==0:
        return True
    else:
        return False 