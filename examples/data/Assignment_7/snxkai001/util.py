def create_grid (grid):
    for u in range(4):
        grid.append([])
        for down in range(4):
            grid[u].append(0)
    

def print_grid(grid):
    print("+" + "-"*20 + "+")
    allign= "{0:" "<5}"
    for row in range(4):
        print("|", end="")
        for col in range(4):
            if grid[row][col] != 0:
                print(allign.format(grid[row][col]), end="")
            
            else:
                print(allign.format(" "), end= "")
        
        
        
        print("|")   
    print("+" + "-"*20 + "+")
    

def check_lost(grid):
    
    for kol in range(4):
            for lef in range(4):
                if grid[kol][lef]==0:
                    return False
                else:
                    continue
                   
        
    
    

    for n in range(4):
        for m in range(3):
            if grid[m][n]==grid[m+1][n]:
                return False
            else:
                continue
            
            
    for i in range(4):
            for j in range(3):
                if grid[i][j]==grid[i][j+1]:
                    return False
                else:
                    continue        
               
               
    return True
  
    
    
def check_won(grid):
    for i in range(4):
            for p in range(4):
                if grid[i][p]>=32:
                    return True
                
                else:
                    continue
                    
                    
    return False


def grid_equal(grid1, grid2):
    
    for i in range(4):
        for j in range(4):
            if grid1[i][j]==grid2[i][j]:
                continue
            else:
                return False
            
    return True

def copy_grid(grid):
    list1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    
    for col in range(4):
        for row in range(4):
            list1[col][row]=grid[col][row]
            
    return list1
                
           

