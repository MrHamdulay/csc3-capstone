#grids
#mahdi marcus
#mrcmah001

def create_grid(grid):
    for i in range(4):              
        grid.append([0]*4)         
        
def print_grid(grid):
    print("+","-"*20,"+",sep="")
    for y in range(4):
        print("|",end="")
        for x in range(4):
            if grid[y][x]!=0:
                print("{0:<5}".format(grid[y][x]),end="")
            else:
                print("{0:<5}".format(""),end="")
        print("|")
    print("+","-"*20,"+",sep="")
    
def check_lost(grid):
    check=""
    for y in range(4):
        for x in range(4):
            if grid[y][x]==0:
                check="check"            
    for y in range(4):
        for x in range(3):
            if grid[y][x] == grid[y][x+1]:
                check="check"                
    for y in range(3):
        for x in range(4):
            if grid[y][x] == grid[y+1][x]:
                check="check"

        
    if check=="check":
        return False
    else:
        return True
        
        
def check_won(grid):            
    check=""
    for y in range(4):
        for x in range(4):
            if grid[y][x]>=32:
                check="check"
    if check=="check":
        return True
    else:
        return False

import copy
def copy_grid(grid):    
    duplicate=copy.deepcopy(grid)
    return duplicate

def grid_equal(GRID1,GRID2):
    if GRID1==GRID2:
        return True
    else:
        return False
    
        

    
        
        
        
        
    
            
                 
    