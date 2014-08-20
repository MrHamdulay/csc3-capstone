import copy            #to use deepcopy



def create_grid(grid):
    #grid = []
    #height = 4
    for i in range(4):
            grid.append([0,0,0,0]) 


def print_grid (grid):   #print out a 4x4 grid in 5-width columns within a box
   
    
    print('+--------------------+')
    for row in range(4):        
        print("|",end="")
        for col in range(4):
            if grid[row][col]==0:
                grid[row][col]=" "
                print("{0:<5}".format(grid[row][col]),end="")
            else:
                print("{0:<5}".format(grid[row][col]),end="")
        print("|")
    print('+--------------------+')          
        


    
def check_lost(grid):                 #return false where you still have the ability to continue playing the game otherwise returning true
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0: 
                return False
    for row in range(4):
        for col in range(4):
            specific_grid=grid[row][col]
            if 0<=col+1<4:
                if specific_grid == grid[row][col+1]:
                    return False
            if 0<col-1<4:
                if specific_grid == grid[row][col-1]:
                    return False
            if 0<=row+1<4:
                if specific_grid == grid[row+1][col]:
                    return False
            if 0<row-1<4:
                if specific_grid == grid[row-1][col]:
                    return False            
                
    return True


def check_won(grid):        #return True if a value>=32 is found in the grid; otherwise False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                return True
        
    return False 
 
 
def copy_grid (grid):        #return a copy of the grid
    gridcopy = copy.deepcopy(grid) 
    
    return gridcopy
    
    
def grid_equal (grid1, grid2):    #check if 2 grids are equal - return boolean value
    global gridcopy
    global grid
    gridcopy = grid1
    grid = grid2
    
    if gridcopy == grid:
        
        return True
    else:
        return False
        



    
            

                
