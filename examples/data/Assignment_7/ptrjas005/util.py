'''Jason Pietersen'''
def create_grid(grid):
#create a 4x4 array
    for i in range(4):
        grid.append([0]*4)
    
def print_grid(grid):
#print_grid
    form= '{0:<5}'
    #top
    print('+--------------------+')
    
    #middle
    for row in range(4):
        for col in range(4):
            if col == 0:
                print('|',end='')
            if grid[row][col]==0:
                print(form.format(' '),end='')
                
            else:
                print(form.format(str(grid[row][col])),end='')
        print('|') 
    #bottom
    print('+--------------------+')

def check_lost(grid):
    for row in range(3):
        for col in range(4):
            if grid[row][col]==0 or grid[row+1][col]==grid[row][col]:
                return False
    for row in range(4):
            for col in range(3):
                if grid[row][col]==0 or grid[row][col+1]==grid[row][col]:
                    return False 
    return True

def check_won(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:
                return True
    return False

def copy_grid(grid):
    grid_2=[]
    for i in range(4):
        grid_2.append([0]*4)    
    
    for row in range(4):
        for col in range(4):
            grid_2[row][col] = grid[row][col]
            
    return grid_2

def grid_equal (grid1,grid2):
    if grid1==grid2:
        return True
    return False