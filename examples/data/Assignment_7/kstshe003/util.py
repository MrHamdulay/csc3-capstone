#sheldon kisten
#grids
#2 may 2014

grid=[]
copyofgrid=[]

def create_grid (grid):
    for i in range(4):
        grid.append([0] * 4) 
    
def print_grid (grid):
    print ("+", "-"*20, "+", sep="")
    for x in range (4): #x for rows
        print ("|",end="")
        for y in range (4): #y for columns
            if grid[x][y]==0:
                grid[x][y]=" "
            print ("{0:<5}".format(grid[x][y]),end="")
        print ("|",end="")
        print()
    print ("+", "-"*20, "+", sep="")
    
def check_lost (grid):
    for x in range (4):
        for y in range (3):            
            if grid[x][y]==" ": #0 check
                return False
            elif grid[x][y]==grid[x][y+1]: #adjacent value check
                return False
    for x in range (3):
        for y in range (4):
            if grid[x][y]==" ": #0 check
                return False
            elif grid[x+1][y]==grid[x][y]: #adjacent value check
                return False
            
    return True    

def check_won (grid):
    for x in range (4):
        for y in range (4):
            if grid[x][y]==" ":
                grid[x][y]=0
            if grid[x][y]==32 or grid[x][y]>=32:
                return True
    
    return False    
        
def copy_grid (grid):
    for i in range (4):
        copyofgrid.append([" "]*4)
    for x in range (4):
        for y in range (4):
            copyofgrid [x][y]=grid [x][y]
    
    return copyofgrid

def grid_equal (grid1, grid2):
    for x in range (4):
        for y in range (4):
            if grid1[x][y] is not grid2[x][y]:
                return False
    
    return True