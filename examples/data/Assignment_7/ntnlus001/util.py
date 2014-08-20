"""program about some boring assignment
Bitch ass nigga
01 May 2014"""

def create_grid(grid):
    """create a 4x4 grd"""
    
    for i in range(4):
        grid.append([0]*4)
        
        
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns a box"""
    print("+", "-"*20, "+", sep="")
    for i in range(4):
        print("|", end="")
        for n in range(4):
            if grid[i][n] == 0:
                print('{0:<5}'.format(' '), end='')
                continue
            print( '{0:<5}'.format(grid[i][n]), end='')
        print('|')
        
    print("+", "-"*20, "+", sep="")
        
def check_lost(grid):
    for i in range(3):
        for n in range(3):
            if grid[i][n]==grid[i+1][n]:
                return False
            elif grid[i][n]==grid[i][n+1]:
                return False            
            elif grid[i][n] == 0:
                return False
            
    return True
                
def check_won(grid):
    for i in range(4):
        for n in range(4):
            if grid[i][n]>=32:
                return True
            
    return False
            
def copy_grid(grid):
    for i in range(4):
        for n in range(4):
            new_grid[i][n]=grid[n][i]
    return new_grid
            

def grid_equal(grid1, grid2):
    for i in range(4):
        for n in range(4):
            if grid1[i][n]!=grid2[i][n]:
                return False
    return True

   