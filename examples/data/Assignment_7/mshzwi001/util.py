# a module of utility functions (called util.py) to manipulate 2-dimensional arrays of size 4x4
# mashau zwivhuya
# 30 april 2014

#create a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)  
    return grid    
#print out a 4x4 grid in 5-width columns within a box 
def print_grid (grid):
        b="+--------------------+"
        print(b)
        
        """for x in range(4):
                for y in range(4):
                        if (grid[x][y] == 0):
                                grid[x][y] = 0"""

        for y in range(4):
            print("|",end="")
            for x in range(4):
                    if grid[y][x] != 0:
                        print("{0:<5}".format(grid[y][x]),end="")
                    else:
                        print("{0:<5}".format(""),end="")
            print("|")
        print(b)
    
#return True if a value>=32 is found in the grid; otherwise False
def check_won (grid):
    k=False
    for i in grid:
        for j in i:
            if j >=32:
                k=True
    return k

#return a copy of the grid             
def copy_grid (grid):
    grid2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    for x in range(4):
        for y in range(4):
            grid2[x][y] = grid[x][y]
    return grid2            
                        
    
#check if 2 grids are equal - return boolean value            
def grid_equal (grid1,grid2):            
        k= True
        for x in range(4):
            for y in range(4):
                if grid2[x][y] != grid1[x][y]:
                    k=False

        if k is True:
            return True
        else:
            return False
        
        
# return True if there are no 0 values and no adjacent values that are equal; otherwise False     
def check_lost (grid):
    k=True
    #horizontal for the first grid
    if grid[0][0] ==grid[0][1] :
        k=False
    if grid[0][1] ==grid[0][0] or grid[0][1]==grid[0][2] :
        k=False 
    if grid[0][2] ==grid[0][1] or grid[0][2]==grid[0][3]:
        k=False 
    if grid[0][3]==grid[0][2]:
        k=False   
     #horizontal for the second grid
    if grid[1][0] ==grid[1][1]:
        k=False
    if grid[1][1] ==grid[1][0] or grid[1][1]==grid[1][2] :
        k=False 
    if grid[1][2]==grid[1][1] or grid[1][2]==grid[1][3]:
        k=False 
    if grid[1][3]==grid[1][2]:
        k=False 
    #horizontal for the third grid
    if grid[2][0] ==grid[2][1] :
        k=False
    if grid[2][1] ==grid[2][0] or grid[2][1]==grid[2][2]:
        k=False 
    if grid[2][2]==grid[2][1] or grid[2][2]==grid[2][3]:
        k=False 
    if grid[2][3]==grid[2][2]:
        k=False     
    #horizontal for the forth grid
    if grid[3][0] ==grid[3][1] :
        k=False
    if grid[3][1] ==grid[3][0] or grid[3][1]==grid[3][2]:
        k=False 
    if grid[3][2]==grid[3][1] or grid[3][2]==grid[3][3]:
        k=False 
    if grid[3][3]==grid[3][2]:
        k=False     
    
    # for the vertical line 1
    if grid[0][0] ==grid[1][0] :
        k=False
    if grid[1][0] ==grid[0][0] or grid[1][0]==grid[2][0] :
        k=False
    if grid[2][0]==grid[1][0] or grid[2][0]==grid[3][0]:
        k=False    
    if grid[3][0]==grid[2][0]:
        k=False
    # for the vertical line 2
    if grid[0][1] ==grid[1][1] :
        k=False
    if grid[1][1] ==grid[0][1] or grid[1][1]==grid[2][1]:
        k=False
    if grid[2][1]==grid[1][1] or grid[2][1]==grid[3][1]:
        k=False    
    if grid[3][1]==grid[2][1]:
        k=False
    # for the vertical line 3
    if grid[0][2] ==grid[1][2] :
        k=False
    if grid[1][2] ==grid[0][2] or grid[1][2]==grid[2][2]:
        k=False
    if grid[2][2]==grid[1][2] or grid[2][2]==grid[3][2]:
        k=False    
    if grid[3][2]==grid[2][2]:
        k=False  
    # for the vertical line 3
    if grid[0][3] ==grid[1][3] :
        k=False
    if grid[1][3] ==grid[0][3] or grid[1][3]==grid[2][3]:
        k=False
    if grid[2][3]==grid[1][3] or grid[2][3]==grid[3][3]:
        k=False    
    if grid[3][3]==grid[2][3]:
        k=False
    return k
        
