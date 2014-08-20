
#Assignment 7
#Question 2

def create_grid (grid):
    for i in range(4):
        lis=[]
        for j in range(4):
            lis.append(0)
        grid.append(lis)
    return grid
    


def print_grid (grid):

    print("+--------------------+")
    
    for k in range(4):
        print('|',end='')
        for l in range(4):
            if grid[k][l]==0:
                grid[k][l]=" "
            print(grid[k][l],sep='',end=' '*(5-len(str(grid[k][l]))))

        print('|')
    print("+--------------------+")
    

def check_lost (grid):
    
    for i in range(4):
        for j in range(3):
            if grid[i][j]==' ':
                grid[i][j]=0             
            if grid[i][j]==0:
                return False
            elif grid[i][j]==grid[i][j+1]:
                return False
            
    for i in range(3):
        for j in range(4):
            if grid[i][j]==' ':
                grid[i][j]=0            
             
            if grid[i][j]==0:
                return False
            elif grid[i+1][j]==grid[i][j]:
                return False
            
    return True


def check_won (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==' ':
                grid[i][j]=0
            if (grid[i][j])>=32:
                return True
            
    return False


def copy_grid (grid):
    copy= []
    for i in range(4):
        lis=[]
        for j in range(4):
            lis.append(" ")
        copy.append(lis)
    for i in range(4):
        for j in range(4):
            copy[i][j]=grid[i][j]
        
    return copy


def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False
    

