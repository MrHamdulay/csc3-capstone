def create_grid(grid):
    ''' create a 4x4 grid'''
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid(grid):
    print('+'+'-'*20+'+')
        
    for row in range (4):
        print('|',end='')
        for col in range (4):
            if grid[row][col]==0:
                print('{0:<5}'.format(''),end='')                
            else:
                print ('{0:<5}'.format(grid[row][col]),end='')
        print('|')   
    print ('+'+'-'*20+'+')

def check_lost(grid):
    for row in range (4):
        for col in range(4):
            if 0 not in grid[row] and grid[row][col] != grid[row][col+1] and grid[row][col] != grid[row+1][col]:
                return True
            
            elif 0 in grid[row] or grid[row][col] == grid[row][col+1] or grid[row][col] == grid[row+1][col]:
                return False

def check_won(grid):
    list=[]
    for i in range(4):
        for j in range(4):
            list.append(grid[i][j])
            
    if max(list) >= 32:
        return True
    elif max(list) < 32:
        return False
    
def copy_grid(grid):
    import copy
    new_grid = copy.deepcopy(grid)
    
    return new_grid

def grid_equal(grid1,grid2):
    grid1list=[]
    grid2list=[]
    for i in range(4):
        for j in range(4):
            grid1list.append(grid1[i][j])
            grid2list.append(grid2[i][j])
            
    if grid1list == grid2list:
        return True
    
    elif grid1list != grid2list:
        return False