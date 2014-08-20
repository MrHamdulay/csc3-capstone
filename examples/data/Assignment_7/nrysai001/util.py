

def create_grid(grid):
    """Create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')
    for col in range(4):
        print('|',end='')
        for row in range(4):
            if grid[col][row]==0:
                print('{0:<5}'.format(' '),end='')
            else:
                print('{0:<5}'.format(grid[col][row]),end='')
        
        
        print("|",end='')
        print()
    print('+--------------------+')


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for col in range (4):
        for row in range(4):
            if grid[col][row]==0:
                return False
            if col !=0 and col!=3 and row!=0 and row!=3:
                        if grid[col][row] == grid[col][row-1] or grid[col][row] == grid[vertical][horizontal+1] or grid[vertical][horizontal] == grid[vertical-1][horizontal] or grid[vertical][horizontal] == grid[vertical+1][horizontal]:
                                return False
                        elif col==0 and row==0:
                            if grid[col][row] == grid[col+1][row] or grid[col][row] == grid[col][row+1]:
                                return False
                        elif col ==3 and row ==0:
                            if grid[col][row] == grid[col-1][row] or grid[col][row] == grid[col][row+1]:
                                return False 
                        elif col==3 and row ==3:
                            if grid[col][row] == grid[col-1][row] or grid[col][row] == grid[col-1][row-1]:
                                return False
                        elif horizontal ==0:
                            if grid[col][row] == grid[col][row+1]:
                                return False
                        elif horizontal==3 :
                            if grid[col][row] == grid[col][row-1]:
                                return False
                        elif row==0:
                            if grid[col][row] == grid[col+1][row]:
                                return False
                        elif row==3:
                            if grid[col][row] == grid[col-1][row]:
                                return False            
    return True
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for col in range (4):
        for row in range(4):
            if grid[col][row]>=32: 
                return True
    return False
def copy_grid (grid):
    """return a copy of the grid"""
    grid1=[]
    for copy in range(4):
        grid1.append([0]*4)
    for vertical in range(4):
        for row in range(4):
            grid1[col][row]=grid[col][row]
    return grid1
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False
