#Ikhlaas Pohplonker
#29 April 2014
#
import copy
def create_grid(grid):#creates a 4x4 grid
    for i in range (4):
        grid.append([0]*4)
    return grid
def print_grid(grid):#prints out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    for row in range (4):
        print("|",end="")
        for col in range (4):
            if grid[row][col]!=0:
                y=("{0:<5}").format(grid[row][col])
                print(y,end="")
            if grid[row][col]==0:
                x=("{0:<5}").format(" ")
                print(x,end="")                
        print("|")
    print("+--------------------+")     
def check_lost (grid):#returns True if there are no 0 values and no adjacent values that are equal; otherwise False
    lost=True
    for row in range (4):
        for col in range (4):
            if row==0 and col==0:
                if grid[row][col]==0 or grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col+1]:
                                lost=False
                                break
            elif row==3 and col==3:
                if grid[row][col]==0 or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row][col-1]:
                                lost=False
                                break  
            elif row==0 and col==3:
                if grid[row][col]==0 or grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col-1]:
                                lost=False
                                break 
            elif row==3 and col==0:
                if grid[row][col]==0 or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row][col+1]:
                                lost=False
                                break            
            elif row==0:
                if grid[row][col]==0 or grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row][col-1]:
                                lost=False
                                break
            elif row==3:
                if grid[row][col]==0 or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row][col-1]:
                                lost=False
                                break 
            elif col==0:
                if grid[row][col]==0 or grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row][col+1]:
                                lost=False
                                break 
            elif col==3:
                if grid[row][col]==0 or grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row][col-1]:
                                lost=False
                                break 
            else:                
                if grid[row][col]==0 or grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row][col-1]:
                    lost=False
                    break
    return lost
def check_won (grid):#returns True if a value>=32 is found in the grid; otherwise False
    won=False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                won=True
                break
    return won       
def copy_grid (grid):#return a copy of the grid
    second_grid=copy.deepcopy(grid)
    return second_grid
def grid_equal (grid1, grid2):#checks if 2 grids are equal - returns tur if they are equal; otherwise false
    isequal=True
    for row in range (4):
        for col in range(4):
            if grid1[row][col]!=grid2[row][col]:
                isequal=False
                break
    return isequal
    