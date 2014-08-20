"""assignment 7, q2- create functions to use in q3
emma jordi
27 april 2014"""

def create_grid(grid):
    #create a 4x4 grid
    for i in range (4):
        grid.append ([0] * 4) 
    return (grid)

def print_grid(grid):
    #create format string
    f="{0:<5}"
    #print out grid
    print("+--------------------+")
    for row in range (4):
        print("|", end="")
        for col in range (4):
            #make 0 into " "
            if grid[row][col]==0:
                print("     ",end='')
            else:
                print (f.format(grid[row][col]),end="")
            
        print ("|") 
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #no two equal numbers in horizontal or vertical. go thorugh grid in both directions.
    #Use true/false
    zero = 0
    same = 0
    #check for zeros
    for row in range(4):
        for col in range (4):
            #if there is a zero, then not true (=1)
            if grid[row][col] == 0:
                zero += 1
                break
     #check for same      
    for row in range(1,4): 
        for col in range(1,4):
            if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col-1]:
                same += 1
                break
    
    if zero == 0 and same == 0:
        return True
    else:
        return False
            
                
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    #look for number 32. while no block >=32, then continue playing
    won=0
    for row in range(4):
        for col in range(4):
            if grid[row][col]>= 32:
                won+=1
    if won==1:
        return True 
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    #create newgrid as new array with all 0's.
    newgrid=[]
    for i in range (4):
            newgrid.append ([0] * 4) 
        
    for row in range(4):
        for col in range(4):
            #newgrid is the same as the old grid. each position in newgrid = each position in old
            newgrid[row][col]= grid[row][col]
    return newgrid
    
    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    #can check for lequality
    if grid1== grid2:
        return True
    else:
        return False
    