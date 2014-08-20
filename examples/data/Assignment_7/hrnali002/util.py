"""A program that has utility functions to manipulate 2D arrays of size 4 x 4
Alison Hoernle
HRNALI002
27 April 2014"""

# create a grid (not sure what to do with it)
def create_grid(grid):
    
    #create a 2D array (list of lists)
    for i in range(4):
        grid.append([0] * 4)
    
    #retun 2D array
    grid_new = []
    for row in range(4):
        for columb in range (4):
            grid_new.append(grid[row][columb])
    
    return grid_new

# Want to make a grid with columbs of width 5. the whole grid within a box    
def print_grid(grid):
    
    # top line of box
    print("+--------------------+")
    
    # rest of the box
    i = 0
    n = 0
    
    while i < len(grid): 
        for num_row in grid:
            print('|', end = '') # beginning of each line in the box
            for num_col in grid[i]:
                
                # if number is a 0, just print 5 spaces
                if num_col == 0:
                    print(' '*5, end = '')
                
                # if not a 0, then print that number formatted to a width of 5 (filled with spaces)
                else:
                    print("{0:<5}".format(num_col), end = '')
        
            print('|') # end of each line in the box 
            i += 1
    # bottom line of the box
    print("+--------------------+")
    
def check_lost(grid):
    row_num = 0
    for i in grid:
        col_num = 0
        
        for value in i:
            # if any 0 values then false
            if value == 0:
                return False
            
            # checking for an adjacent value in the horizontal on the right
            if col_num < len(i)-1:
                if value == grid[row_num][col_num+1]:
                    return False
                
            # checking for an adjacent value in the horizontal on the left
            elif col_num > 0:
                if value == grid[row_num][col_num-1]:
                    return False
                
            # checking for an adjacent value below
            if row_num < len(grid)-1:
                if value == grid[row_num+1][col_num]:
                    return False
                
            # checking for an adjacent value above
            elif row_num > 0:
                if value == grid[row_num-1][col_num]:
                    return False
            col_num += 1
        row_num += 1
    
    return True

def check_won(grid):
    for i in grid:
        for value in i:
            if value >= 32:
                return True
    
    return False
            
              
def copy_grid (grid):
    
    grid_new = []
    for item in grid:
            grid_new.append(list(item))
    
    return grid_new

def grid_equal(grid1, grid2):
    # defining the row variable to be used later
    row = 0
    
    # iterate through the first list and each value in the list and check if the corresponding value in the second list is the same. If not then return false straight away
    for item1 in grid1:
        column = 0
        for value in item1:
            if grid2[row][column] != value:
                return False
            else:
                column += 1
        row += 1
    
    return True