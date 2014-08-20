#DenishaRamaloo
#util
def create_grid (grid):
    for i in range(4):
        grid.append([0,0,0,0])
    return grid

def print_grid(grid):
    print("+--------------------+")
    for i in range(4):
        print("|",end="")
        for j in range(4):
            if(grid[i][j]==0):
                print("{:<5}".format(" "),end="")
            else:
                print("{:<5}".format(grid[i][j]),end="")
        print("|",end="")    
        print()
    print("+--------------------+")



def check_won (grid):
    for i in range(4):
        for j in range(4):
            if(grid[i][j]>=32):
                return True
    return False

def check_lost(grid):
    for i in range(4):
        for j in range(4):
            if(grid[i][j]==0):
                return False
            if(j<3 and grid[i][j]==grid[i][j+1]):
                return False
            if(i<3 and grid[i][j]==grid[i+1][j]):
                return False
    
    return True

def copy_grid(grid):
    copy=[['','','',''],['','','',''],['','','',''],['','','','']]
    for i in range(4):
        for j in range(4):
            copy[i][j]=grid[i][j]
    return copy

def grid_equal (grid1, grid2):
    if(grid1==grid2):
        return True
    else:
        return False
            
            
    



                