"""Raeesa Behardien
BHRRAE003
Assignment 7
Question 2
02 May 2014"""


def create_grid(grid):
    """create a 4x4 grid"""
    for a in range(4): 
        grid.append([0,0,0,0])
    return grid 

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for a in range(4): 
        symbol="|"
        for b in range(4):
            val=str(grid[a][b])
            if val=='0':
                val=' '
            symbol+=val+' '*(5-(len(val))) 
        symbol+='|'
        print(symbol)
    print("+--------------------+")


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for a in range(4):
        for b in range(4):
            if grid[a][b]==0:
                return False
        for c in range(3):
            if grid[a][c]==grid[a][c+1] or grid[c][a]==grid[c+1][a]:
                return False
    else: return True
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for a in range(4):
        for b in range(4):
            if grid[a][b]>=32:
                return True
    else: return False

def copy_grid (grid):
    """return a copy of the grid"""
    for a in range(4):
        for b in range(4):
            grid[a][b]=str(grid[a][b])
    
    #mirror to copy grid
    for c in range(4):
        grid[c]="/".join(grid[c])
    symbol="*".join(grid)
    mirror=symbol.split("*")

    for d in range(4):
        mirror[d]=mirror[d].split('/')
        
    for e in range(4):
        for f in range(4):
            mirror[e][f]=eval(mirror[e][f])
            
    for g in range(4):
        grid[g]=grid[g].split('/')
    
    for h in range(4):
        for i in range(4):
            grid[h][i]=eval(grid[h][i])
    return mirror
                            

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False

