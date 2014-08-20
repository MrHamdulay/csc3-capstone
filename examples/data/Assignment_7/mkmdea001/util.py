grid=[]

def create_grid (grid):
    for i in range(4):
        grid.append([0]*4)

    
def print_grid (grid):
    print("+"+"-"*20+"+")
    for row in range (4):
        for col in range (4):
            if grid[row][col]==0:
                grid[row][col]=" "
            if col==0:
                print ("|"+"{0:5}".format(str(grid[row][col])),end="")   
            elif col==3:
                print ("{0:5}".format(str(grid[row][col]))+"|",end="")
            else:
                print ("{0:5}".format(str(grid[row][col])),end="")
                     
        print()
    print("+"+"-"*20+"+")   
    
def check_lost(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col]== " ":
                grid[row][col]=0
            elif grid[row][col]==0 or grid[row][col]==grid[row][col+1]:
                return False
            elif grid[row][col]==0 or grid[row][col]==grid[row+1][col]:
                return False
    return True
            
               
            
               
    
    
            
def check_won(grid):
    valid=False 
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                valid = True 
    return valid 

def copy_grid(grid):
    return grid
    
def grid_equal (grid1, grid2):
    if grid1 == grid2:
        return True
    else:
        return False 