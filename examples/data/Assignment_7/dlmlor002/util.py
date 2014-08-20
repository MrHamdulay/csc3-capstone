"""programs to manipulate 2D arrays of size 4x4
Lorena Dal Maso
27 April 2014"""
 
#create a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
        
#print out a 4x4 grid in 5-width columns within a box        
def print_grid(grid):
    print("+--------------------+")
    for row in range(4):
        print("|",end='')
        for column in range(4):
            if grid[row][column]== 0:
                print(" "*5,end="")
            else:
                print(grid[row][column]," "*(5-len(str(grid[row][column]))),sep="",end='')
        print("|")
    print("+--------------------+") 
        
def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False  
    for row in range(4):
        for column in range (4):
            if grid[row][column] == 0:
                return False
            
    for row in range(4):
        for column in range (4):
            if row==3 and column==3:
                1==1            
            else:
                if column==3:
                    if grid[row][column] == grid[row +1][column]:
                        return False
                elif row == 3:
                    if grid[row][column] == grid[row][column +1]:
                        return False
                elif grid[row][column] == grid[row][column +1] or grid[row][column] == grid[row +1][column] :
                    return False
    return True        

def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    for row in range (4):
        for column in range (4):
            if grid[row][column] >= 32:
                return True
    return False

def copy_grid (grid):
    #return a copy of the grid
    new_grid = []
    temp_array = []
    for row in range (4):
        temp_array = []
        for column in range (4):
            temp_array.append(grid[row][column])
        new_grid.append(temp_array)
    return new_grid

def grid_equal (grid1, grid2):
    #check if 2 grids are equal - return boolean value
    for row in range (4):
        for column in range (4):
            if grid2 == grid1:
                return True
    return False