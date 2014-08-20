#a module of utility functions to manipulate 2-dimensional arrays of size 4x4
#Gordon Skhosana
#2/05/2014

height=4
width=5
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append(["0"]*4)
    
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*height*width,"+",sep="")     
    for row in range(height):
        print("|",end="")
        for col in range(height):
            if grid[row][col]!=0:
                print("{0:<5}".format(grid[row][col]),end="")
            else: 
                print("{0:<5}".format(" "),end="")
        print("|",end="")
        print()
    print("+","-"*height*width,"+",sep="")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    zero=True
    for row in range(height):
        for col in range(height):
            if grid[row][col]==0:
                zero=False
    #checking for vertical matches
    no_vertical_match=True
    for row in range(height):
        for col in range(height):
            if row==0:
                if grid[row][col]==grid[row+1][col]:
                    no_vertical_match=False
            elif 0<row<height-1:
                if grid[row][col]==grid[row+1][col]:
                    no_vertical_match=False                    
    #checking for horizontal matches
    no_horizontal_match=True
    for col in range(height):
        for row in range(height):
            if col==0:
                if grid[row][col]==grid[row][col+1]:
                    no_horizontal_match=False
            elif 0<col<height-1:
                if grid[row][col]==grid[row][col+1]:
                    no_horizontal_match=False
    if not zero:
        return False
    elif no_vertical_match and no_horizontal_match:
        return True
    else: 
        return False
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won=False
    for row in range(height):
            for col in range(height):
                if grid[row][col]>=32:
                    won=True
    return won
def copy_grid (grid):
    """return a copy of the grid"""
    grid_new=[]
    grid_temp=[]
    j=0
    for row in range(height):
        for col in range(height):
            grid_temp.append(grid[row][col])
    for i in range(height):
        grid_new.append(grid_temp[j:j+4])
        j+=4
    return grid_new
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal=True
    for row in range(height):
        for col in range(height):
            if grid1[row][col]!=grid2[row][col]:
                equal=False
    return equal