from copy import copy, deepcopy

def create_grid(grid):

    
    for i in range(4):
        
        grid.append([0,0,0,0])
  

        
    

def print_grid(grid):
    print ("+--------------------+")
    
    for i in range(4):
        for j in range(4):
            if j == 0:
                print("|", end = "")

            if grid[i][j] == 0:
                print('{: <5}'.format(""), end = "")
            else:
                print('{: <5}'.format(grid[i][j]), end = "")


            if j == 3:
                print("|")
        
        
    print("+--------------------+")

def check_lost(grid):
    same = 0
    zero = 0
    for i in range(3):
        for j in range(1,4):
            if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j]:
                same+=1
                
                break
    #check for 0's
    for i in range(4):
        if 0 in grid[i]:
            zero+=1
            break
    
    if same==0 and zero==0:
        return True
    else:
        return False
            
        
                

def check_won(grid):
    cnt = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] >=32:
                return True
    return False

def copy_grid(grid):
    return deepcopy(grid)

def grid_equal(grid1,grid2):
    if grid1 == grid2:
        return True
    else:
        return False
    
grid = []
create_grid(grid)
            
        



