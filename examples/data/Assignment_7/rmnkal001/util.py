#Kalind Ramnarayan
#27 April 2014
#module to manipulate 2D-lists

import copy

def create_grid(grid):
    for i in range (4):
        grid.append([0]*4)

def print_grid (grid):
    
    print("+--------------------+")
    for i in grid:
        print("|",end="")
        for j in i:
            if j==0:
                print(" "," "*(4-len(str(j))),end="")
            else:
                print(j," "*(4-len(str(j))),end="")
        print("|",end="")
        print()
    print("+--------------------+")

def check_lost (grid):
    tempGrid=[]
    for i in range (5):
            tempGrid.append([-1]*5) 
            
    for i in range (4):
        for j in range(4):
            tempGrid[i][j]=grid[i][j]
    
    for i in range(4):
        for j in range(4):
            if tempGrid[i][j]==0 or tempGrid[i][j]==tempGrid[i][j+1] or tempGrid[i][j]==tempGrid[i+1][j]:
                return False
                            
    else:
        return True    

def check_won (grid):
    for i in grid:
        for j in i:
            if j>=32:
                return True
    else:
        return False
    
            
            
def copy_grid (grid):
    grid2=copy.deepcopy(grid)
    return grid2
        
        
def grid_equal (grid1, grid2):
    for i in range (4):
        for j in range(4):
            if grid1[i][j]!=grid2[i][j]:
                return False
                break
                
    else:
        return True
                
            
              
                
            
            
                

    

