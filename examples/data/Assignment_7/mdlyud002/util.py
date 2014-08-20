# Yudhi Moodley
# Assignment 7 - Repetition omission program
# 29/04/2014

import copy

def create_grid (grid):
    for i in range (4):
        grid.append([0]*4)

def print_grid (grid):
# print out a 4x4 grid in 5-width columns within a box 
    
    print("+--------------------+")

    # iterate through the grid:
    for i in range (4):

        # print left border  
        for r in range (4):
            if r == 0:   
                print("|",end="")
 
            # print the formatted value
            if grid[i][r] == 0:
                print("     ", end="")
            else:    
                print("{0:<5}".format(grid[i][r]),end='',sep='')
            
            # print the right border
            if r == 3:
                print("|",end="") 
        print() # leave a line for aesthetic appeal ;) arrrrrrrrrrr!
    print("+--------------------+")

def check_lost (grid):
#return True if there are no 0 values and no adjacent values that are equal; otherwise False
    
    # values to be tested
    noZero = 0
    noAdj = 0
    
    # check if any values are 0, exist                
    for i in range (4):
        
        for r in range (4):
            
            if grid[i][r] == 0:
                
                noZero += 1
    
    # check adjacent values           

    for i in range (1,2):
        
        for r in range (1,2):
            
            
            if (grid[i][r] == grid[i+1][r]) or (grid[i][r] == grid[i][r+1]):
                noAdj += 1
                
    # return the appropriate boolean 
    if (noAdj == 0) and (noZero == 0):
        return True
    
    else:
        return False          

def check_won (grid):
# return True if a value>=32 is found in the grid, otherwise False
    check = 0 # this value is used to keep track of values >= 32
    # iterate through the grid:
    for i in range (4):
        for j in range (4):
            if grid[i][j] >= 32: # if a grid value is >= 32
                check = check+1 # increase check
            else:
                check += 0 # do nothing with check
                
    # check if check has recorded a value >= 32            
    if check > 0:
        return True
    else:
        return False            
    
def copy_grid(grid):
#return a copy of the grid
    
    grid2 = copy.deepcopy(grid) # use deepcopy function to copy grid because I'm not so shallow ;)
    return grid2

def grid_equal (grid1, grid2):
# check if 2 grids are equal - return boolean value '''
    
    checkEq = 0 # value used to store number of equal values
    
    for i in range (4):
        
        for r in range (4):
            
            if grid1[i][r] == grid2[i][r]:
                checkEq +=1 # if 2 corresponding values are equal, add one to checkEq
    if checkEq == 16: # if 2 grids are identical, checkEq should be 16
        return True
    
    else:
        return False