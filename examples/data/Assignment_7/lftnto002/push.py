"""functions for merging grid values in 2048 game
   Bridgette Lefatsa
   LFTNTO002
   2 May 2014"""                                                                                            
                    
                      
#merge grid values upwards
def push_up (grid):
           #movement
           for col in range(4):
                      for row in range(3):
                                 if grid[row][col]==0:
                                            grid[row][col]=grid[row+1][col]
                                            grid[row+1][col]=0    
            #merging                                
           for col in range(4):
                      for row in range(3):
                                 if grid[row][col] == grid[row+1][col]:
                                            grid[row][col]=grid[row+1][col]*2
                                            grid[row+1][col]=0
                                            
                                                                                 
    
        
    
    
#merge grid values downwards
def push_down (grid):
           #movement
           for col in range(4):
                      for row in range(3):
                                 if grid[row][col] == 0:
                                            grid[row+1][col] = grid[row][col]
                                            grid[row][col] = 0               
           #merging
           for col in range(4):
                      for row in range(3):
                                 if grid[row][col] == grid[row+1][col]:
                                            grid[row+1][col] = grid[row][col]*2
                                            grid[row][col] = 0
                                            
    
#merge grid values left
def push_left (grid):
           #movement
           for row in range(4):
                      for col in range(3):
                                 if grid[row][col] == 0:
                                            grid[row][col] = grid[row][col]
                                            grid[row][col+1] = 0                      
           
           #merging
           for row in range(4):
                      for col in range(3):
                                 if grid[row][col] == grid[row][col+1]:
                                            grid[row][col] = grid[row][col]*2
                                            grid[row][col+1] = 0
                                           
           
    
#merge grid values right
def push_right (grid):
           #movement
           for row in range(4):
                      for col in range(3):
                                 if grid[row][col] == 0:
                                            grid[row][col+1] = grid[row][col]
                                            grid[row][col] = 0           
           #merging
           for row in range(4):
                      for col in range(3):
                                 if grid[row][col] == grid[row][col+1]:
                                            grid[row][col+1] = grid[row][col]*2
                                            grid[row][col] = 0
                                                                            
    