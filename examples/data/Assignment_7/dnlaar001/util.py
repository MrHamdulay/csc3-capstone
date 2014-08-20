def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])      
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')
    for o in range(len(grid)):
        print('|',end='')
        for e in range(len(grid[o])):
            j=grid[o][e]
            if j==0:
                g=' '
            else:
                g=j
            print(g,end=' '*(5-len(str(grid[o][e]))))
        print('|')
    print('+--------------------+')          

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    t=0
    for o in range(len(grid)):
        for e in range(len(grid[o])):
            if grid[o][e]==0:
                t+=1
            else:
                ()
    r=0
    for o in range(len(grid)):
        for e in range(len(grid[o])-1):
            if grid[o][e]==grid[o][e+1]:
                r+=1
            elif grid[o][3]==grid[o][2]:
                r+=1    
            else:
                ()
                
    v=0
    for o in range(len(grid)):
        for e in range(len(grid[o])-1):
            if grid[e][o]==grid[e+1][o]:
                v+=1
            elif grid[3][o]==grid[2][o]:
                v+=1    
            else:
                ()    
                
    if t==0 and r==0 and v==0:
        return True
    else:
        return False   

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    p=0
    for k in range(len(grid)):
        for g in range(len(grid[k])):  
            if grid[k][g]>=32:
                p+=1
            else:
                ()
    if p>0:
        return True
    else:
        return False
               

def copy_grid (grid):
    """return a copy of the grid"""
    c=[]
    for i in range(len(grid)):
        c.append(grid[i])
    return eval(str(c))
   
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    s=0    
    for h in range(4):
        for m in range(4):
            if grid1[h][m]==grid2[h][m]:
                s+=1
            else:
                ()
    if s==16:
        return True
    else:
        return False
    
