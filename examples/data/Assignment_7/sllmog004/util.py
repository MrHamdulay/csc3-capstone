"""Assigment 7 Util
Yaseen Sulliman
29 April 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):                          
        grid.append([0,0,0,0])                  
    return grid                                 

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")             
    for i in range(4):                          
        string="|"                              
        for j in range(4):                      
            value=str(grid[i][j])               
            if value=='0':
                value=" "                       
            string+=value+" "*(5-(len(value)))  
        string+="|"                             
        print(string)                           
    print("+--------------------+")             

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):                          
        for j in range(4):                      
            if grid[i][j]==0:                   
                return False
        for k in range(3):
            if grid[i][k]==grid[i][k+1] or grid[k][i]==grid[k+1][i]:    #check if adjacent values are equal
                return False
    else: return True                           

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):                          
        for j in range(4):                      
            if grid[i][j]>=32:                  
                return True                     
    else: return False                          
    
def copy_grid(grid):
    """return a copy of the grid"""
    for i in range(4):                          
        for j in range(4):                      
            grid[i][j]=str(grid[i][j])          
    for k in range(4):                          
        grid[k]="/".join(grid[k])               
    string="*".join(grid)                       
    grid_copy=string.split("*")                 
    for l in range(4):
        grid_copy[l]=grid_copy[l].split('/')    
    for m in range(4):
        for n in range(4):
            grid_copy[m][n]=eval(grid_copy[m][n])
    for h in range(4):
        grid[h]=grid[h].split('/')              
    for p in range(4):
        for t in range(4):                      
            grid[p][t]=eval(grid[p][t])         
    return grid_copy                            

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:                            #check if two grids are identical
        return True
    else:
        return False