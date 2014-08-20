#module of functions to manipulate 4x4 arrays
#victor gueorguiev
#27 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+'+'-'*20+'+')
    for row in range(len(grid)):
        print('|',end='')
        for qelement in grid[row]:
            if qelement == 0:
                print('{0:<5}'.format(' '),end='')
            else:
                print('{0:<5}'.format(qelement),end='')
        print('|')
    print('+'+'-'*20+'+')

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    any_zeroes = False
    any_equal_adjacents = False
    for i in range(len(grid)):
        for q in range(len(grid[i])):
            if grid[i][q] == 0:
                any_zeroes = True
    for i in range(1,len(grid)-1):
        #for row starting at second row, and column not including the last column, this should be sufficient to check the whole grid
        for q in range(len(grid[i])-1):
            if (grid[i+1][q] == grid[i][q]) or (grid[i-1][q] == grid[i][q]) or (grid[i][q+1] == grid[i][q]):
                any_equal_adjacents = True
            #check row above, below, and to the right of grid element 1 for equality, no need to the left because if the right is not equal then this implies inequality for the next element to the left 
    if (any_zeroes == False) and (any_equal_adjacents == False):
        return True
    else: 
        return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    result = False
    for i in range(len(grid)):
        for q in range(len(grid[i])):
            if grid[i][q] >= 32:
                result = True
    return result

def copy_grid (grid):
    """return a copy of the grid"""
    copy_grid1 = []
    for i in range(len(grid)):
        new_1D_element = []
        for q in range(len(grid[i])):
            new_1D_element.append(grid[i][q])
        copy_grid1.append(new_1D_element)
    return copy_grid1
                        
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False