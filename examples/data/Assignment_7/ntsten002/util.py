#util
#Tendani Netshitenzhe
#02May014

#Create Grid function creating a 4x4 grid
def create_grid(grid):
    if grid:
        for row in range(4):
            for col in range(4):
                if grid[row][col] == 0:
                    grid[row][col] = " "
    else:
        for i in range(4):
            grid.append([0]*4)

#Print the grid with borders       
def print_grid(grid):
    print("+"+"-"*20+"+")
    for row in range(4):
        print("|", end="")
        for col in range(4):
            if grid[row][col] == 0:
                grid[row][col] = " "            
            if col == 3:
                print("{0:<5}".format(grid[row][col]),"|", sep="")
            else:
                print("{0:<5}".format(grid[row][col]), end="")
    print("+"+"-"*20+"+")

#Check if the game is lost
def check_lost(grid):
    lost = True
    lost_a = True
    
    for row in range(4):
        for col in range(4):            
            if (grid[row][col] == 0):
                lost = False
                break
    for row in range(3):
        for col in range(3):
            if (grid[row][col] == grid[row+1][col]):
                lost_a = False
            if (grid[row][col] == grid[row][col+1]):
                lost_a = False
                break
                
    if (lost_a == True and lost == True):
        return True
    else:
        return False

#Check if game is won
def check_won(grid):
    won = False
    for row in range(4):
        for col in range(4):
            if type(grid[row][col]) != str:
                if grid[row][col] >= 32:
                    won = True
    return won    

#Copy grid and return new grid
def copy_grid(grid):
    new_grid=[]
    for i in range(4):
        new_grid.append([" "]*4)    
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                grid[row][col] = " "            
            new_grid[row][col] = grid[row][col]
    return new_grid

#Determine if two grids are equal
def grid_equal(grid1, grid2):
    found = True
    for row in range(4):
        for col in range(4):
            if grid1[row][col] != grid2[row][col]:
                found = False
    return found
                    
                    