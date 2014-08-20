# Module of functions used to manipulate 2D arrays
# Conor O'Sullivan
# 4/27/2014




#create a 4x4 grid
def create_grid(grid):
    for x in range(4):
        grid.append([0]*4)
    return grid
        

#print out a 4x4 grid in 5-width columns within a box
def print_grid (grid):
    print("+--------------------+")
    for row in range(4):
        print("|",end = "")
        for col in range(4):
            if grid[row][col] == 0: 
                print("{:<5}".format(" "),  end = "")
            else: 
                print("{:<5}".format(grid[row][col]) ,  end = "")
        print("|")
    print("+--------------------+")

    
#return True if there are no 0 values and no adjacent values that are equal; otherwise False
def check_lost (grid):

    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0 or grid[row+1][col] == 0 or grid[row][col+1]==0: 
                return False
            elif grid[row][col] == grid[row][col+1]:
                return False
            elif grid[row][col] == grid[row+1][col]:
                return False
     
    return True
        # check right       
 
    return check
#return True if a value>=32 is found in the grid; otherwise Fals
def check_won (grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:
                return True
    return False
    
#return a copy of the grid
def copy_grid (grid):
    grid_copy = []
    for x in range(len(grid)):
        grid_copy.append(grid[x][:])
    return grid_copy
    
#check if 2 grids are equal - return boolean value
def grid_equal (grid1, grid2):
    if grid1 == grid2:
        return True
    return False


#Insure all functions are not run when program is imported    
if __name__ == '__main__': 
    create_grid(grid)
    print_grid(grid)
    check_lost(grid)
    check_won(grid)
    copy_grid(grid)
    grid_equal(grid1,grid2)