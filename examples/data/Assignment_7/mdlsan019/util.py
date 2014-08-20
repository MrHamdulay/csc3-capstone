'''Sanele Mdlalose
   MDLSAN019
   01-05-2014
   Grids'''

def create_grid (grid):
    #creates a 4x4 grid    
    for i in range(4):
        grid.append([0]*4)
        
def print_grid (grid):
    #prints a 4x4 grid with column width-5
    print("+--------------------+")
    for row in range(4):
        print('|',end='')
        for col in range(4):
            height=len(str(grid[row][col]))
            width=5
            if grid[row][col]!=0:
                print(grid[row][col],' '*(width-height),sep='',end='')
            else:
                
                empty_zero=' '
                print(empty_zero*(width),end='')
                
        print('|')
    print("+--------------------+")        
            
       
    
def check_lost (grid):
    #checks if there is a zero and adjacent-equal numbers in a grid  
    for row in range (4):
        for col in range (4):
            check = False
            zero = False
            if grid[row][col] == 0:
                zero = True
                for i in range (4):
                    for j in range (1,3):
                        if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i][j+1]:
                            check = True
                        
                for a in range (1,3):
                    for b in range (4):
                        if grid[a][b] == grid[a-1][b] or grid[a][b] == grid[a+1][b]:
                            check = True
            elif grid[row][col] != 0:
                for i in range (4):
                    for j in range (1,3):
                        if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i][j+1]:
                            check = True
                                       
                for a in range (1,3):
                    for b in range (4):
                        if grid[a][b] == grid[a-1][b] or grid[a][b] == grid[a+1][b]:
                            check = True
                
            else:
                check = False
                zero = False
    if check == False and zero == False:
        return True
    else:
        return False
        
def check_won (grid):
    #checks if there is any value>=32
    num=False
    for row in range (4):
        for col in range (4):
            #value=grid[row][col]
            if grid[row][col]>=32:
                num=True
    if num==True:
        return True
    else:
        return False
    
def copy_grid (grid):
    #copies an input grid to a new grid
    new_grid=[]
    
    for i in range(4):
        new_grid.append([0]*4)
        
    for row in range(4):
        for col in range(4):  
            new_grid[row][col]=grid[row][col]
    return new_grid

def grid_equal (grid1, grid2):
    #checks for equality of two input grids
    if grid1==grid2:
        return True
    else:
        return False