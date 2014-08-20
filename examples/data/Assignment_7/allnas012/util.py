#Nasiha Ally
#ALLNAS012  
#02 May 2014



def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
        
def print_grid(grid):
    import copy
    x=copy.deepcopy(grid)
    for row in range(4):
        for column in range(4):
            if x[row][column]==0:
                x[row][column]=" "
    print("+","-"*20,"+",sep="")

    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(x[0][0],x[0][1],x[0][2],x[0][3]),"|",sep="")
    
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(x[1][0],x[1][1],x[1][2],x[1][3]),"|",sep="")
    
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(x[2][0],x[2][1],x[2][2],x[2][3]),"|",sep="")
    
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(x[3][0],x[3][1],x[3][2],x[3][3]),"|",sep="")
    print("+","-"*20,"+",sep="")
        
        

def check_lost(grid):
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0:
                return False
    if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
        return False
    if grid[0][3]==grid[0][2] or grid[0][3]==grid[1][3]:
        return False
    if grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
        return False
    if grid[3][3]==grid[2][3] or grid[3][3]==grid[3][2]:
        return False
    if grid[0][1]==grid[0][2] or grid[0][1]==grid[1][1]:
        return False
    if grid[0][2]==grid[1][2]:
        return False
    if grid[1][1]==grid[2][1] or grid[1][1]==grid[1][2] or grid[1][1]==grid[1][0]:
        return False
    if grid[2][1]==grid[2][0] or grid[2][1]==grid[2][2] or grid[2][1]==grid[3][1]:
        return False
    if grid[1][0]==grid[2][0]:
        return False
    if grid[1][2]==grid[1][3] or grid[1][2]==grid[2][2]:
        return False
    if grid[2][2]==grid[2][3] or grid[2][2]==grid[3][2]:
        return False
    if grid[3][1]==grid[3][2]:
        return False
    else:
        return True 
    
    
def check_won(grid):
    y=False
    for row in range(4):
        for column in range(4):
            if grid[row][column]>=32:
                y=True
                break
    return y

def copy_grid(grid):
    import copy
    x=copy.deepcopy(grid)
    return x

def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True
    else:
        return False