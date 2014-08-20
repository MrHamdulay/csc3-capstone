#Program of utility functions to manipulate 2-dimensional arrays of size 4x4.
#BRXCAI001
#02 MAY 2014

#First utility function.
def create_grid(grid):
    """create a 4x4 grid"""
    
#Create a 2D array.  
    for i in range(4): 
        grid.append([0]*4)
    
    second_grid=[]
    for rownum in range(4):
        for colnum in range(4):
            second_grid.append(grid[rownum][colnum])
    return  second_grid

#Second utility function.
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
#Print first line of box.
    print("+--------------------+")
    
    var = 0
    
    while var < len(grid):
        for rownum in grid:
            print('|', end='')
            for colnum in rownum:
                #If colnum equals 0 it must be replaced with an empty string.
                if colnum == 0: 
                    colnum =' '
                #Format width 5.
                print("{0:<5}".format(colnum), end='')
            print('|')
            var= var + 1
    
#Print last line of box.
    print("+--------------------+")

            
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal;otherwise False"""
    rownum=0
    for row in grid: 
        colnum=0
        
        for column in row: 
            if colnum == 0: 
                return False
            
            elif rownum < rownum[::-1]:
                if colnum == grid[rownum + 1][colnum]: 
                    return False
            
            elif rownum > 0:
                if colnum ==grid[rownum-1][colnum]: #if value is equal to the value above it
                    return False
                
            elif colnum < colnum[::-1]:
                if colnum == grid[rownum][colnum+1]: 
                    return False
            
            elif colnum > 0: 
                if colnum == grid[rownum][colnum-1]:
                    return False
            colnum = 1 + colnum
            
    row = 1 + row       
    return True


def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for rownum in grid:
        for colnum in rownum:
            if colnum>=32: 
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid=[]
    for item in grid:
        new_grid.append(list(item))
    return new_grid
            
def grid_equal (grid1, grid2):
    """check if 2 grids are equal- return bollean value"""
   
    repeat=0
    for row_num in range(4):
        for  col_num in range(4):
            if grid1[row_num][col_num]!=grid2[row_num][col_num]:
                repeat = 1 + repeat
    if repeat !=0: 
        return False
            
    else: 
        return True