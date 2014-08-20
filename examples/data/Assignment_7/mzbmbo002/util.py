#Mbongeni Mazibuko
#MZBMBO002
#Assignment 7

def create_grid(grid):
    """creates a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)  

def print_grid (grid):
    """prints out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')
    for row in range(4):
        print('|',end='')
        for col in range(4):
            if grid[row][col]!=0:
                print(grid[row][col],' '*(5-len(str(grid[row][col]))),sep='', end='')
            else: print(' '*5, end='')
        print('|')
    print('+--------------------+')
            
def check_lost (grid):
    """returns True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    adj=False
    zero=False
    for row in range(1,3):
        for col in range(4):
            if grid[row][col]==grid[row-1][col]:
                adj= True
            elif grid[row][col]==grid[row+1][col]:
                adj= True
    for row in range(4):
        for col in range(1,3):
            if grid[row][col]==grid[row][col-1]:
                adj= True
            elif grid[row][col]==grid[row][col+1]:
                adj= True
    for i in range(4): 
        if 0 in grid[i]:
            zero= True
        
    if zero==False and adj==False:
        return True
    else: return False

def check_won (grid):
    """returns True if a value>=32 is found in the grid; otherwise False"""
    won=0
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                won=1
    if won==1:
        return True
    else: return False

def copy_grid (grid):
    """returns a copy of the grid"""
    copy_grid=[]
    for i in range(4):
        copy_grid.append(['']*4) 
    for i in range(4):
        for j in range(4):
            copy_grid[i][j]=grid[i][j]
    return copy_grid

def grid_equal (grid1, grid2):
    """checks if 2 grids are equal - return boolean value"""
    equal=''
    for i in range(4):
        for j in range(4):
            if  equal!='no':
                if grid1[i][j]!=grid2[i][j]:
                    equal='no'
                    return False
    if equal=='':
        return True