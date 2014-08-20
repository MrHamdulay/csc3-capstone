'''Game grid
Frans Ledwaba
3 May 2014'''

def grid(grid):
    #create 2D array
    grid = []
    height = 4
    for i in range(height):
        grip.append([0]*4)
        
    #change coordinate variables
    for x in range(height):
        for y in range(height):
            grid[x][y] = x + y

def print_grid(grid):
    print('+-------------------------+')
    for x in range(height):
        for y in range(height):
            print('|', grid[x][y], '|' sep='')
    print('+-------------------------+')
    
def check_lost(grid):
    #lossing parameters
    for x in range(height):
        for y in range(height):    
            if grid[x][y] == grid[x+1][y] or grid[x][y] == grid[x-1][y] or grid[x][y] == grid[x][y-1] or grid[x][y+1]:
                return True
        else: return False

def check_won(grid):
    #winning parameters
    for x in range(height):
        for y in range(height):
            if grid[x][y] >= 32:
                return True
            else: return False

def copy_grid(grid):
    grid == grid1

def grid_equal(grid1, grid2):
    if grid1[x][y] == grid2[x][y]:
        return grid1[x][y] + grid2[x][y]
        