""" Yonela Ford
30 April 2014
Manipulating 2-D arrays of size 4X4"""

"""create a 4x4 grid"""
def create_grid(grid):
    #make a 4X4 grid
    height=4
    for i in range (height):
        #make a list and extend it
        grid.append([0]*4)
                    

"""print out a 4x4 grid in 5-width columns within a box""" 
def print_grid(grid):
    #create top part of frame
    print("+","-"*20,"+",sep="")
    
    #create grid
    height=4
    for i in range (height):
        grid.append([0]*4)
    for row in range (height):
        print("|",end="")
        for col in range (height):
            if grid[row][col]==0:
                print(" ".ljust(5), end="")
            else:
                print (str((grid[row][col])).ljust(5),end="")
        print("|")
    
    #create bottom part of grid
    print("+","-"*20,"+",sep="")
   


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:                                     
                return False                                        #return False if gird has entries with value 0
        for k in range(3):   
            if grid[i][k] == grid[i][k+1]:
                return False                                        #return False if grid has adjacent values equal
            elif grid[k][i] == grid[k+1][i]:
                return False                                        #return False if grid has adjacent values equal
    return True

"""return True if a value>=32 is found in the grid; otherwise False"""
def check_won (grid):
    for i in grid:
        for j in i:
            if j>=32:
                return True
    return False

"""return a copy of the grid"""
def copy_grid (grid):
    import copy
    y=copy.deepcopy(grid)
    return y

"""check if 2 grids are equal - return boolean value"""
def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False




  

                
                
    


