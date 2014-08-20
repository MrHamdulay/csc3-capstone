def create_grid(grid):
   
    for i in range (4):
        grid.append([0]*4)
    
def print_grid(grid):
    
    print('+'+'-'*(20)+'+',end='')
    print()
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j]==0:
                print('{:<5}'.format(' '),end='')
            else:
                print('{:<5}'.format(grid[i][j]),end='')
        print('|',end='')
        print()
    print('+'+'-'*(20)+'+',end='')                 
             
def check_lost(grid):

    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return False
         
    for i in range(4):
        for j in range(4):
            ref=grid[i][j]
            if 0<=j+1<4:
                if ref==grid[i][j+1]:
                    return False
            if 0<=j-1<4:
                if ref==grid[i][j-1]:
                    return False
            if 0<=i+1<4:
                if ref==grid[i+1][j]:
                    return False
            if 0<=i-1<4:
                if ref==grid[i-1][j]:
                    return False
    return True
    
     
def check_won(grid): 
  
    for i in range(4): 
        for j in range(4):
            if grid[i][j]>=32 or grid[j][i]>=32:
                return True
    return False
    
def copy_grid(grid): 
    
    copy=[]
    create_grid(copy)
    for i in range(4):
        for j in range(4):
            copy[i][j]=grid[i][j]
    return copy
    
def grid_equal(grid1,grid2): 
   
    if grid1==grid2:
        return True
    return False 










