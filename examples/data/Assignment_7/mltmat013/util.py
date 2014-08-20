''' Assignment 7 Question 2
Matshepo Malatji MLTMAT013
2 May 2014'''

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append ([0] * 4)
        
           
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    sObj = '{0:<5}'
    print('+' + '-'*20 + '+',end ='')
    print()
    for row in range(4):
        print('|',end='')
        for col in range(4):
            if grid[row][col] == 0:
                print(sObj.format(' '),end='')
            else:
                print(sObj.format(grid[row][col]), end='')            
        print('|',end='')
        print()
    print('+' + '-'*20 + '+',end='')
    print()
     
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    flag = False
    #check if there are 0 values in the grid
    if 0 not in grid:
        flag = True
    else:
        flag = False
    #check if there are horizontally adjacent values that are equal
    second_flag = False
    counter = 0
    for row in range(4):
        for col in range(3):
            if grid[row][col] == grid[row][col+1]:
                counter += 1
    
    if  counter == 0:
        second_flag = True
    else:
        second_flag = False

    #check if there are vertically adjacent values that are equal    
    third_flag = False
    k = 0
    for row in range(3):
        for col in range(4):
            if grid[row][col] == grid[row+1][col]:
                k += 1
    if k ==0:
        third_flag = True
    else:
        third_flag = False
        
    if (flag == True) and (second_flag == True) and (third_flag == True):
        Marker = True
    else:
        Marker = False
        
    return Marker
    
    
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:
                return True
    return False
             
def copy_grid(grid):
    """return a copy of the grid"""
    new_grid = copy.deepcopy(grid)
    return new_grid
    

def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False

