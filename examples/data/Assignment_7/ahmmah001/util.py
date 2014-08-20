''''Program to manipulate 2D arrays
Mahnoor Ahmed
30 April 2014'''

import copy
count=0
grid=[] 

def create_grid (grid):
    for i in range(4):
        grid.append([0]*4)
    return(grid)

def print_grid(grid):
    grid=create_grid(grid)
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                grid[i][j]= " "
    print("+","-"*20,"+",sep="")
    print("|","{0:<5}".format(grid[0][0]),"{0:<5}".format(grid[0][1]),"{0:<5}".format(grid[0][2]),"{0:<5}".format(grid[0][3]),"|\n","|","{0:<5}".format(grid[1][0]),"{0:<5}".format(grid[1][1]),"{0:<5}".format(grid[1][2]),"{0:<5}".format(grid[1][3]),"|\n","|","{0:<5}".format(grid[2][0]),"{0:<5}".format(grid[2][1]),"{0:<5}".format(grid[2][2]),"{0:<5}".format(grid[2][3]),"|\n","|","{0:<5}".format(grid[3][0]),"{0:<5}".format(grid[3][1]),"{0:<5}".format(grid[3][2]),"{0:<5}".format(grid[3][3]),"|",sep="")
    print("+","-"*20,"+",sep="")

def check_lost(grid):
    grid=create_grid(grid)
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            
            elif grid[i][j] > 32:
                return False
            
            elif (i-1)>=0 and grid[i][j] == grid[i-1][j]:
                return False
            elif (j-1)>=0 and grid[i][j] == grid[i][j-1]:
                return False
            elif (i+1)<=3 and grid[i][j] == grid[i+1][j]:
                return False
            elif (j+1)<=3 and grid[i][j] == grid[i][j+1]:
                return False
            
    return True
                        
def check_won(grid):
    grid=create_grid(grid)
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    return False
                        
def copy_grid(grid):
    grid=create_grid(grid)
    new_grid= copy.deepcopy(grid)
    return(new_grid)

def grid_equal(grid1,grid2):
    count=0
    for i in range(4):
        for j in range(4):
            if grid1[i][j] == grid2[i][j]:
                count = count + 1
                        
    if count == 16:
        return True
    else:
        return False
    
        