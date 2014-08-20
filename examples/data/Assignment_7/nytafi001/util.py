""" A module of utility functions to manipulate 2-dimensional arrays of size 4x4.
Author: Afika Nyati
Date: 1st May 2014"""

from copy import * # Imports all the functions from the copy library. I specifically use the deepcopy function to clone lists in one of the functions.

def create_grid(grid): # Creates a 4 X 4 Grid
    
    for i in range(4): # A definite loop that creates a 1D array four times to create the 2D array.
        grid.append([0,0,0,0]) # Adds a four value array to an empty list.
        
        
        
def print_grid(grid): # A fucntion that prints the grid placed as an arguement.
    
    formatting = "{:<5}" # Creating the formatting to each value in the 2D array in a neat five width space.
    
    print("+" + "-"*20 + "+") # Prints the top of the box in which the numbers are in.
    
    for y in range(4): # Loops through each row
        
        print ("|", end = "") # Prints the boundary of the box on each row.
        
        for x in range(4): # Loops through each value in one row
                if grid[y][x] != 0:  # If the given value in the given row and column is not equal to zero, it is printed on the screen with the formatting
                    print(formatting.format(grid[y][x]), end ="") # By using end ="", the next print statement won't go to the next line.
                    
                else: # If the given value in the given row and column is zero, it prints a blank space in the formatting.
                    print(formatting.format(" "), end ="") # By using end ="", the next print statement won't go to the next line.
        
        print("|") # This print statement closes the boundary of the given line
     
    print("+" + "-"*20 + "+") # Prints the bottom of the box in which the numbers are in
                
    

def check_lost(grid): # A function that checks whether a 2048 game is over.
    
    for y in range(4): # Loops through each row
        
        for x in range(4): # Loops through each value in one row.
            
            if (grid[y][x] == 0): return False # If the given value in the given row and column is equal to zero, the game is not over and thereby returns False.
            
            elif (y==3 and x==3): return True # If the loops reach the last value of the grid, while no zeros or adjacent values were found, the game is over and thereby returns True.
            
            elif (y==3): # For values in the bottom row of the grid, check whether the left adjacent number is equal to value.
                
                if((grid[y][x]==grid[y][x+1])): return False # If the number is equal, the game is not over and thereby returns False.
            
            elif (x==3): # For values in the last column of the grid, check whether the bottom adjacent number is equal to value.
                
                if(grid[y][x]==grid[y+1][x]): return False # If the number is equal, the game is not over and thereby returns False.
                
            elif (grid[y][x]==grid[y+1][x] or grid[y][x]==grid[y][x+1]): return False # For all other values in the grid, check whether the botom adjacent number or right adjacent number is equal to value.
            
            # *** There is no need to check all four surrounding values for each number because there will be many repeats of checking. The method I've used tries to make sure all adjacents are checked, but with the least amount of repeated checks.
         
           
                
def check_won(grid): # Checks whether the game is won.
    
    
    for y in range(4): # Loops through each row
        
        for x in range(4): # Loops through each value in one row.
            
            if grid[y][x] >= 32: # If the given value in the given row and column is bigger or equal to 32, the game is won and thereby True is returned.
                
                return True
                
    return False # If the loop is finished and none of the values are bigger or equal to 32, the game isn't won, and thereby False in returned.
  
  
  
    
    
def copy_grid(grid): # Clones a grid inputed as an arguement and returns the cloned grid
    
    new_grid = deepcopy(grid) # This line uses the deepcopy function from the clone library. This function is required so that a shallow copy is not performed. Shallow copies don't create a new independent grid. The values of the original grid and the new grid are still linked.
    
    return new_grid
    



    
def grid_equal(grid1, grid2): # A function that checks whether two grids inputed as arguements are equal.
    
    
    for y in range(4): # Loops through each row
        
        for x in range(4): # Loops through each value in one row.
            
            if grid1[y][x] != grid2[y][x]: # If the given value in the given row and column in one grid is not equal to the equivalent in the other grid, the two grids arent equal. As a result, return False.
                
                return False
            
    
    return True # If the loop is finished and all of the values are equal, the grids are equal, and thereby False in returned.


