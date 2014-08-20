grid = []
othergrid= []

def create_grid(grid):
    for i in range (4):
        grid.append ([0] * 4)        
    for i in range (4):
        othergrid.append ([0] * 4)    
    
def print_grid(grid):
    print('+','-'*20,'+',sep='')
    for row in range (4):
        print('|',end='')
        for col in range (4):
            
            if grid[row][col] == 0:
                print ('{0:<5}'.format(' '),sep='',end="")
            else:
                print ('{0:<5}'.format(grid[row][col]),sep='',end="")
        print ('|')        
    print('+','-'*20,'+',sep='')
    
def check_lost(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0: 
                return False
    for row in range(0,3):
        for col in range(4):            
            if grid[row][col] == grid[row+1][col]:
                return False
    for row in range(1,4):
        for col in range(4):    
            if grid[row][col] == grid[row-1][col]:
                return False
    for row in range(4):
        for col in range(0,3):    
            if grid[row][col] == grid[row][col+1]:
                return False
    for row in range(4):
        for col in range(1,4):    
            if grid[row][col] == grid[row][col-1]:
                return False
    return True
            
def check_won(grid):
    for row in range(4):
            for col in range(4):
                if int(grid[row][col]) >= 32:
                    return True
    return False
                
def copy_grid(grid):
    import copy
    new_grid = copy.deepcopy(grid)
    return new_grid

def grid_equal(grid1,grid2):
    if grid1 == grid2:
        return True
    else: return False
    
    
    
    
    
    