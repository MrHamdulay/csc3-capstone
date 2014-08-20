def create_grid(grid) :
    for x in range (4) :
        grid.append (["0"] * 4) 
     
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    #grid = [[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]
       
    for row in range (4):
        print("|",end="")
        for col in range (4):
            x=(grid[row][col])
            length =len(str(x))
            if x==0 :
                print(" ",(5-length)*" ",sep="",end="")
            else :
                print(x,(5-length)*" ",sep="",end="")
        print ("|")    
               
    print("+--------------------+")      
          
          
          
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    False
    for row in range (4):
        for col in range (4):    
            x=(grid[row][col])
            
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""

def copy_grid (grid):
    """return a copy of the grid"""

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    
#print_grid([])