def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
        
def print_grid(grid):
    print('+' + '-'*20 + '+')
    for row in range(4):
        print('|', end='')
        for col in range(4):
            if grid[row][col] == 0:
                print('     ', end='')  #dont make 0 an empty string,wont work in 2048.py
            else:
                x = "{0:<5}".format(grid[row][col])   #each column has a width of 5
                print(x, end='')
        print('|')
    print('+' + '-'*20 + '+')

def check_lost(grid): 
    i = True
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                i = False
    for row in range(4):
        for col in range(3):
            if grid[row][col] == grid[row][col+1]:
                i = False
    for row in range(3):
        for col in range(4):
            if grid[row][col] == grid[row+1][col]:
                i = False
    return i 
            
def check_won(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] > 31:
                return True
            else:
                continue
    return False
                
def copy_grid(grid):
    new_grid = []
    for i in range(4):
            new_grid.append([0]*4)    
    
    for row in range(4):
        for col in range(4):
            new_grid[row][col] = grid[row][col]
    return new_grid
        
def grid_equal(grid1, grid2):
    i = True
    for row in range(4):
        for col in range(4):
            if grid1[row][col] == grid2[row][col]:
                continue
            else:
                i = False
    return i        
            
            
    