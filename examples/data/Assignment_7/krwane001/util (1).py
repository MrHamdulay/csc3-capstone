def make_grid(grid):
    for i in range(4):
        grid.append([0]*4)
        
def output_grid(grid):
    print("+"+"-"*20+"+")
    for i in range():
        print("|",end="")
        for j in range(4):
            if grid[i][j]==0:
                print("    ",end="")
            else:
                print(str(grid[i][j]+(" "*(5-len(str(grid[i][j]))))),end="")
        print("|",end="")
    print("+"+"-"*20+"+")
    
def see_lost (grid):
    S = 0
    Z = 0
    for i in range(3):
        for j in range(1,4):
            if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j]:
                S=S+1
                break
   
    for i in range(4):
        if 0 in grid[i]:
            Z=Z+1
            break
    if S==0 and Z==0:
        return True
    else:
        return False
            
def see_won (grid):
    W = 0
    for i in range(4):
            for j in range(4):
                if grid[i][j] >= 32:
                    W = W+1
                    break
    if W == 0:
        return False
    else:
        return True
                
def copy_grid (grid):
    C = []
    for i in range(4):
        C.append([0]*4)
    for i in range(4):
        for j in range(4):
            copy[i][j] = grid[i][j]
    return C

def grid_same (g1, g2):
    if g1 == g2:
        return True
    else:
        return False