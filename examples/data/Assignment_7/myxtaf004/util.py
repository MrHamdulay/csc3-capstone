"""utility functions to manipulate 2-dimensional arrays of size 4x4
Tafadzwa Moyo
27 April 2014"""
#creates a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])
    return grid
#print out a 4x4 grid in 5-width columns within a box
def print_grid (grid):
    print("+--------------------+")
    for v in range(4):
        print("|", end='')
        for i in range(4):
            gap=5-len(str(grid[v][i]))
            value=" "
            if grid[v][i]:
                value=grid[v][i]
            print(value, " "*gap,sep='', end='')
        print("|")
    print("+--------------------+")
#return True if there are no 0 values and no adjacent values that are equal; otherwise False 
def check_lost (grid):
    for v in range(4):
        for i in range(4):   
            if v==0 or v==3:
                if grid[v][1]==grid[v][0] or grid[v][1]==grid[v][2] or grid[v][2]==grid[v][3]:
                    return False	                
            elif  i==0 or i==3:
                if grid[1][i]==grid[0][i] or grid[1][i]==grid[2][i] or grid[2][i]==grid[3][i]:
                    return False
                
            elif grid[v][i]!=0 and (grid[v][i]!=grid[v+1][i] or grid[v][i]!=grid[v-1][i] or grid[v][i]!=grid[v][i-1] or grid[v][i]!=grid[v][i+1]):
                return True
    return False
#return True if a value>=32 is found in the grid; otherwise False
def check_won (grid):
    for v in range(4):
        for i in range(4):  
            if grid[v][i]>=32:
                return True
    return False

#return a copy of the grid
def copy_grid (grid):
    grid1=[]
    create_grid(grid1)
    for v in range(4):
        for i in range(4):    
            grid1[v][i]=grid[v][i]
    return grid1
#return true if grids are equal, else it return false
def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    return False
"""create_grid(grid)
print_grid(grid)
print(check_lost(grid))
grid[2][1]=32
print(check_won(grid))
grid1=copy_grid(grid)
print(grid==grid1)"""