'''This program manipulate 2-dimensional arrays of size 4x4
Sandile Christopher Mahlangu
29 April 2014'''

def create_grid(grid):
    """This function creats a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
def print_grid (grid):
    """This function prints out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')
    
    for vertical in range(4):
        print('|',end='')
        for horizontal in range(4):
            #Replace the zeros with empty strings
            if grid[vertical][horizontal]==0:
                print('{0:<5}'.format(' '),end='')

            else:
                print('{0:<5}'.format(grid[vertical][horizontal]),end='')
        print('|',end='')
        print()
    print('+--------------------+')

def check_lost (grid):
    """This functions returns True if there are no 0 values and no adjacent values that are equal in a grid; otherwise it rreturns False"""
    checker=  False
    counter=0
    #Checks if there are any zeros or empty spaces
    while not checker and counter<len(grid):
        for vertical in range(len(grid)):
            for horizontal in range(len(grid)):
                if grid[vertical][horizontal]==0:
                    return checker
            counter+=1
    
    
    #Checking if any adjacent values are the same
    for vertical in range(len(grid)):
        for horizontal in range(len(grid)):
            if vertical !=0 and vertical!=3 and horizontal!=0 and horizontal!=3:#Leaving out boarders
                    
                if grid[vertical][horizontal] == grid[vertical][horizontal-1] or grid[vertical][horizontal] == grid[vertical][horizontal+1] or grid[vertical][horizontal] == grid[vertical-1][horizontal] or grid[vertical][horizontal] == grid[vertical+1][horizontal]: #Checking adjacent values in the middle
                    return False
           
            #Checking around the boarders and edges of the grid 
            elif vertical==0 and horizontal==0:
                if grid[vertical][horizontal] == grid[vertical+1][horizontal] or grid[vertical][horizontal] == grid[vertical][horizontal+1]:
                    return False
            elif vertical ==3 and horizontal ==0:
                if grid[vertical][horizontal] == grid[vertical-1][horizontal] or grid[vertical][horizontal] == grid[vertical][horizontal+1]:
                    return False 
            elif vertical==3 and horizontal ==3:
                if grid[vertical][horizontal] == grid[vertical-1][horizontal] or grid[vertical][horizontal] == grid[vertical-1][horizontal-1]:
                    return False
            elif horizontal ==0:
                if grid[vertical][horizontal] == grid[vertical][horizontal+1]:
                    return False
            elif horizontal==3 :
                if grid[vertical][horizontal] == grid[vertical][horizontal-1]:
                    return False
            elif vertical==0:
                if grid[vertical][horizontal] == grid[vertical+1][horizontal]:
                    return False
            elif vertical==3:
                if grid[vertical][horizontal] == grid[vertical-1][horizontal]:
                    return False
                
    return not checker
def check_won (grid):
    """This function returns True if a value>=32 is found in the grid; otherwise False"""
    for vertical in range(len(grid)):
                for horizontal in range(len(grid)):
                    if grid[vertical][horizontal]>=32:

                        return True 
    return False 

def copy_grid (grid):
    """This function returns a copy of the given grid"""
    new_grid=[]#Making a new grid
    for i in range(len(grid)):
            new_grid.append([' ']*4)    
    for vertical in range(len(grid)):
        for horizontal in range(len(grid)):
            new_grid[vertical][horizontal]=grid[vertical][horizontal]#assigning values to the new grid
    return new_grid

def grid_equal (grid1, grid2):
    """This function checks if 2 grids are equal then returns boolean value"""
    for vertical in range(len(grid1)):
            for horizontal in range(len(grid1)):
                if grid2[vertical][horizontal]!=grid1[vertical][horizontal] :
                    return False
    return True 