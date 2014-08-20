#Program to merging functions that merge adjacent equal values and eliminate gaps
#Saul Bloch
#29 April 2014

#Function to push everything up and merge
def push_up(grid):   
    #Start in the second row as top row down not need to be moved up. Start top left
        #Loop 3 times for all 3 rows below top row
        for looper in range(3):
                for i in range(1,4):
                        for j in range(4):
                                if grid[i-1][j] == 0:
                                        grid[i-1][j] = grid[i][j] 
                                        grid[i][j] =0
        #Now if you shift up and the number above is the same as the one bolow, merge them and move them both up  
        for i in range(1,4):
                for j in range(4):
                        if grid[i-1][j] == grid[i][j]:
                                grid[i-1][j] += grid[i][j]
                                grid[i][j] = 0
                                
        #getting rid of extra spaces
        for i in range(1,4):
                for j in range(4):
                        if grid[i-1][j] == 0:
                                grid[i-1][j] = grid[i][j]
                                grid[i][j] =0 
                                
                                
#Function to push everything down and merge
#Similar function, just started looping from bottom, not top
def push_down(grid):
       #Start in the third row as dottom row does not need to be moved down. Start bottom left
        #Loop 3 times for all 3 rows above bottom row
        for looper in range(3): 
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
            
    
#Function to push everything left and merge  
#Similar function to top one, just started looping from left, not top
def push_left(grid):
        #Start in the second to left column far left column does not need to be moved left
                        #Loop 3 times for all 3 columns left of far left column        
        for looper in range(3):
        
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
                                        
                                        
#Function to push everything right and merge  
#Similar function to top one, just started looping from right, not top
def push_right(grid):  
        #Start in the second to right column far right column does not need to be moved right
        #Loop 3 times for all 3 columns right of far right column 
        
        for looper in range(3):
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
                