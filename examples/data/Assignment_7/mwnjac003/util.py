# module of utility functions
# by Jacob Mwanza
# 1/05/2014

length = 4

def create_grid(grid):
    
    # create a 4x4 grid
    for i in range(length):
        grid.append(['0']*4)
    return grid
        
def print_grid (grid):
    
    # print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    formatted_output = ('{0:<5}')
    for i in range (length):
        print('|',end = '')
        for k in range (4):
            temp = int(grid[i][k])
            if (temp == 0):
                print(formatted_output.format(' '), end='')
        
            else:
                
                print(formatted_output.format(temp), end=''),
        print('|', end = '')
        print()
    print("+--------------------+")          

def check_lost (grid):
    
    # return True if there are no 0 values and no adjacent values that are equal; otherwise False
    count = 0
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                count += 1
                
    if count == 0:
        return True
    else: 
        return False
    
    
def check_won (grid):
    count1 = 0
    
    # return True if a value>=32 is found in the grid; otherwise False
    for row in range(4):
        for col in range(4):
            if int(grid[row][col]) >= 32:
                count1 += 1
                
    if count1 == 0:
        return False
    else: 
        return True
    
def copy_grid (grid):
    copied_grid = []
    create_grid(copied_grid)
    for row in range(4):
            for col in range(4):
                copied_grid[row][col] = grid[row][col]   
    
    # return a copy of the grid
    return copied_grid

def grid_equal (grid1, grid2):
    count2 = 0
    
    # check if 2 grids are equal - return boolean value
    for row in range(4):
        for col in range(4):
            if grid1[row][col] == grid2[row][col]:
                count2 += 1
                
    if count2 < 16:
        return False
    else:
        return True