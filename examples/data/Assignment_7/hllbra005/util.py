def create_grid (grid):
    #code here
    
    for i in range (4):
        grid.append ([] * 4)      
        
    
def print_grid (grid):
    #Code here
    print ("+" + "-"*20 + "+")
    for row in range (4):
        print ("|", end ="")
        for col in range (4):
            if grid[row][col]==0:
                grid[row][col]==" "
                print ("{0:<5}".format(grid[row][col]), end = "")
            print ("|")
    print ("+" + "-"*20 + "+")
                 
            
     
def check_lost (grid):
    lost = True
    for row in range (4):
            for col in range (4):
                if ( (grid[row][col])== grid[row][col+1] or grid[row][col]== grid[row+1][col] 
                     or grid[row][col]== grid[row][col-1] or grid[row][col]== grid[row-1][col]):    
                    lost = False
    for row in range (4):
        for col in range (4):
            if ( (grid[row][col])==' '):
                lost = False                    
    return lost

         
    
def check_won (grid):
    for row in range (4):
        for col in range (4):
            if ( (grid[row][col])==2048):
                return True           
    
def copy_grid (grid):
    a = copy.deepcopy(grid)
     
    return a
    #code
    
def grid_equal (grid1, grid2):
    equals = False
    if (grid1 ==grid2):
        equals = True
    return equals    
    
        
    
