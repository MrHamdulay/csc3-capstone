"""Utility Class for 2048 Grid"""
#Liam Brodie
#BRDLIA004
#April 2014


def create_grid(grid):
    """create a 4x4 grid"""  
    for i in range(4):
        grid.append([0]*4)
        

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range (4):
        print("|",end="")
        for j in grid[i]:
            if j != 0:
                print(str(j)+(5-len(str(j)))*" ",end="")
            else:
                print("     ",end="")
        print("|")
    print("+--------------------+")
        
    
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if(grid[i][j]==0): 
                return False
            elif i==3 and j==3:
                return True
            elif i==3:
                if((grid[i][j]==grid[i][j+1])):
                    return False
            elif j==3:
                if(grid[i][j]==grid[i+1][j]):
                    return False
                
            elif(grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1]):
                return False
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j>=32:
                return True
    return False
            
        

def copy_grid (grid):
    """return a copy of the grid"""
    gridCopy=[]
    for i in range (4):
        CopyPart=[]
        for j in range(4):
            CopyPart.append(grid[i][j])
        gridCopy.append(CopyPart)
    return gridCopy
    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range (4):
            for j in range(4):
                if(grid1[i][j]!=grid2[i][j]):
                    return False
    return True
          