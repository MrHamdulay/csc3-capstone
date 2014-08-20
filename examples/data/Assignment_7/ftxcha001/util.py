
"""Create a 4x4 grid"""

def create_grid(grid): 
    
    for i in range(4):
        grid.append([0]*4)
    return grid 

"""print out a 4x4 grid in 5-width columns within a box"""

def print_grid(grid): 
    print("+--------------------+") #print the top of the box 
    
    for row in range(4): #4 rows in the box excluding top and bottom 
        print("|", end = "") # printing left side of the box, only 1 | needed per row.
        
        for column in range(4): 
            if grid[row][column]==0:
                print(" "*5, end="") #printing spaces where there are 0 values in the box
            
            else:
                print(grid[row][column], (5-len(str((grid[row][column]))))*" ", sep="",end="")
                #width of column is 5. 
                
        print("|") #close box on the right hand side
        
    print("+--------------------+") #print the bottom of the box 
    
"""return True if there is no 0 values and no adjacent 
values that are equal, otherwise Falsese"""

def check_lost(grid):
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0:
                return False
            if row != 3:
                if grid[row][column] == grid[row+1][column]:
                    return False 
            if column != 3:
                if grid[row][column] == grid[row][column+1]:
                    return False 
    return True

"""return True if a value >=32 is found in the grid: otherwise False"""

def check_won(grid):
    for row in range(4):
        for column in range(4):
            if grid[row][column] >= 32:
                return True
    return False
    
"""return a copy of the grid"""

def copy_grid(grid):
    CopyGrid=[]
    
    for row in range(4):
        row_list=[]
        for column in range(4):
            row_list.append(grid[row][column])
        CopyGrid.append(row_list)
    return CopyGrid

"""check if 2 grids are equal - return boolean value"""

def grid_equal (grid1, grid2):
    for row in range(4):
        for column in range (4):
            if grid1[row][column] != grid2[row][column]:
                return False 
            
    return True 
            
    
            
    
    
    
    
            
    
                