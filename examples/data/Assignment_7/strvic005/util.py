"""program containing utility functions to manipulate 2-D arrays of size 4x4
vicky stark
29 april 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    
    for i in range(4): #a 2-D array
        grid.append([0]*4)
    
    #to print the array (like in Hussein's example)
    new_grid=[]
    for row_number in range(4):
        for column_number in range(4):
            new_grid.append(grid[row_number][column_number])
    return  new_grid
                     
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    #print top line
    print("+--------------------+")
    
    j=0
    
    #to print the middle part of the box
    while j < len(grid):
        for row_number in grid:
            print('|', end='')
            for column_number in row_number:
                if column_number==0: # replace any 0 with empty strings
                    column_number=' '
                print("{0:<5}".format(column_number), end='') #use format with width of 5 for each
            print('|')
            j+=1
    
    #print bottom line
    print("+--------------------+")

            
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal;otherwise False"""
    row_number=0
    for row in grid: #for each row
        column_number=0
        
        for column in row: #for each column in each row
            
            if column_number == 0: #if the value equals zero then return false
                return False
            
            elif row_number< row_number[::-1]:
                if column_number==grid[row_number+1][column_number]: #if value is equal to the value below it 
                    return False
            
            elif row_number >0:
                if column_number==grid[row_number-1][column_number]: #if value is equal to the value above it
                    return False
                
            elif column_number< column_number[::-1]:
                if column_number==grid[row_number][column_number+1]: #if a value to the right is equal to value 
                    return False
            
            elif column_number > 0: 
                if column_number==grid[row_number][column_number-1]: #if a value to the left is equal to value
                    return False
            column+=1
            
    row+=1        
    return True


def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row_number in grid:
        for column_number in row_number:
            if column_number>=32:         #if value is 32 or greater they have won
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    
    #copy function- create a new 2d array- call it 'new-grid' - so you end up with something that has all zeros   
   
    new_grid=[]
    for item in grid:
        new_grid.append(list(item))
    return new_grid
            
def grid_equal (grid1, grid2):
    """check if 2 grids are equal- return bollean value"""
    #go through every correspondong element in the two grids, and if things don't match return false
    
    count=0
    for row_num in range(4):
        for  col_num in range(4):
            if grid1[row_num][col_num]!=grid2[row_num][col_num]:
                count+=1
    if count !=0: #if there is an error, 1 will be added to count and so if count has a value it means there is an error and so returns false
        return False
            
    else: 
        return True
            
            
    