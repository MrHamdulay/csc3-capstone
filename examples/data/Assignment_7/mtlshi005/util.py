def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid

        
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*20,"+",sep="")
    for row in range (4):
            
            for col in range (4):
                    if grid[row][col]==0:
                            grid[row][col]=" "
                    if col==0:
                            print ("|{0:<5}".format(grid[row][col]),sep="",end="")   
                    elif col==3:
                            print ("{0:<5}".format(grid[row][col]),sep="",end="|")
                    else:
                            print ("{0:<5}".format(grid[row][col]),sep="",end="")
            print ()        
    print("+","-"*20,"+",sep="")           
     
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    value=True
    listv=[]
        
    for col in range (4):
        for row in range (4):                            #creating list to compare each number with previous one in a listv
                                            
            if grid[row][col]==0:
                value= False
            elif col==0:
                if row==0 and col==0:
                    if grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col+1]:     #check if value below is equal
                        value=False
                        
                elif row==3 and col==0:
                    if grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row-1][col]:     #check if value to the right is equal
                        value=False                        
                             
                                
                else:
                    if grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row-1][col]:     #check if value below is   equal
                        value=False
                             
                           
            elif col==1 or col==2:
                if row==0:
                    if grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row][col-1]:     #check if value below is equal
                        value=False
                                                   
                    elif row==3:
                        if grid[row][col]==grid[row][col-1] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row-1][col]:     #check if value below is equal
                            value=False
                             
                    else:
                        if grid[row][col]==grid[row][col-1] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row+1][col]:     #check if value to the left is equal
                            value=False
                        
                                    
            elif col==3:
                if row==0:
                    if grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col-1]:     #check if value below is equal
                        value=False
                             
                    elif row==3:
                             
                        if grid[row][col]==grid[row][col-1] or grid[row][col]==grid[row-1][col]:     #check if value to the left is equal
                            value=False                        
                            
                    else:
                        if grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col-1] :     #check if value below is  equal
                            value=False            
    
    
    return value    
                    
                  

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    
    value=False
    for row in range (4):
            for col in range (4):
                    
                    if grid[row][col]>=32:
                            value=True    
    return value

def copy_grid (grid):
    """return a copy of the grid"""
    grid2=[]
    
    for i in range(4):
        grid2.append([0]*4)              #Not working with 64
        
    
    for row in range(4):
        for col in range(4):
            grid2[row][col]=grid[row][col]
        
    return grid2
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    
    
    
    boo=True
    for row in range (4):
            for col in range (4):
                    if grid1[row][col]!=grid2[row][col]:
                            boo=False
                            
    return boo   
    


