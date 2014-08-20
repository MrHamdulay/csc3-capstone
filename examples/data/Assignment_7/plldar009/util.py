def create_grid (grid):
    for i in range(4):
        grid.append([])
        for d in range(4):
            grid[i].append(0)
            
    
def print_grid(grid):
    
    print("+" + "-"*20 + "+")
    
    form = "{0:" "<5}"
    
    for i in range(4):
        print("|", end="")
        
        for k in range(4):
            if grid[i][k] != 0:
                print(form.format(grid[i][j]), end="")
            
            else:
                print(form.format(" "), end= "")
        
        print("|")
        
    print("+" + "-"*20 + "+")
    

def check_lost(grid):
    
    for i in range(4):        
        for d in range(3):
            if grid[i][d] == grid[i][d+1]:
                return False
            else:
                continue
            
    
    for s in range(4):
        for t in range(3):
            if grid[t][s] == grid[t+1][s]:
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
        for d in range(4):
            if grid[i][d] >= 32:
                return True
            else:
                continue
            
        
    return False

def copy_grid(grid):
    new_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
   
    for i in range(4):
        
        for d in range(4):
            new_grid[i][d] = grid[i][d]
           
    return new_grid



def grid_equal(grid1, grid2):
    
    for i in range(4):

        for s in range(4):
            if grid1[i][s] == grid2[i][s]:

                continue
            
            else:

                return False      
    return True