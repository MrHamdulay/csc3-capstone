#mknnit002
#question2 ass 7

def create_grid(grid):
    """create a 4x4 grid"""
    
    for i in range (4):
        grid.append([0]*4)   #append each row of the grid one at a time
        return grid
    
def print_grid(grid):
    """print out 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")        #prints the top of the box
    for row in range(4):
        print("|", end="")   #prints the left side of the box
        for col in range (4):
            if grid[row][col]==0:
                print(" "*5, end="")   #prink blank spaces if item is a zero
            else:
                print(grid[row][col],(5-len(str((grid[row][col]))))*" ", sep="",end="")
        print("|") #print left of box
        
        
    print("+--------------------+") #print bottom of box
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for col in range (4):
            if grid[row][col]==0:
                return False
           
            if row!=3:
                if gird[row][col]==grid[row+1][col]:
                    return False
            if col!=3:
                if grid[row][col]==grid[row][col+1]:
                    return False
                    
                
    return True

def check_one(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if gird[row][col]>=32:
                return True
    return False

def copy_grid(grid):
    """return a copy of the grid"""
    copygrid=[]
    
    for row in reange(4):
        rowlist=[]
        for col in range (4):
            rowlist.append(grid[row][col])
        copygrid.append(rowlist)
    return copy_grid

def grid_equal(grid1, grid2):
    """check if two grids are equal- return boolean value"""
    for row in range(4):
        for col in range (4):
            if grid1[row][col]!=grid2[row][col]:
                return False
    return True

 
        
    
                   
            
    
    