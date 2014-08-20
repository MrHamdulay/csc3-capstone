""""Program to create functions to create 2048
Gary Finkelstein
1 May 2014"""


#Make a function to create a 4x4 grid containing zeros

def create_grid(grid):
    
    for i in range(4):
        grid.append([0]*4)
        
    return grid

#Make a function to print out a 4x4 grid in 5 width columns within a box

def print_grid(grid):
    print("+--------------------+")
    
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col] ==0:
                print(" "*5, end="")
            else:
                print(grid[row][col],(5-len(str((grid[row][col]))))*" ", sep="",end="")
        print("|")
        
    print("+--------------------+")
    
#return True if there are no 0 values and no opposite values that are equal
def check_lost(grid):
    for x in range(4):    #Check that there are no 0 values in grid        
        for y in range(4):
            if grid[x][y] == 0:
                return False 
    
     
#Now check for adjacent values equal:
    
    for i in range(4):
        for j in range(4):
             
            if i ==0 and j==0:
                if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
                    return False
                
            elif i==3 and j==0: 
                if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i-1][j]:
                    return False
                                
            elif i==3 and j==3: 
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i-1][j]:
                    return False
                
            elif i==0 and j==3: 
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j]:
                    return False
                
                
                
            elif i ==1 and j==0:  
                if grid[i][j] == grid[i+1][j]:
                    return False
                    
                    
            elif i ==0 and j==1:  
                if grid[i][j] == grid[i][j+1]:
                    return False
                
                
            elif i ==1 and j==3: 
                if grid[i][j] == grid[i+1][j]:
                    return False    
                
            elif i ==3 and j==1:  
                if grid[i][j] == grid[i][j+1]:
                    return False            
                         
            
            elif (i==1 and j==1) or (i==1 and j==2) or (i==2 and j==1) or (i==2 and j==2) :
                
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i-1][j] :
                    return False
            
            
    return True
    
        
    
#Make a function to return True if a value>=32 is found in the grid
def check_won(grid):
    
    for i in range(4):
        
        for j in range(4):
            
            
            
            if grid[i][j]>=32:
             
                return True
    return False
            
            
            
#Make a function to return a copy of the grid
def copy_grid(grid):
    copygrid=[[],[],[],[]] #create empty list (4 lists within list)
    
    for i in range(4):        
        for j in range(4):            
            copygrid[i].append(grid[i][j])
               
            
    return copygrid
            

# Make a function to check if 2 grids are equal 
def grid_equal(grid1, grid2):
    
    for i in range(4):  
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
            
    return True

                       
            
    
        
    
    
    
    
    
    
    
            


    
    
    
