""""Module creating functions to make the 2048 game
JP Lanser
27 April 2014"""


#Make a function to create a 4x4 grid containing zeros
#The parameter passed in as an empty list
def create_grid(grid):
    
    for i in range(4):
        grid.append([0]*4)
        
    return grid

#Make a function to print out a 4x4 grid in 5 width columns within a box
# Use nested loops and print out as required per sample I/0
def print_grid(grid):
    print('+','-'*20,'+', sep="")
    for i in range(4):
        print('|', end="")
        for j in range(4):
            if grid[i][j] == 0:
                x=" "  #print a space instead of actually printing the number zero in the grid.
            else: x= grid[i][j]
            format_to_width_five = "{0:<5}".format(x)
            print( format_to_width_five, end="")            
            
        print('|')
    print('+','-'*20,'+', sep="")
    
#return True if there are no 0 values and no adjacent values that are equal; otherwise False  
def check_lost(grid):
    for x in range(4):    #Check that there are no 0 values in grid        
        for y in range(4):
            if grid[x][y] == 0:
                return False 
    
     
#Now check for adjacent values equal bearing in mind that there are no zeroes in the grid anymore.
    
    for i in range(4):
        for j in range(4):
             
            if i ==0 and j==0: #This is the upper left block. Check if the block BELOW or to the RIGHT have the same value:
                if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
                    return False
                
            elif i==3 and j==0: #This is the lower left block. Check if the block ABOVE or to the RIGHT have the same values
                if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i-1][j]:
                    return False
                                
            elif i==3 and j==3: #This is the lower RIGHT block. Check if the block ABOVE or to the LEFT have the same values
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i-1][j]:
                    return False
                
            elif i==0 and j==3: #This is the top right block. Check if the block BELOW or to the LEFT have the same values
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j]:
                    return False
                
                
                
            elif i ==1 and j==0:  #These are the two far left (middle) blocks, check if they are equal.
                if grid[i][j] == grid[i+1][j]:
                    return False
                    
                    
            elif i ==0 and j==1:  #These are the two top (middle)  blocks, check if they are equal.
                if grid[i][j] == grid[i][j+1]:
                    return False
                
                
            elif i ==1 and j==3:  #These are the two far right (middle), check if they are equal.
                if grid[i][j] == grid[i+1][j]:
                    return False    
                
            elif i ==3 and j==1:  #These are the two bottom (middle), check if they are equal.
                if grid[i][j] == grid[i][j+1]:
                    return False            
                         
            
            
            
            #Now for the middle 4 blocks, check if the block BELOW, ABOVE, RIGHT or LEFT have the same value: After this all options have been checked
            elif (i==1 and j==1) or (i==1 and j==2) or (i==2 and j==1) or (i==2 and j==2) :
                
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i-1][j] :
                    return False
            
            
    return True
    
        
    
#Make a function to return True if a value>=32 is found in the grid; otherwise False    
def check_won(grid):
    
    for i in range(4):
        
        for j in range(4):
            
            
            
            if grid[i][j]>=32:
             
                return True
    return False
            
            
            
#Make a function to return a copy of the grid
def copy_grid(grid):
    copy=[[],[],[],[]] #create empty list (4 lists within list)
    #Use nested loops to add each part of old list to the copy
    for i in range(4):        
        for j in range(4):            
            copy[i].append(grid[i][j])
               
            
    return copy
            

# Make a function to check if 2 grids are equal - then return boolean value
def grid_equal(grid1, grid2):
    
    for i in range(4):  #loop through both lists and if corresponding parts aren't equal return False
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
            
    return True

                       
            
    
        
    
    
    
    
    
    
    
            


    
    
    
