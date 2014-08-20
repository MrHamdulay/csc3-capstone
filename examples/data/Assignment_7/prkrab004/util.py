#Assignment 7
#Question 2
#Rabia Parker
#PRKRAB004
#Due Date: 02/04/14


def create_grid(grid):
    """create a 4x4 grid"""
    for x in range(4): #loop to create grid
        grid.append([0,0,0,0])
    return grid #show grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for x in range(4): #loop the '|'
        line="|"
        for y in range(4):
            item=str(grid[x][y])
            if item=='0':
                item=' '
            line+=item+' '*(5-(len(item))) 
        line+='|'
        print(line)
    print("+--------------------+")


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for x in range(4):
        for y in range(4):
            if grid[x][y]==0:
                return False
        for z in range(3):
            if grid[x][z]==grid[x][z+1] or grid[z][x]==grid[z+1][x]:
                return False
    else: return True
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for x in range(4):
        for y in range(4):
            if grid[x][y]>=32:
                return True
    else: return False

def copy_grid (grid):
    """return a copy of the grid"""
    for x in range(4):
        for y in range(4):
            grid[x][y]=str(grid[x][y])
    
    for z in range(4):
        grid[z]="/".join(grid[z])
    line="*".join(grid)
    copy=line.split("*")

    for r in range(4):
        copy[r]=copy[r].split('/')
        
    for w in range(4):
        for v in range(4):
            copy[w][v]=eval(copy[w][v])
            
    for q in range(4):
        grid[q]=grid[q].split('/')
    
    for d in range(4):
        for h in range(4):
            grid[d][h]=eval(grid[d][h])
    return copy
                            

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False

#end of program