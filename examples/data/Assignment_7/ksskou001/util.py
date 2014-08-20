'''This program contains some core functions for the games 2048: it basically 
consists in manipulating 2-D arrays
By Kouame KOUASSI
On 27 april 2014'''

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        x= [0]*4
        grid.append(x)
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""    
    #print the upper part of the frame
    print('+--------------------+')
    #print the array and the borders of the frame
    x = "{0:<5}"
    for i in range(4):
        for j in range(4):
            if j == 0:
                print('|',end='')
            if grid[i][j] == 0:
                print(x.format(' '),end = '')
            else:
                print(x.format(grid[i][j]),end='')
            if j == 3:
                print('|')
       
    #print the lower part of the frame
    print('+--------------------+') 
    
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #separate these conditions into tzo differents conditions
    condition_1 = True
    condition_2 = True
    #check if there are 0 values
    for i in grid:
        #i is assigned each sub_string and check if 0 is a value of i
        if 0 in i:
            condition_1 = False
            break
        else:
            continue
    #check if no adjacent values that are equal except the horizontally in row 4
    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
                condition_2 = False
                break
            else :
                continue
    #check horizontally for row 3 
    else:
        for i in range(3):
            if grid[3][i] == grid[3][i+1]:
                condition_2 = False
                break
            else:
                continue
    #return True if condition_1 stays True(0 not found) and as well as condition_2(not adjacent found)
    if condition_1 and condition_2:
        return True
    else:
        return False
    
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False""" 
    #i gets assigned each array in the grid
    for i in grid:
        #j gets assigned eah value in i
        for j in i:
            #check if a value in j in bigger than or equal to 32 and if so return True
            if j >= 32:
                return True
    #return False if value bigger than or equal to 32 not found
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    #create an empty grid
    grid_copy = create_grid([])
    for i in range(4):
        for j in range(4):
            grid_copy[i][j] = grid[i][j]
    return grid_copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False