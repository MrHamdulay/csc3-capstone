def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append ([0] * 4) 
    #return grid

        
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+','-'*20,'+',sep='')
    for i in grid:
        print('|',end="")
        for j in i:
            if j == 0:
                j = ''
                
            print("{0:<5}".format(j),end="")
        print('|')
    print('+','-'*20,'+',sep='')

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in grid:
        for j in i:
            if j == ' ':
                return False
    for i in range(len(grid)):
        for j in range(4):
            position = grid[i][j]
            to_right = j +1
            if 0 <= to_right <4:
                if position==grid[i][to_right]:
                    return False
            to_left = j - 1
            if 0 <= to_left <4:
                if position==grid[i][to_left]:
                    return False
            up = i -1
            if 0 <= up < 4:
                if position == grid[up][j]:
                    return False
            down = i + 1
            if 0 <= down <4:
                if position == grid[down][j]:
                    return False
    return True
        
def copy_grid (grid):
    """return a copy of the grid"""
    copy_grid = []
    create_grid(copy_grid)
    for i in range(4):
        for j in range(4):
            copy_grid[i][j] = grid[i][j]
    
    return copy_grid      
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j >= 32:
                return True
    return False

    





if __name__ == '__main__':
    a=[]
    create_grid(a)
    print_grid(a)