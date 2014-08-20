def create_grid(grid):
    grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    return grid

def print_grid (grid):
    print('+'+'-'*20+'+')
    for i in grid:
        print('|',end='')
        for j in i:
            if j==0:
                print(' '.ljust(5),end='')
            else:
                print(str(j).ljust(5),end='')
        print('|')
    print('+'+'-'*20+'+')
    
def check_lost(grid):
    false='false'
    f_alse='f_alse'
    for row in range(4):
        for col in range(3):
            if grid[row][col]==0 or grid[row][col]==' ':
                false=1
            if grid[col][row]==grid[row][col+1]:
                false=1
            else:
                false = 0
            
    for row in range(3):
        for col in range(4):
            if grid[row][col]==0 or grid[row][col]==' ':
                f_alse=1
            if grid[col][row]==grid[row+1][col]:
                f_alse=1
            else:
                f_alse=0
                
    if false==1 or f_alse==1:
        return False
    else:
        return True
    
            
    
def check_won (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    else:
        return False
            
def copy_grid (grid):
    import copy
    Copy=copy.deepcopy(grid)
    return Copy
        
def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False
    