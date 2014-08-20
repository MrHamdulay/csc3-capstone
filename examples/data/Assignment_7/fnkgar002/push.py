"""Program used to create functions to merge grids
Gary Finkelstein
1 May 2014"""


#Create function to push grid up and merge
def push_up(grid):   
    
    #loop through the grid starting with second row, if the number above is equal to zero (a space), shift all numbers up. Do this 3 times. 
        for k in range(3): 
                for i in range(1,4):
                        for j in range(4):
                                if grid[i-1][j] == 0: 
                                        grid[i-1][j] = grid[i][j] 
                                        grid[i][j] =0 
     #if the number above is equal to the number below, add the two, put them in the topmost block and make the one below zero.            
        for i in range(1,4):
                for j in range(4):
                        if grid[i-1][j] == grid[i][j]:
                                grid[i-1][j] += grid[i][j]
                                grid[i][j] = 0
                                
 # get rid of 'spaces' that may have appeared due to the addition.
         
        for i in range(1,4):
                for j in range(4):
                        if grid[i-1][j] == 0:
                                grid[i-1][j] = grid[i][j]
                                grid[i][j] =0 
                                
                                
                                


#Create function to push grid down and merge
def push_down(grid):
        
        
        for k in range(3): 
                for i in range(2,-1,-1): #loop through the grid, if the block below is a space(0), shift down
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
                        for j in range(1,4): 
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
                        for j in range(2,-1,-1): #start at the second furthest right column. If the block to the right is zero, shift to the right.
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
                                
                                
                
                
                                
        
                                
        
                                