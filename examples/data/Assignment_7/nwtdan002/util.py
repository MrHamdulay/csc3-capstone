'''Program to manipulate and examine 4x4 grids
By Daniel Newton
27/04/14'''

def create_grid(grid):      #creates a 4x4 array with 0 as every element.
    '''Create a 4x4 grid'''
    for i in range (4):
        grid.append ([0] * 4)          
    
def print_grid(grid):
    '''Prints out a 4x4 grid in 5-width columns within a box'''
    print("+--------------------+")     #prints top line
    for i in range(4):      #prints each row
        print("|",end='')
        for j in grid[i]:
            if j==0:
                print("     ",end='')   #replaces elements equal to 0 with blank spots
            else:
                print(j," "*(5-len(str(j))),sep='',end='')  #places other numbers in a 5 width area
        print("|")
    print("+--------------------+") #prints bottom line
        

def check_lost(grid):
    '''Return True if there are no 0 values and no adjacent values that are equal; otherwise False'''
    start=1
    for i in grid:
        for j in i:
            if j==0:    #checks for values of 0
                return False

        for a in range(3):
            if i[a]==i[a+1]:    #checks  for horizontally adjacent matching pairs
                return False
        if start<3:
            for b in range(4):  #checks for vertically adjacent matching pairs
                if i[b]==grid[start][b]:
                    return False
        start+=1
    return True

def check_won(grid):
    '''Return True if a value>=32 is found in the grid; otherwise False'''
    for i in grid:
        for j in i:
            if j>=32:   #checks if there is a value in whole grid >= 32
                return True
    return False

def copy_grid(grid):
    '''Return a copy of the grid'''
    copygrid=[]     #creates new grid
    create_grid(copygrid)
    for i in range(4):
        for j in range(4):
            copygrid[i][j]=grid[i][j]   #sets each element of grid given to a corresponding element in the new grid.
    return copygrid

def grid_equal(grid1,grid2):
    '''check is 2 grids are equal - return boolean value'''
    if grid1==grid2:    #checks if equal
        return True
    return False