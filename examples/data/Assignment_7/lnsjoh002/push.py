"""Functions/Module to merge grids for the game 2048
JP Lanser
27 April 2014"""


#Create function to push grid up and merge
def push_up(grid):   
    
    #loop through the grid starting with second row, if the number above is equal to zero (a space), shift all numbers up. Do this 3 times. i.e. loop 3 times to ensure no spaces left at the top
        for k in range(3): #loop 3 times to ensure no spaces
                for i in range(1,4):
                        for j in range(4):
                                if grid[i-1][j] == 0: #If the number above is zero
                                        grid[i-1][j] = grid[i][j] 
                                        grid[i][j] =0 #Set the zero to the below number, effectively shifting up
     #loop through the grid, starting with the second row, if the number above is equal to the number below, add the two, put them in the topmost block and make the one below zero.            
        for i in range(1,4):
                for j in range(4):
                        if grid[i-1][j] == grid[i][j]:
                                grid[i-1][j] += grid[i][j]
                                grid[i][j] = 0
                                
 #repeat first step to get rid of 'spaces' that may have appeared as a result of the addition. Not necessary to loop three times this time. 1 is sufficient
         
        for i in range(1,4):
                for j in range(4):
                        if grid[i-1][j] == 0:
                                grid[i-1][j] = grid[i][j]
                                grid[i][j] =0 
                                
                                
                                
#Same sort of algorithm can be used to create the other functions, minor adjustments necessary for each one


#Create function to push grid down and merge
def push_down(grid):
        #use the same process, get rid of spaces, ADD, get rid of spaces again.
        
        for k in range(3): 
                for i in range(2,-1,-1): #loop through the grid, starting with second bottom row, if the block below is a space(0), shift down
                        for j in range(4): 
                                if grid[i+1][j] ==0:
                                        grid[i+1][j] = grid[i][j]
                                        grid[i][j] = 0
                                
        for i in range(2,-1,-1):
                for j in range(4):
                        if grid[i+1][j] == grid[i][j]:
                                grid[i+1][j] += grid[i][j]
                                grid[i][j] =0
                                
                                
        
        for i in range(2,-1,-1): 
                for j in range(4): 
                        if grid[i+1][j] ==0:
                                grid[i+1][j] = grid[i][j]
                                grid[i][j] = 0        
            
    
    
#Create function to shift grid left and merge      
def push_left(grid):
        
        for k in range(3):
        
                for i in range(4):
                        for j in range(1,4): #start in the second column, if block to the left is zero, shift left. Same process as used in above functions
                                if grid[i][j-1]==0:
                                        grid[i][j-1] = grid[i][j]
                                        grid[i][j] = 0
                                        
        for i in range(4):
                for j in range(1,4):
                        if grid[i][j-1] == grid[i][j]:
                                grid[i][j-1]+=grid[i][j]
                                grid[i][j] =0
                                
     
        for i in range(4):
                for j in range(1,4): 
                        if grid[i][j-1]==0:
                                grid[i][j-1] = grid[i][j]
                                grid[i][j] = 0  
                                        
                                        
#Create function to push grid right and merge       
def push_right(grid):  
        
        for k in range(3):
                for i in range(4):
                        for j in range(2,-1,-1): #start at the second furthest right column. If the block to the right is zero, shift right. Use same process as in above functions
                                if grid[i][j+1] ==0:
                                        grid[i][j+1] = grid[i][j]
                                        grid[i][j] =0
                                        
        for i in range(4):
                for j in range(2,-1,-1):
                        if grid[i][j+1] == grid[i][j]:
                                grid[i][j+1]+=grid[i][j]
                                grid[i][j]=0
                                
                                
       
        for i in range(4):
                for j in range(2,-1,-1): 
                        if grid[i][j+1] ==0:
                                grid[i][j+1] = grid[i][j]
                                grid[i][j] =0                
                                
                                
                
                
                                
        
                                
        
                                