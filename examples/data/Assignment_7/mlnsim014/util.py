'''program containing utility functions to manipulate 2-d arrays
Simangaliso Mlangeni
MLNSIM014
02 May 2014'''


grid = [] 

#Function to create grid
def create_grid(grid):
    for i in range (4):
        grid.append([" "]*4)#creates and appends 4x4 array to grid
    for row in range(4):
        for col in range(4):
            if grid[row][col]==" ":
                grid[row][col]=0
    return grid

#assigns grid as global variable

grid = create_grid(grid)

#Function to print out grid
def print_grid(grid):
    #outer column surrounding grid
    print("+--------------------+")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col]==0:
                grid[row][col]=" "#checks if item = 0, and if it is assigns index to an empty string
            
            #variable to create width columns of 5 
            space = ' '*(5 - (len(str(grid[row][col]))))
            print(grid[row][col],space,sep= "",end = "")#prints out 4x4 grid
        print("|",end = "")
        print()
    #outer column surrounding grid
    print("+--------------------+")
    
grid = (create_grid(grid))

#function to check whether grid inserted has won or not
def check_won(grid):
    maX = 0
    for i in grid:
        for j in i:
            if j > maX:
                maX = j#Iterates through loop assigning value that is the biggest to max
    if maX >= 32:
        #if max is greater than 32 returns boolean value
        return True
    else:
        return False
            
#creates a copy of the second grid
def copy_grid(grid):
    grid = grid
    grid2= []
    for i in grid:#iterates through origional grid
        grid2.append(i)#appends values to new grid
    return grid2
#assign old variable grid to to new variable grid1
grid1 = grid

#Function to check if two grids are equal or not
def grid_equal(grid1,grid2):
    r=0
    for row in range(4):
        for col in range(4):
            if grid2[row][col] is grid1[row][col]:#checks if grid1 = grid2 and if it return boolean value
                
                r+=1
            else:
                return False
        if r==16:
            return True
            
#function to check whether grid assigned qualifies to have lost or not 
def check_lost(grid):
    #iterates through grid
    z=0
    for row in range(4):
        for col in range(3):
            if grid[row][col]== 0:#if grid has an item equal to zero returns boolean value
                z+=1#if this variable accumulates it means there is a value equal to zero in the grid
        if z>0:
            return False
    #iterates through eveery item in the list
    v=0
    p=0
    for row in range(3):
        for col in range(4):
            #check if item has any values equal to it that are adjacent and returns a boolean value if there are
            if grid[row][col]==0:
                continue
            elif grid[row][col]== grid[row][col+1] or grid[row][col]== grid[row][col-1]:
                v+=1
            elif grid[row][col]== grid[row+1][col] or grid[row][col] == grid[row-1][col]:
                p+=1
            
        if v>0 or p>0:
            return true
        else:
            return false