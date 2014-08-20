#Keanon Fell
#Assignment 7
#Question 2
#02 May 2014

#Creating functions that can be called from other programs
def create_grid(grid):
    #create a 4x4 grid
    for k in range(4): 
        grid.append([0,0,0,0])
    return grid 

def print_grid (grid):
    #print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    for k in range(4): 
        icon="|"
        for e in range(4):
            amount=str(grid[k][e])
            if amount=='0':
                amount=' '
            icon+=amount+' '*(5-(len(amount))) 
        icon+='|'
        print(icon)
    print("+--------------------+")


def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    for k in range(4):
        for e in range(4):
            if grid[k][e]==0:
                return False
        for a in range(3):
            if grid[k][a]==grid[k][a+1] or grid[a][k]==grid[a+1][k]:
                return False
    else: return True
    
def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    for k in range(4):
        for e in range(4):
            if grid[k][e]>=32:
                return True
    else: return False

def copy_grid (grid):
    #return a copy of the grid
    for k in range(4):
        for e in range(4):
            grid[k][e]=str(grid[k][e])
    
    for k in range(4):
        grid[k]="/".join(grid[k])
    icon="*".join(grid)
    twin=icon.split("*")

    for n in range(4):
        twin[n]=twin[n].split('/')
    
    for o in range(4):
        for f in range(4):
            twin[o][f]=eval(twin[o][f])
            
    for l in range(4):
        grid[l]=grid[l].split('/')
    
    for r in range(4):
        for d in range(4):
            grid[r][d]=eval(grid[r][d])
    return twin
                            

def grid_equal (grid1, grid2):
    #check if 2 grids are equal - return boolean value
    if grid1==grid2:
        return True
    else:
        return False