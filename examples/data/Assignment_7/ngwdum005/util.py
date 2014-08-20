'''Dumisani Ngwenza
NGWDUM005
29/04/2014
Asssignment 7 Question 2'''

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid
    
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    column = '{0:<5}'
    print ('+', '-'*20, '+', sep ='')
    for i in range (4): #row
        print ('|', end='')
        for j in range(4): #column
            if grid[i][j] == 0:
                print (column.format(' '), sep='', end='')
            else:
                print (column.format(grid[i][j]), sep='', end='')
        print('|')
    print ('+', '-'*20, '+', sep ='')


def check_lost (grid):
    """return True if there are no more 0 values and no adjacent values that are equal otherwise False"""
    for i in range (4):
        for j in range(4):
            if grid[i][j] == 0 and (grid[i-1][j] != grid[i][j] or grid[i+1][j] != grid[i][j] or grid[i][j-1] != grid[i][j] or grid[i][j+1] !=grid[i][j]):
                return True
            else:
                return False
            

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range (4):
        for j in range (4):
            if grid[i][j] < 32:
                continue
            else:
                return True
    else:
        return False


def copy_grid (grid):
    """return a copy of the grid"""
    grid2 = []
    for i in range (4):
        grid2.append([0]*4)
    
    for i in range (4):
        for j in range (4):
            grid2[i][j] = grid[i][j]
    return grid2


def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean values"""
    for i in range (4):
        for j in range (4):
            if grid1 == grid2:
                return True
            else:
                return False
    

if __name__=='__main__':
    l = []
    create_grid(l)
    print_grid(l)
    print(check_lost(l))
    print (copy_grid(l))