def create_grid(grid):
    #v for vertical
    #h for horizontal
    for v in range (4):
            grid.append([0]*4)
            
def print_grid(grid):
    print ("+--------------------+") #prints the top section of the grid 
    for v in range (4):
        print("|",end="")
        for h in range (4):
            #this creates a border on the left hand side of the grid
            if grid[v][h] == 0:
                grid[v][h] = " "
            print ("{0:<5}".format(grid[v][h]),end="",sep=""), #prints the five space format values
            if h ==3:
                print("|",end="")# \this creates the border on the right hand side of the grid
        print()
    print ("+--------------------+")#prints the bottom section of the grid

def check_lost(grid):
    c=0
    #this part checkks for zeros
    for v in range (4):
        for h in range (4):
            if grid[v][h] == 0:
                c=c+1
    for v in range (1,2):#check values not 100% sure
        for h in range (1,2):
            #next line checks top and to the side of the box for identical values 
            if grid[v][h] == grid[v+1][h] or grid[v][h]==grid[v][h+1]:
                c=c+1
    if c == 0:
        return True
    elif c!=0:
        return False

def check_won(grid):
    c=0
    #counter ensures that one boolean value is returned at the end of the functions 
    for v in range (4):
        for h in range (4):
            if grid[v][h]>=32:
                c=c+1
    if c>0:
        return True
    else:
        return False

def copy_grid(grid):
    # first necessary to create a new grid 
    duplicate=[]
    for new in range(4):
        duplicate.append([" "]*4)
    for v in range (4):
        for h in range (4):
            duplicate[v][h] = grid[v][h]
    return duplicate

def grid_equal(grid1,grid2):
    #scans through the grids to be compared and returns
    c=0 #counter ensures that the function returns only 1 boolean value
    for v in range (4):
        for h in range(4):
            if grid1[v][h] != grid2[v][h]:
                return False
            else:
                c=c+1
    #4x4 grid hence must check across 16 values 
    if c==16:
        return True
    else:
        return False