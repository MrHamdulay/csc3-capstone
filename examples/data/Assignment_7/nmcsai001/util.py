"""Saijil Nemchund
NMCSAI001
Program that manipulates 4x4 2D arrays"""

def create_grid(grid):   #creating a 4x4 grid 
    for i in range(4):   #adding zeros to the grid 
        grid.append([0,0,0,0])

        
def print_grid(grid): #print out a 4x4 grid in 5-width columns within a box
    grid1=list(grid)
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                grid1[i][j]=""    
                

    print("+",20*"-","+",sep="")
    
    for n in range(4): 
        print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(grid1[n][0],grid1[n][1],grid1[n][2],grid1[n][3]),"|",sep="")

    print("+",20*"-","+",sep="")
    
def check_lost(grid): #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    a=True
    b=True
    c=True
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                a=False
    
    for k in range(4):
        for l in range(3):
            if grid[k][l]==grid[k][l+1]:
                b=False
                
    for g in range(3):
        for y in range(4):
            if grid[g][y]==grid[g+1][y]:
                c=False
    if a and b and c:
        return True
    else:
        return False
    
def check_won(grid): #return True if a value>=32 is found in the grid; otherwise False
    a=False
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                a=True
    return a

def copy_grid(grid): #return a copy of the grid
    Ngrid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            Ngrid[i][j]=grid[i][j]
    
    
    
    return Ngrid

def grid_equal(grid1,grid2): #check if 2 grids are equal - return boolean value
    if grid1==grid2:
        return True
    else:
        return False