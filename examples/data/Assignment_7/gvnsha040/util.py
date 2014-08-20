def create_grid (grid):
    for i in range(4):
        grid.append([])

        for k in range(4):
            grid[i].append(0)
    
    
def print_grid(grid):
    
    print ("+" + "-"*20 + "+")
    
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
    



def check_won(grid):
    
   
    for p in range(4):
        
        for n in range(4):

            if grid[p][n] >= 32:
                return True

            else:
                continue
            
        
    return False



def copy_grid(grid):
    new_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    for d in range(4):
        
        for g in range(4):
            new_grid[d][g] = grid[d][g]
            
    return new_grid



def grid_equal(grid1, grid2):
    
    for d in range(4):
        
        for g in range(4):
            if grid1[d][g] == grid2[d][g]:
                continue
            else:
                return False
            
    return True


def check_lost(grid):

    for i in range(4):        

        for j in range(3):

            if grid[i][j] == grid[i][j+1]:
                return False

            else:
                continue
            
    
    
    for x in range(4):

        for y in range(3):

            if grid[y][x] == grid[y+1][x]:
                return False

            else:
                continue
            
            
    for s in range(4):
        for g in range(4):
            
            if grid[s][g] == 0:
                return False
            else:
                continue
            
    return True