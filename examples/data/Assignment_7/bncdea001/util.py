#Module of utility functions
#Dean Bunce
#27 April 2014

def create_grid(grid):  
    #Create 2D array
    for row in range(4):
        grid.append([0]*4)
        
    return grid

def print_grid(grid):
    
    #Print out a 4x4 grid in 5-width columns within a box
    
    print("+--------------------+")
    
    
    for i in range(4):
        print("|",end="")
        for x in grid[i]:
            if x==0:  print("{0:<5}".format(" "),end="")
            else: print("{0:<5}".format(x), end="")
        print("|")
    print("+--------------------+")
    
def check_lost(grid):
    
    #Set variable
    lose_0=True
    #Check grid for 0
    for i in range(4):
        for x in grid[i]:
            if x==0: lose_0=False
                
    #Set variable       
    lose_ineq=True
    
    #Check rows
    for row in range(3):
       
        
        #Check Rows
        for column in range(3):
            if grid[row][column]==grid[row+1][column]:
                    lose_ineq=False            
            if grid[row][column]==grid[row][column+1]:
                lose_ineq=False
            
    if lose_0==False or lose_ineq==False:
        return False
        
            
    else: return True

def check_won(grid):
    #Look through grid for number 32 or greater
    for i in range(4):
        for x in grid[i]:
            if x>=32:
                return  True
    else: return False

#Create a deep copy of the grid
def copy_grid(grid):
    import copy
    for row in range(4):
            grid.append([0]*4)
    grid_2=copy.deepcopy(grid)
    
    return grid_2
    
#Check if 2 grids are equal
def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True
    else:return False
