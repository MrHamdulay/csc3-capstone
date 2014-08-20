""" Sphiwe Muthembi
    Mthsph007
    Question 3 - Assignment 7"""


#===============================================
#Create functions that will be used to play game:
# Movements and directions

def push_up(grid):                                      #Up
    for i in range (len(grid)):
        for k in range( len(grid[i])):
            
            counter =1 
            
           # while counter < 4 :
            if grid[i][k] == grid[i + counter][k]:
                merge = grid[i][k] + grid[i+counter][k]
                grid.insert([0][k],merge)
                grid[i+counter][k] == ''
                    
                    
                counter +=1   
#=====================================================   Down                 
                    
def push_down(grid):
    
    for i in range (len(grid)):
        for j in range( len(grid)):
            
            counter = 2
            while counter > -1:
                
                if grid[i][j] == grid[i + counter][j]:
                    merge = grid[i][j] + grid[i + counter][j]
                    grid.insert([3][j],merge)
                    grid[i][j] == ''
                    
                counter-=1    
                    
#======================================================= Left

def push_left (grid):
    
    for i in range (len(grid)):
        for k in range(len(grid[i])):
            
            counter =1
            while counter < 4:
                
                if grid[i][k] == grid[i][k+ counter]:
                    merge = grid[i][k] + grid[i][k + counter]
                    grid.insert([i][0],merge)
                    grid[i][k + counter] == ''
                counter +=1    
                    
#====================================================== Right
def push_right (grid):
    
    for i in range (len(grid)):
        for k in range(len(grid[i])):
            
            counter =2
            while counter < 4:
                
                if grid[i][k] == grid[i][k+ counter]:
                    merge = grid[i][k] + grid[i][k + counter]
                    grid.insert([i][3],merge)
                    grid[i][k] == ''
                counter -=1    