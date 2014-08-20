def create_grid (grid):
    for i in range(4):
        grid.append([])
        for j in range(4):
            grid[i].append(0)
    
def print_grid(grid):
    
    print("+" + "-"*20 + "+")
    
    form = "{0:" "<5}"
    
    for i in range(4):
        print("|", end="")
        
        for j in range(4):
            if grid[i][j] != 0:
                print(form.format(grid[i][j]), end="")
            
            else:
                print(form.format(" "), end= "")
        
        print("|")
        
    print("+" + "-"*20 + "+")
    
def check_lost(grid):
    for i in range(4):        
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                return False
            else:
                continue
    for n in range(4):
        for m in range(3):
            if grid[m][n] == grid[m+1][n]:
                return False
            else:
                continue      
    for k in range(4):
        for l in range(4):
            if grid[k][l] == 0:
                return False
            else:
                continue
            
    return True

def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
            else:
                continue
            
        
    return False

def copy_grid(grid):
    new_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][j]
            
    return new_grid

def grid_equal(grid1, grid2):
    
    for i in range(4):
        for j in range(4):
            if grid1[i][j] == grid2[i][j]:
                continue
            else:
                return False
            
    return True
