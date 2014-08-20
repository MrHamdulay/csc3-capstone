'''A program that manipulate 2-d arrays of size 4x4 
Jacob Ntesang
29 April 2014'''

#Create a 4x4 grid
def create_grid(grid):
    for i in range (4):
        grid.append([0]*4)
#Print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    out="{0:<5}"
    print("+--------------------+")
    for i in grid:
        print("|",end="")
        for j in i:
            if j == 0:
                print(out.format(""),end="")
            else:
                print(out.format(j),end="")
        print("|") 
        
    print("+--------------------+")
#check lost
def check_lost (grid):
    for x in range(4):
        if 0 in grid[x]:
            return False
        for y in range(4):
            if x > 0 and grid[x-1][y] == grid[x][y]:
                return False
            elif y > 0 and grid[x][y-1] == grid[x][y]:
                return False
    else:
        return True
                    
                    
                    
def check_won (grid):
    for i in grid:
            for j in i:
                if j >= 32:
                    return True    
                else:
                    continue
    return False
    
def copy_grid(grid):
#create a new grid but the same copy as the other one'''
    grid2=[]
    for i in range (4):
            grid2.append([0]*4)
    for col in range(4):
        for row in range(4):
            grid2[col][row] = grid[col][row]
    return grid2

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False
    
    
    
                    

    
    
        
            
            

    