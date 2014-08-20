"""Assignment 7 util module
functions for 2048 game
Shaheen Karodia
KRDSHA003
2014-04-27"""





def create_grid(grid):
    """create a 4x4 grid"""
    
    for i in range (4):
        grid.append([0]*4)    #append 1 row of the grid at a time
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")   #print top of box
    for row in range (4):
        print("|", end="")    #print left side of box 
        for col in range (4):
            if grid[row][col]==0:
                print(" "*5, end="")  #prints blank spaces if item is a zero
            else:
                print(grid[row][col], (5-len(str((grid[row][col]))))*" ", sep="", end="")   #justify output left in a collumn of width of 5
        print("|")           #print left side of box
        
    print("+--------------------+")  #print bottom of box
    
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range (4):
        for col in range (4):
            if grid[row][col]==0:   
                return False
            
            if row!=3:     #condition ensures that index is not out of range
                if grid[row][col]==grid[row+1][col]:
                    return False
                
            if col!=3:     #condition ensures that index is not out of range
                if grid[row][col]==grid[row][col+1]:
                    return False
    return True    
        

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range (4):
        for col in range (4):
            if grid[row][col]>=32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    copygrid=[]  #initialise variable
    
    for row in range(4):
        row_list=[]          #ensures variable is re-initilised after every iteration of the inner
        for col in range (4):
            row_list.append(grid[row][col])
        copygrid.append(row_list)    #appends entire rows at a time to copygrid
    return copygrid
        
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range (4):
        for col in range(4):
            if grid1[row][col]!=grid2[row][col]:
                return False
    return True