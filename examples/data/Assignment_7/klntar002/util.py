
def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
    return grid
        
        
def print_grid(grid):
    print('+--------------------+')
    for column in range(4):
        
        for row in range(-1, 5):                
            if row==-1 or row==4:
                print ('|',end="")
               # print('|'+"{0:5}".format(str(grid[column][row])),end='')
            #if row==3:
                #print("{0:5}".format(str(grid[column][row]))+"|",end='')
            else:
                if grid[column][row]==0:
                    grid[column][row]=' '
                print ("{0:5}".format(str(grid[column][row])),end='')
                
        print()
    print('+--------------------+')
    
    
def check_lost(grid):
    for column in range (4):
        for row in range (4):
            if grid[column][row]==0:
                return False
            elif row!=3 and grid[column][row]== grid[column][row+1]:
                return False
            elif column!=3 and grid[column][row]== grid[column+1][row]:
                return False
    return True        
                
        


def check_won(grid):
    nono=False
    for column in range(4):
        for row in range(4):
            if grid[column][row]>=32:
                nono=True
    return nono



def copy_grid(grid):
    an_grid=[]
    for i in range(4):
        an_grid.append([0]*4)
        
    for column in range(4):
        for row in range(4):
            an_grid[column][row]=grid[column][row]
    return an_grid

def grid_equal(grid1,grid2):
    for i in range(grid1):
        if all(grid1[i]==grid2[i]):
            return True
        else:
            return False
        
def grid_equal(grid1,grid2):
     """check if 2 grids are equal - return boolean value"""
     if grid1==grid2:
         return True
     else:
         return False
            
    
        
                
                
                