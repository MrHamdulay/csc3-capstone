
import copy

def create_grid(grid):
    for a in range(4):
        grid.append([" "]*4)
        
def print_grid(grid):
    print("+--------------------+") 
    #print inner box
    for row in range(4):
        print("|", end="")
        for col in range(4):
            if grid[row][col]== 0:
                print ( "{0:<5}".format(" "), end = "")
            else:
                print ( "{0:<5}".format(grid[row][col]), end = "")
        print("|")                
    print("+--------------------+") 
    
def check_lost(grid):
    #check no 0s
    foundZero = 0
    for y1 in range (4):
        for x1 in range(4):
            if grid[y1][x1] == 0:
                foundZero= -1
                break
   
    
    #check adjacent numbers
    
    #horizontal
    horizonatalAdj = 0
    for y2 in range(3):
        for x2 in range(3):
            if grid[y2][x2] == grid[y2][x2+1]:
                horizontalAdj = -1
                break
        
    #vertical
    verticalAdj = 0
    for y3 in range(3):
        for x3 in range(3):
            if grid[y3][x3] == grid[y3+1][x3]:
                verticalAdj = -1
                break
            
    if horizonatalAdj == -1 or verticalAdj == -1 or foundZero == -1:
        return False
    else:
        return True

def check_won(grid):
    found32 = 0
    for y in range(4):
        for x in range(4):
            if grid[x][y] >= 32:
                found32 = -1
    
    if found32 == -1:
        return True
    else:
        return False
    
                

def copy_grid(grid):
    newgrid=copy.deepcopy(grid)
    return newgrid


def grid_equal(grid, grid2):
    if grid == grid2:
        return True
    else:
        return False
    
    
            
        
            
       
                
