"""functions to be used in a game
danica van der zandt
1 may 2014"""

#creating a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
        
    
#printing the 4x4 grid in coloumns of width five surrounded by a box        
def print_grid(grid):
        print("+"+"-"*20+"+")
        for row in range(4):
            print("|",end="")
            for col in range(4):
                if grid[row][col]==0:
                    print(" ".ljust(5),end='')
                else:
                    print(str(grid[row][col]).ljust(5),end="")
            print("|")
        print("+"+"-"*20+"+")



#return True if there are no 0 values and no adjacent values that are equal; otherwise False      
def check_lost(grid):
    #go through grid and see if there is a zero in it
    buffer_grid=[]
    for i in range(5):
            buffer_grid.append(["-1"]*5)    
    for i in range(0,4):
        for j in range(0,4):
            buffer_grid[i][j]=grid[i][j]
            
    for i in range(0,4):
        for j in range(0,4):
            if buffer_grid[i][j]=="0":
                return False
            else:
                if buffer_grid[i][j]==buffer_grid[i][j+1] or buffer_grid[i][j]==buffer_grid[i+1][j]:
                    return False
        
    return True
        #if there is no zero, go through the entire grid again and check for equal adj values (horizontally and vertically
 
 
#return True if a value>=32 is found in the grid; otherwise False
def check_won(grid):
    #scan through entire list and see if any item is 32 to greater
    for i in range(0,4):
        for j in range(0,4):
            if grid[i][j]>=32:
                return True
    return False


#return a copy of the grid
def copy_grid (grid):
    import copy
    new_grid= copy.deepcopy(grid)
    return new_grid
    
    
   
#check if 2 grids are equal - return boolean value 
def grid_equal (grid1, grid2):
    for i in range(0,4):
        for j in range(0,4):
            if grid1[i][j]!=grid2[i][j]:
                return False
    return True
    
         

