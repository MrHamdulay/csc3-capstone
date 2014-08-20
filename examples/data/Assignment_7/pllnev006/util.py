#Module containing grid fuctions for the 2048 game
#Nevarr Pillay - PLLNEV006
#1 May 2014

def create_grid(grid): 
    """Creates a 4x4 grid"""
    for i in range(4):
        grid.append([])
        for j in range(4):
            grid[i].append(0)
        
def print_grid(grid): 
    """Prints the grid out in a box with columns of width 5"""
    print ("+","+",sep="-"*len(grid)*5)
    # Format for each column
    column = "{0:<5}"
    for i in range(len(grid)):
        print("|",end="")
        for j in range(len(grid[i])):
            #If the value in the block is not zero, the value is printed out using the column format
            if grid[i][j] > 0:
                print(column.format(grid[i][j]),end="")
            #Otherwise 5 spaces are printed out    
            else:
                print(" "*5,end="")
        print("|")
    print ("+","+",sep="-"*len(grid)*5)     
            

def check_lost(grid): 
    """If all the blocks are filled with numbers greater than 0 and no adjacent numbers are equal, this returns True, otherwise False"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return False
            else:
                up = i-1
                down = i+1
                left = j-1
                right = j+1
                if up >= 0:
                    if grid[i][j] == grid[up][j]:
                        return False
                if down < len(grid):
                    if grid[i][j] == grid[down][j]:
                        return False
                if left >= 0:
                    if grid[i][j] == grid[i][left]:
                        return False
                if right < len(grid[i]):
                    if grid[i][j] == grid[i][right]:
                        return False
    return True               

def check_won(grid): 
    """Checks to see if a number >= 32 appears in the grid"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 32:
                return True
    return False

def copy_grid(grid): 
    """Returns a copy of a grid"""
    newgrid = []
    for i in range(len(grid)):
        newgrid.append([])
        for j in range(len(grid[i])):
            newgrid[i].append(grid[i][j])        
    return newgrid
                
def grid_equal(grid1,grid2): 
    """Checks to see if two grids are equal"""
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True       
    

    