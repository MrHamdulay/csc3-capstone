#Author: NLXALE001
#Date: 30 April 2014
#Assignment 7

#doesn't work!!!
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (0,4):
        grid.append([0,0,0,0])
    return (grid)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print ("+--------------------+")
    #format to width 5
    out = "{0:" "<5}"
    for i in range (0,4):
        if grid[i][0]==0:
            grid[i][0]=""
        if grid[i][1]==0:
            grid[i][1]="" 
        if grid[i][2]==0:
            grid[i][2]="" 
        if grid[i][3]==0:
            grid[i][3]=""        
        print ("|", out.format(grid[i][0]), out.format(grid[i][1]), out.format(grid[i][2]), out.format(grid[i][3]), "|", sep="")
    print ("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost = True
    for i in range (0,4):
        for j in range (0,4):
            if grid[i][j]==0:
                lost = False
                break
            if i<3 and j<3: #make sure index will be in range
                if grid[i][j]==grid[i][j+1]: #compare to one next to it
                    lost = False
                    break
                if grid[i][j]==grid[i+1][j]: #compare to one below it
                    lost = False
                    break                    
    return (lost)

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range (0,4):
        for j in range (0,4):
            if grid[i][j]=='':
                grid[i][j]=0
    won = False
    for i in range (0,4):
        for j in range (0,4):  
            if grid[i][j]>=32:
                won = True
                break
    return(won)

def copy_grid (grid):
    """return a copy of the grid"""
    newgrid = [["","","",""], ["","","",""], ["","","",""], ["","","",""]]
    for i in range (0,4):       
        for j in range (0,4):
            newgrid[i][j]=grid[i][j]
    return (newgrid)

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal = True
    for i in range (0,4):
        for j in range (0,4):
            if grid1[i][j]!=grid2[i][j]:
                equal = False
                break
    return (equal)