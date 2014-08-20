#omphemetse molusi
#mlsomp001
#02 april 2014

def create_grid(grid):#creating a square grid with side length of 4
    for i in range(4):
        grid.append([0]*4)
    return grid
    
    
def print_grid (grid):#printing a grid with in a column 
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


def check_lost (grid):#checking the list
    for i in range (4):
        for j in range(4):
            if grid[i][j] == 0 and (grid[i-1][j] != grid[i][j] or grid[i+1][j] != grid[i][j] or grid[i][j-1] != grid[i][j] or grid[i][j+1] !=grid[i][j]):
                return True
            else:
                return False
            

def check_won (grid):#what to return when the variable is greater then 32
    for i in range (4):
        for j in range (4):
            if grid[i][j] < 32:
                continue
            else:
                return True
    else:
        return False


def copy_grid (grid):#returning an exact duplicate of the grid
    grid2 = []
    for i in range (4):
        grid2.append([0]*4)
    
    for i in range (4):
        for j in range (4):
            grid2[i][j] = grid[i][j]
    return grid2


def grid_equal (grid1, grid2):#
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