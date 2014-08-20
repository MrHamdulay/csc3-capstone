"""QUESTION 2, Assignment 7
Charlie Shang
SHNHUA002"""

def create_grid (grid):
    #creates and empty 4x4 grid
    for y in range(4):
        row = []
        for x in range(4):
            row.append(0)
        grid.append(row)

def print_grid (grid): 
    #prints the grid with values padded by spaces so the length is 5 characters
    print('+', 20*'-' , '+', sep= '')
    
    for i in range(len(grid)):
        print('|', end = '') #border
        
        for num in grid[i]:    
            if num != 0:
                print("{0:<5}".format(num), end = '') 
            else:
                print("{0:<5}".format(' '), end = '')
        
        print('|')#border
    
    print('+', 20*'-' , '+', sep= '') #border
    

def check_lost(grid):
    
    for i in range(4): #returns false if 0 is found in grid
        for num in range(4):
            if grid[i][num] == 0:
                return False
        
        for num in range(3): #returns false if there are horizontally adjacent equal values
            if grid[i][num] == grid[i][num+1]:
                return False
            
    for i in range(3): #returns false if there are vertically adjacent equal values
        for num in range(4):
            if grid[i][num] == grid[i+1][num]:
                return False
            
    return True #returns true if all conditions are all not met

def check_won(grid):
    
    for i in grid: #return true if there is a value >= 32 in the grid
        for a in i:
            if a >= 32:
                return True
    return False

def copy_grid (grid):
    
    new_grid = []
    
    for i in grid: #loop through old grid and append its items to new grid
        new_row = []
        
        for k in i:
            new_row.append(k)
            
        new_grid.append(new_row)
        
    return new_grid

def grid_equal(grid1,grid2):
    
    for y in range(4): #loop through each grid
        for x in range(4):
            
            if grid1[y][x] != grid2[y][x]: #return false if corresponding elements do not match
                return False
            
    return True #returns true if there are matches
                           