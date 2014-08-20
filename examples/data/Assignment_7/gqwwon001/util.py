# A module to get different utility functions for the 2048 game
# Wongwa Giqwa
# 28 April 2014

grid = []
def create_grid(grid):
     # create a 4x4 grid
    
    height = 4
    
    for i in range  (height) :
        grid.append ([0,0,0,0])
    #return grid
        
        #print()

def print_grid(grid):
    
    # create a border around the 4x4 grid
    
    print('+'+'--'*10+'+')
    
    for i in range(4):
        print("|",end='')
        for col in range(4):
            if grid[i][col] ==0:
                print('{0:<5}'.format(''), end='')
            else:
                print('{0:<5}'.format(grid[i][col]), end='')
        print("|")
    
    print('+'+'--'*10+'+')
    
  
   
def check_lost(grid):
    # return True if there are no 0 values and no adjacent values that are equal, otherwise return False
    
# create nested loops to go through rows(i) and columns(j) to check when the conditions apply
    
    for i in range (4):
        for j in range (4):
            if grid[i][j]==0:
                return False
            # checks adjacent rows and columns to see if any values are the same
    if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
        return False 
    if grid[0][3]==grid[0][2] or grid[0][3]==grid[1][3]:
        return False            
    if grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
        return False
    if grid[3][3]==grid[2][3] or grid[3][3]==grid[3][2]:
        return False 
    if grid[0][1]==grid[0][2] or grid[0][1]==grid[1][1]:
        return False 
    if grid[0][2]==grid[1][2]:
        return False    
    if grid[1][1]==grid[2][1] or grid[1][1]==grid[1][2] or grid[1][1]==grid[1][0]:
        return False
    if grid[2][1]==grid[2][0] or grid[2][1]==grid[2][2] or grid[2][1]==grid[3][1]:
        return False 
    if grid[1][0]==grid[2][0]:
        return False
    if grid[1][2]==grid[1][3] or grid[1][2]==grid[2][2]:
        return False
    if grid[2][2]==grid[2][3] or grid[2][2]==grid[3][2]:
        return False
    if grid[3][1]==grid[3][2]:
        return False
    else:
        return True           
            
            
                
def check_won(grid):
    # return true if a value >=32 is found in the grid, otherwise false
    
    decision=False 
    # create nested loop to go through the rows and columns to check if the conditions for winning apply
    for i in range (4):
        for j in range (4):
            if grid[i][j] >= 32:
                decision = True
                break
    return decision

def copy_grid(grid):
    # return a copy of the grid
    
    import copy
    new_grid = copy.deepcopy(grid)
    return new_grid

def grid_equal(grid1, grid2):
    # check if two grids are equal
    
    if grid1 == grid2:
        return True
    else:
        return False
            
            
            
            
    
    
    
    

