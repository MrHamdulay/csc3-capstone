#grid=[]
#Create 4x4 grid
def create_grid (grid):
    for i in range(4):
        lis=[]
        for j in range(4):
            lis.append(0)
        grid.append(lis)
    return grid
    

#print grid in a box with five spaces at each position
def print_grid (grid):

    print('+','-'*20,'+',sep='')
    
    for k in range(4):
        print('|',end='')
        for l in range(4):
            if grid[k][l]==0:
                grid[k][l]=" "
            print(grid[k][l],sep='',end=' '*(5-len(str(grid[k][l]))))

        print('|')
    print('+','-'*20,'+',sep='')
    
#Check if any zeros or equal adjacents 
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

#Check if reached 32
def check_won (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==' ':
                grid[i][j]=0
            if (grid[i][j])>=32:
                return True
            
    return False

#Create a copy of the grid
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

#Check if two grids are equal
def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False
    

#grid= create_grid(grid)
#print_grid(grid)
#grid1 = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
#grid2 = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
#cop=copy_grid(grid) 
#print(cop)