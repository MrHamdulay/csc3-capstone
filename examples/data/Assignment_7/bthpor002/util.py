#A program that creates the grid 



#Create the 4x4 grid
def create_grid (grid):
    height=4
    for i in range(height):
        list1=[]
        for j in range(height):
            list1.append(0)
        grid.append(list1)
    return grid
    

#Print the grid that is left aligned with 5 spaces
def print_grid (grid):

    print('+','-'*20,'+',sep='')
    
    for i in range(4):
        print('|',end='')
        for l in range(4):
            if grid[i][l]==0:
                grid[i][l]=" "
            print(grid[i][l],sep='',end=' '*(5-len(str(grid[i][l]))))

        print('|')
    print('+','-'*20,'+',sep='')
    
#Check if there are any zero's or adjacent equal numbers  
def check_lost (grid):
    
    for k in range(4):
        for j in range(3):
            if grid[k][j]==' ':
                grid[k][j]=0             
            if grid[k][j]==0:
                return False
            elif grid[k][j]==grid[k][j+1]:
                return False
            
    for k in range(3):
        for j in range(4):
            if grid[k][j]==' ':
                grid[k][j]=0            
             
            if grid[k][j]==0:
                return False
            elif grid[k+1][j]==grid[k][j]:
                return False
            
    return True

#Check if the numbers have reached 32
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
        list1=[]
        for j in range(4):
            list1.append(" ")
        copy.append(list1)
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
    

