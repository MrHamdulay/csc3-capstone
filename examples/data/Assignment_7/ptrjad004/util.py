"""question 2
Jade Petersen
29 April 2014"""


def create_grid(grid):#create a 4x4 grid
    for i in range (4):
        grid.append ([0] * 4)    
        
def print_grid (grid):#print out a 4x4 grid in 5-width columns within a box
    import copy
    g=copy.deepcopy(grid)
    for row in range(4):
        for col in range(4):
            if g[row][col]==0:
                g[row][col]=" "
    print("+", "-"*20, "+", sep="")
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(g[0][0],g[0][1],g[0][2],g[0][3]),"|",sep="")
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(g[1][0],g[1][1],g[1][2],g[1][3]),"|",sep="")
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(g[2][0],g[2][1],g[2][2],g[2][3]),"|",sep="")
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(g[3][0],g[3][1],g[3][2],g[3][3]),"|",sep="")
    print("+", "-"*20, "+", sep="")
    
   
def check_lost (grid):#return True if there are no 0 values and no adjacent values that are equal; otherwise False
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0:
                return False
    if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
        return False 
    if grid[0][3]==grid[0][2] or grid[0][3]==grid[1][3]:
        return False            
    if grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
        return False
    if grid[3][3]==grid[2][3] or grid[3][3]==grid[3][2]:
        return False 
    if grid[0][1]==grid[0][2] or grid[0][1]==grid[1][1]:
        return False 
    if grid[0][2]==grid[1][2]:
        return False    
    if grid[1][1]==grid[2][1] or grid[1][1]==grid[1][2] or grid[1][1]==grid[1][0]:
        return False
    if grid[2][1]==grid[2][0] or grid[2][1]==grid[2][2] or grid[2][1]==grid[3][1]:
        return False 
    if grid[1][0]==grid[2][0]:
        return False
    if grid[1][2]==grid[1][3] or grid[1][2]==grid[2][2]:
        return False
    if grid[2][2]==grid[2][3] or grid[2][2]==grid[3][2]:
        return False
    if grid[3][1]==grid[3][2]:
        return False
    else:
        return True
    
def check_won (grid):#return True if a value>=32 is found in the grid; otherwise False
    w=False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                w=True
                break
    return w
                
def copy_grid (grid):#return a copy of the grid
    import copy
    g=copy.deepcopy(grid)
    return g

def grid_equal (grid1, grid2):#check if 2 grids are equal - return boolean value
    if grid1 == grid2:
        return True
    else:
        return False