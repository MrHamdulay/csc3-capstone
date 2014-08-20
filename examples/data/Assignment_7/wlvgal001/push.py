#Push provides directions for moving in 2048
#Galya Wolov
# 1 May 2014

import util

#moves left to do so isolate the individual columns that are made by the 2 D Array
def push_left(grid): 
        
        for iterate in range(4):
                for row in range(4):
                        for col in range(3): 
                                #isolating step
                                #finds the zeroes and fills the "empty space" by shifting whole grid left
                                if grid[row][col] == 0:
                                        #shifting step
                                        grid[row][col+1]= grid[row][col]
                                        grid[row][col]=grid[row][col+1]   
                                        
        for iterate in range(4):
                for row in range(4):
                        for col in range(3): 
                                #isolating step
                                #finds the zeroes and fills the "empty space" by shifting whole grid left
                                if grid[row][col] == 0:
                                        #shifting step
                                        grid[row][col+1]= grid[row][col]
                                        grid[row][col]=grid[row][col+1]  
        
        #adds like numbers and shifts the whole grid left and then adds a 0 to the empty space was
        for row in range(4): 
                for col in range (3): 
                        #isolating step
                        if grid[row][col] == grid[row][col+1]:
                                #adds the numbers
                                grid[row][col]*=2
                                grid[row][col+1]=0 
                                
        
        return grid



#moves right to do so isolate the individual columns that are made by the 2 D Array
def push_right(grid):        
                                      
        for iterate in range(4):
                for row in range(4):
                        for col in range(3,0,-1): 
                        #isolating step
                        #finds the zeroes and fills the "empty space" by shifting whole grid right
                                if grid[row][col] == 0:
                                                #shifting step
                                                grid[row][col-1]=grid[row][col]
                                                grid[row][col]=grid[row][col-1]
        
        for iterate in range(4):
                for row in range(4):
                        for col in range(3,0,-1): 
                                #isolating step
                                #finds the zeroes and fills the "empty space" by shifting whole grid right
                                if grid[row][col] == 0:
                                #shifting step
                                        grid[row][col-1]=grid[row][col]
                                        grid[row][col]=grid[row][col-1]                                
                        
                                        
        for row in range(4):
                for col in range(3,0,-1): 
                        #isolating step
                        #adds like numbers and shifts the whole grid right and then adds a 0 to the empty space was
                        if grid[row][col] == grid[row][col-1]:
                                        grid[row][col]*=2
                                        grid[row][col-1]=0                         
                                
        return grid

#moves up to do so isolate the individual rows that are made by the 2 D Array                       
def push_up(grid):  
        for iterate in range(4):
                for row in range(3):
                        for col in range (3):
                                #finds the zeroes and fills the "empty space" by shifting whole grid down         
                                if grid[row][col] == 0:
                                #shifting step
                                        grid[row][col]=grid[row+1][col]
                                        grid[row+1][col]=grid[row][col]        
                        
        for iterate in range(4):
                for row in range(3):
                        for col in range (3):
                        #finds the zeroes and fills the "empty space" by shifting whole grid down         
                                if grid[row][col] == 0:
                                #shifting step
                                        grid[row][col]=grid[row+1][col]
                                        grid[row+1][col]=grid[row][col]
                                        
        for row in range(3):
                for col in range(4):
                        #isolating step
                        #adds like numbers and shifts the whole grid up and then adds a 0 to the empty space was                        
                        if grid[row][col]==grid[row+1][col]:
                                    grid[row][col]*=2
                                    grid[row+1][col]=0
                                                                                    
        return grid                                                                           

#moves down to do so isolate the individual rows that are made by the 2 D Array
def push_down(grid):   
        
        for iterate in range(4):
                for row in range(3,0,-1): #isolating step
                        for col in range(4):
                                #finds the zeroes and fills the "empty space" by shifting whole grid down         
                                if grid[row][col] == 0:
                                        #shifting step
                                        grid[row-1][col]=grid[row][col]
                                        grid[row][col]=grid[row-1][col]

                        
        for iterate in range(4):
                for row in range(3,0,-1): #isolating step
                        for col in range(4):
                                #finds the zeroes and fills the "empty space" by shifting whole grid down         
                                if grid[row][col] == 0:
                                #shifting step
                                        grid[row-1][col]=grid[row][col]
                                        grid[row][col]=grid[row-1][col]
                                        
        for row in range(3,0,-1): #adds like numbers and shifts the whole grid down and then adds a 0 to the empty space was
                for col in range(4):
                        if grid[row][col]==grid[row-1][col]:
                                #adds the numbers
                                grid[row][col]*=2
                                grid[row-1][col]=0  
        return grid
                                
                                
                            
                


                                
                        
        
            