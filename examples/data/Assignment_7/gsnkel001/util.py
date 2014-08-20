#grid functions
#1 may 2014
#kelly goosen

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4) #appending one row at a time
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+") #top of box
    for row in range(4):
        print("|",end="") #left side of box
        for column in range(4):
            if grid[row][column]==0:
                print(" "*5,end="") #prints spaces if item is 0
            else:
                print(grid[row][column],(5-len(str((grid[row][column]))))*" ",sep="",end="") #justify left
        print("|") #left side of box
    print("+--------------------+") #bottom of box    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range (4):
       for column in range (4):
           if grid[row][column] == 0:
               return False
           if row != 3: #ensures not out of range
               if grid[row][column]==grid[row+1][column]:
                   return False
           if column != 3: #ensures index not out of range
               if grid[row][column]==grid[row][column+1]:
                   return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for column in range(4):
            if grid[row][column]>=32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    copygrid=[] #initialize the variable
    for row in range(4):
        rowlist=[] #ensure variable is repeatedly initailised
        for column in range(4):
            rowlist.append(grid[row][column])
        copygrid.append(rowlist) #appends rows at a time
    return copygrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range(4):
        for column in range(4):
            if grid1[row][column]!= grid2[row][column]:
                return False
    return True