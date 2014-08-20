'''Question 2 Assignment 7
Utility functions which manipulate a 2 dimensional, 4*4 array
Adam Oosthuizen
27 April 2014'''

def create_grid(grid):
    '''creates a 4x4 grid'''
    grid=[]
    for i in range(4):
        grid.append(['']*4)
    return grid

def print_grid(grid):
    '''Print out a 4x4 grid in 5-width collumns within a box'''
    #+--------------------+
    #|2         2         |
    #|     4         8    |
    #|     16        128  |
    #|2    2    2    2    |
    #+--------------------+      
    print("+--------------------+")
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j] != 0:
                print(grid[i][j]," "*(5-(len(str(grid[i][j])))),sep='',end='')
            else:
                print(" "*5,end='')
        print('|')    
    
    print("+--------------------+")

                
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    check1 = True
    check2 = True
    #checking for equal numbers adjacent to eachother
    for i in range(4):
        for j in range(4):
            if i == 0 and j==0:
                if grid[i+1][j] == grid[i][j] or grid[i][j+1] == grid[i][j]:
                    check1 = False
            elif i == 3 and j ==0:
                if grid[i-1][j] == grid[i][j] or grid[i][j+1] == grid[i][j]:
                    check1= False
            elif i ==0 and j == 3:
                if grid[i+1][j]==grid[i][j] or grid[i][j-1] == grid[i][j]:
                    check1 = False
            elif i ==3 and j ==3:
                if grid[i][j-1]==grid[i][j] or grid[i-1][j]==grid[i][j]:
                    check1 = False
            elif i == 0:
                if grid[i+1][j]==grid[i][j] or grid[i][j+1]==grid[i][j] or grid[i][j-1]==grid[i][j]:
                    check1 = False
            elif i ==3:
                if grid[i-1][j]==grid[i][j] or grid[i][j+1]==grid[i][j] or grid[i][j-1]==grid[i][j]:
                    check1 = False
            elif j == 0:
                if grid[i+1][j] == grid[i][j] or grid[i-1][j] == grid[i][j] or grid[i][j+1] == grid[i][j]:
                    check1 = False
            elif j == 3:
                if grid[i+1][j] == grid[i][j] or grid[i-1][j] == grid[i][j] or grid[i][j-1] == grid[i][j]:
                    check1 = False
            else:
                if grid[i+1][j] == grid[i][j] or grid[i-1][j] == grid[i][j] or grid[i][j+1] == grid[i][j] or grid[i][j-1] == grid[i][j]:
                    check1 = False
                
        #check for 0
        for i in range(4):
            for i in range(4):
                if grid[i][j] == '' :
                    check2 = False
        
        if check1 == True and check2 == True:
            return True
        else:
            return False
            #+--------------------+
            #|2         2         |
            #|     4         8    |
            #|     16        128  |
            #|2    2    2    2    |
            #+--------------------+        
            
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    test = False
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                test = True
    return test
def copy_grid (grid):
    """return a copy of the grid"""
    grid2 = grid
    return grid2
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    test = True
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                test = False
    
    return test