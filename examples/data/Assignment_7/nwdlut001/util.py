def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
    return grid
   
def print_grid(grid):
    print("+"+"-"*20+"+")
    for row in range(4):
        print("|",end='')
        for col in range(4):
            if grid[row][col]==0:
                print(' ',' '*(4-len(str(grid[row][col]))),end="")
            else:
                print(grid[row][col],' '*(4-len(str(grid[row][col]))),end="")
        print("|")
    print("+"+"-"*20+"+")



def check_lost(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return False
            elif grid[i][j]!=grid[i+1][j+1] and grid[i][j]!=grid[i-1][j-1] :
                return True
            else:
                return False

def check_won (grid):
    won = False
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                won = True
    return won
def copy_grid(grid):
    copygrid=[]
    for g in range(4):
        copygrid.append([0]*4)
    for i in range(4):
        for j in range(4):
            copygrid[i][j]=grid[i][j]
    return copygrid


def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True
    else:
        return False
