"""the utility function
Aphiwe Baleni
29 April 2014"""
grid=[]
def create_grid(grid):
    height = 4
    for i in range (height):
        grid.append ([0] * 4)
    return grid
grid=create_grid(grid)

def print_grid(grid):
    print('+','-'*20,'+',sep='')
    form='{0:<5}'
    for row in range (4):
        print('|',end='')
        for col in range (4):
            if (grid[row][col])==0:
                grid[row][col]=' '            
                print (form.format(grid[row][col]),end="")
            else:
                print (form.format(grid[row][col]),end="")
        print('|',end='')
        print ()    
    print('+','-'*20,'+',sep='')
    grid=create_grid(grid)

def check_lost(grid) :
    for row in range(4):
        #if 0 in row:
            #return False
        for col in range(4):
            if row> 0:
                if grid[row-1][col]==grid[row][col]:
                    return False
            elif col>0:
                if grid[row][col]==grid[row][col-1]:
                    return False
    else:
        return True

def check_won(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                return True
    else:
        return False
def copy_grid(grid):
    import copy
    copy_grid=copy.deepcopy(grid)
    return copy_grid
#test=0
def grid_equal(grid1,grid2):
    test=0
    for row in range(4):
        for col in range(4):
            if grid1[row][col]==grid2[row][col]:
                test+=1
    if test==16:
        return True
    else:
        return False
              