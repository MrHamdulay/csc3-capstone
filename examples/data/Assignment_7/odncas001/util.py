"""grid manipulation functions for 2048 game
casey o'donnell
27 april 2014"""

def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
    return (grid)
        
    
def print_grid(grid):
    print("+","-"*20,"+",sep="")
    for row in range(len(grid)):
        print("|",end="")
        for col in range(len(grid)):
            a=grid[row][col]
            if a==0:
                a=""
            print("{0:<5}".format(a),end="")
        print("|") 
    print("+","-"*20,"+",sep="")
    
def check_lost(grid):
    #check for zeros
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col]==0:
                return False
    #check for adjacent equivalence within rows
    for row in range(len(grid)):
        for col in range(len(grid)-1):
            if grid[row][col]==grid[row][col+1]:
                return False
    #check for adjacent equivalence within columns
    for row in range(len(grid)-1):
        for col in range(len(grid)):
            if grid[row][col]==grid[row+1][col]:
                return False
    return True

def check_won(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col]>=32:
                return True
    return False

def copy_grid(grid):
    new_grid=create_grid([])
    for row in range(len(grid)):
        for col in range(len(grid)):
            new_grid[row][col]=grid[row][col]
    return new_grid

def grid_equal(grid1, grid2):
    for row in range(len(grid1)):
        for col in range(len(grid1)):
            if grid1[row][col]!=grid2[row][col]:
                return False
    return True
    

        
    
        
        
        
        
        
    