def create_grid(grid):
    #create a 4x4 grid
    for i in range(4): 
        grid.append([0]*4)  #fill in grid with 0's
        
def print_grid(grid): 
    #print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    
    #loop over entire grid
    for row in range(4):
        print("|", end="") #print out "|" at the beginning of every row
        for col in range(4):
            if grid[row][col]==0:  #if the vale of the grid is 0:
                print("{0:<5}".format(" "), end="") #Use a field width of 5, replace the 0 with a space and left align it
            else:
                print("{0:<5}".format(grid[row][col]), end="") #if the value of the grid is not 0, use a field width of 5 and left align it the value
        print("|") #print out "|" at the end of every row
    print("+--------------------+")
    
def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    
    #loop over entire grid:
    for row in range(4):
        for col in range (4):
            if grid[row][col]==0: #if a 0 is found in the grid, return False
                return False
            #else, if no 0 if found, for every row, compare grid[row][0] to grid[row][1], grid[row][1] to grid[row][2] and grid[row][2] to grid[row][3], and return False if any of the pairs of compared values are equal.
            elif col<3:  
                if grid[row][col]==grid[row][col+1]:
                    return False 
                
                
    #loop over entire grid
    #for every col, compare grid[0][col] to grid[1][col], grid[1][col] to grid[2][col] and grid[2][col] to grid[3][col], and return False if any of the pairs of compared values are equal.            
    for col in range(4):
        for row in range(4):
            if row<3:
                if grid[row][col]==grid[row+1][col]:
                    return False            
    return True #if there are no 0 values and no adjacent values that are equal, return True

def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    
    for row in range(4):
            for col in range (4):  #loop over entire grid:
                if grid[row][col]>=32:  #If a value>=32 is found, return True
                    return True  
    return False  #If all values in the grid are less than 32, return False

def copy_grid (grid):
    #return a copy of the grid
    
    #create a grid, which you fill with 0's:
    new_list=[]
    for i in range(4):
            new_list.append([0]*4)
            
    #loop over the OLD grid (before the reassignments) and over new_list     
    for col in range(4):
        for row in range(4):
            new_list[row][col]=grid[row][col] #change all the values in new_list (the 0's) with the values from OLD grid, i.e, COPY THE OLD GRID into new_list.
    return new_list #return new_list, which is simply a copy of the OLD grid
         

def grid_equal (grid1, grid2):
    #check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True #return True if the grids are equal
    return False #return Flase if the grids are not equal
    