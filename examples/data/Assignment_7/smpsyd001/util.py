#utility functions
#29/04/2014
#Sydney Simpson

def create_grid(grid):
    '''create a 4x4 grid'''
    for i in range(4):
        grid.append(["0"]*4)
    return grid


def print_grid (grid):
    '''print out a 4x4 grid in 5-width columns within a box'''
    print("+--------------------+")
    for row in range (4):
        print("|", end='')
        for column in range(4):
            #print(row, column)
            s='{0:<5}'
            if grid[row][column]==0:
                print(s.format(" "),end="")
            else:
                print(s.format(grid[row][column]), end="")
        print("|")
    print("+--------------------+")
    
    
def check_lost(grid):
    '''return True if there are no 0 values and no adjacent values that are equal; otherwise False'''
    for item in range (4):
        for i in range (4):
            if grid[item][i]==0:
                return False
            if i>0 and i!=3:
                if grid[item][i]==grid[item][i+1] or grid[item][i]==grid[item][i-1]:
                    return False
            if i==0:
                if grid[item][i]==grid[item][i+1]:
                    return False
                
            if item ==0:
                if grid[item][i]==grid[item+1][i]:
                    return False
                
            if item > 0 and item !=3:
                if grid[item][i]==grid[item-1][i] or grid[item][i]==grid[item+1][i]:
                    return False
    return True
    
    
def check_won(grid):
    '''return True if a value >=32 is found in the grid; otherwise False'''
    for i in range (4):
        for j in range (4):
            if grid[i][j]>=32:
                return True
    return False

def copy_grid(grid):
    '''return a copy of the grid'''
    new_grid=[]
    create_grid(new_grid)
    for i in range(4):
        for j in range (4):
            a=grid[i][j]
            new_grid[i][j]=a
    return new_grid
    
def grid_equal (grid1,grid2):
    '''check is 2 grids are equal - return boolean value'''
    for i in range (4):
        for j in range (4):
            if grid1[i][j]!=grid2[i][j]:
                return False
    return True