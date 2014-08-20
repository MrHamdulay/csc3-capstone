"""functions that are needed for the Game
barak setton
27/04/2014"""
import util

def push_up (grid):
        for more in range(4):
                for col in range (4):
                        for row in range(3):
                                if grid[row][col] == 0:
                                        grid[row][col] = grid[row+1][col]   #  moving the numbers to the top
                                        grid[row+1][col]=0      
                        
        for col in range(4):
                for row in range(3):
                        if grid[row+1][col] == grid [row][col]:
                                grid[row][col] = 2*(grid[row][col])         # addint the matching numbers
                                grid[row+1][col] = 0                        
        for more in range(4):
                for col in range (4):
                        for row in range(3):
                                if grid[row][col] == 0:
                                        grid[row][col] = grid[row+1][col]   #  moving the numbers to the top
                                        grid[row+1][col]=0   
                                

def push_down (grid):
        for more in range(4):
                for col in range (4):
                        for row in range(3,0,-1):
                                if grid[row][col] == 0:
                                        grid[row][col] = grid[row-1][col]   # Moving the numbers all along the bottom 
                                        grid[row-1][col]=0      
                                
        for col in range(4):
                for row in range(3,0,-1):
                        if grid[row-1][col] == grid [row][col]:
                                grid[row][col] = 2*(grid[row][col])         # adding the maching the numbers together
                                grid[row-1][col] = 0 
                                
        for more in range(4):
                for col in range (4):
                        for row in range(3,0,-1):
                                if grid[row][col] == 0:
                                        grid[row][col] = grid[row-1][col]   # Moving then all along the bottom 
                                        grid[row-1][col]=0         

def push_left (grid):
        for more in range(4):
                for row in range (4):
                        for col in range(1,4):
                                if grid[row][col-1] == 0:
                                        grid[row][col-1] = grid[row][col]   # Moving the numbers all along the bottom 
                                        grid[row][col]=0      
        #util.print_grid (grid)                                               
        for row in range(4):
                for col in range(1,4):
                        if grid[row][col-1] == grid [row][col]:
                                grid[row][col-1] = 2*(grid[row][col])         # adding the maching the numbers together
                                grid[row][col] = 0 
         
        for more in range(4):                                                 # to make sure the rows are done multipal times
                for row in range (4):
                        for col in range(1,4):
                                if grid[row][col-1] == 0:
                                        grid[row][col-1] = grid[row][col]   # Moving then all along the bottom 
                                        grid[row][col]=0  
        #util.print_grid (grid) 

def push_right (grid):
        for more in range(4):
                for row in range (4):
                        for col in range(3,0,-1):
                                if grid[row][col] == 0:
                                        grid[row][col] = grid[row][col-1]   # Moving the numbers all along the bottom 
                                        grid[row][col-1]=0      
                                
        for row in range(4):
                for col in range(3,0,-1):
                        if grid[row][col-1] == grid [row][col]:
                                grid[row][col] = 2*(grid[row][col])         # adding the maching the numbers together
                                grid[row][col-1] = 0 
                                
        for more in range(4):
                for row in range (4):
                        for col in range(3,0,-1):
                                if grid[row][col] == 0:
                                        grid[row][col] = grid[row][col-1]   # Moving then all along the bottom 
                                        grid[row][col-1]=0          
