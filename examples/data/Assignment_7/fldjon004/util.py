#Jono Field
#1 May 
#util.py

def create_grid(grid):   #create a 4x4 grid
    for p in range(4):
        grid.append([" "]*4)
    return grid


def print_grid(grid):  #print a 4 by 4 grid in 5-width columns
    print("+", "-"*20, "+", sep = "")
    for x in range (4):
        print('|', end = "")
        for y in range (4):
            if grid[x][y]==0:
                z = " "  #print space instead of 0
            else:
                z = grid[x][y]
            width_column = "{0:<5}".format(z)
            print(width_column, end = "")               
        print("|")
    print("+", "-"*20, "+", sep = "")
    
    
def check_lost(grid): #return True if there are no 0 values and no adjacent values that are equal, otherwise False
    for x in range (4):
        for y in range (4):
            if grid[x][y]==grid[x+1][y+1] or grid[x][y]==grid[x][y+1] or grid[x][y]==grid[x+1][y]:
                return False      
    return True
    
     
def check_won(grid): #return True if a value of >= 32 is found in the grid, otherwise False
    for x in range (4):
        for y in range (4):
            if grid[x][y]>=32:
                return True
    return False
            
            
def copy_grid(grid): #return a copy of the grid
    copy = [ [], [], [], [] ] 
    for x in range (4):        
        for y in range (4):            
            copy[x].append(grid[x][y])      
    return copy
            

def grid_equal(grid1, grid2): #check if 2 grids are equal - return boolean value
    for x in range (4):  #loop through to see if grids values are the same
        for y in range (4):
            if grid1[x][y]!=grid2[x][y]:
                return False        
    return True