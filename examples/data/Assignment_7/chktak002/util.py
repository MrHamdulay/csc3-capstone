grid = []


def create_grid (grid):
    """create a 4x4 grid"""

    for i in range(4):
       
        grid.append([0]*4)   
    
def print_grid(grid):
    
    print("+" + "-"*20 + "+") #boarder of width 20 characters
    
    for row in range(4):
        
        for col in range(4):   #creates 5 width columns
            if grid[row][col] == 0:
                x = " "
            
                if col == 0:  
                    print ("|" + "{0:5}".format(x),end = "")   
                elif col == 3:
                    print ("{0:5}".format(x) + "|",end = "")                   
                else: 
                    print ("{0:5}".format(x),end = "") 
            else:
                
                if col == 0:  
                    print ("|" + "{0:5}".format(str(grid[row][col])),end = "")   
                elif col == 3:
                    print ("{0:5}".format(str(grid[row][col])) + "|",end = "")                   
                else:
                    print ("{0:5}".format(str(grid[row][col])),end = "")                
                   
        print()
    print("+" + "-"*20 + "+")   
    
def check_lost(grid):   
    
    valid = False
    for row in range (3):
            
            for col in range (3):
                
                x = grid[row][col]  
            
                if grid[row][col]==" " or grid[row][col]==grid[row][col-1]:  #Check every item , check of they are spaces or equal to the item to the left of it
                    return False    
                
    for row in range (3):
        
        for col in range (3):
            
            x = grid[row][col]  
            
            if grid[row][col]==" " or grid[row][col]==grid[row][col+1]:  #Check every item and check of they are spaces or equal to the item to the right of it 
                return False 
            
    for row in range (3):
        
        for col in range (3):
            
            x = grid[row][col]  
        
            if grid[row][col]==" " or grid[row][col]==grid[row-1][col]:  #Check every item in the 2D array, and check of they are spaces or equal to the item above it
                return False  
           
            
    for row in range (3):
                   
        for col in range (3):
                       
            x=grid[row][col]  
                       
            if grid[row][col]==" " or grid[row][col]==grid[row+1][col]:  #Check every item in the 2D array, and check of they are spaces or equal to the item below it
                return False               
            
    return True

def check_won(grid):
    valid = False
    for row in range(4):
            
        for col in range(4):
            if grid[row][col] != " ":
                if grid[row][col] >= 32:  #Check if the value is greater than 32
                    valid = True  
    return valid

def copy_grid(grid):
    c_grid = []     
    for i in range(4):
        c_grid.append([0]*4)    
    
    for row in range(4):    #Iterate through the old grid, and assign every corresponding value to the grid copy
        for col in range(4):
            c_grid[row][col] = grid[row][col]
    
    return c_grid  

def grid_equal (grid1, grid2):
    
    if grid1 == grid2:
        return True
    else:
        return False