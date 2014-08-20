''' a module of utility functions to manipulate 2-dimensional arrays of size 4x4
sankara mallane
29 april 2014'''

# create a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])
    
# print out a 4x4 grid in 5-width columns within a box
def print_grid (grid):
    print("+--------------------+")    
    
    for row in range (4):
        print('|',end='')
        for column in range (4):
            if grid[row][column] == 0:
                print('     ',end='')
            else:
                print("{:<5}".format(grid[row][column]),end='')
        print('|')

    print('+--------------------+')
        
# return True if there are no 0 values and no adjacent values that are equal; otherwise False      
def check_lost (grid):
    for row in range (4):
        
        for column in range (4):
            if grid[row][column] == 0:
              
                return False
            
            elif column-1 >= 0 and grid[row][column-1] == grid[row][column]:
               
                return False
            
            elif column < 3 and grid[row][column+1] == grid[row][column]:
             
                return False
            
            elif row-1 >= 0 and grid[row-1][column] == grid[row][column]:
               
                return False    
            
            elif row + 1 <= 3 and grid[row+1][column] == grid[row][column]:
                
                return False  
    return True

#return True if a value>=32 is found in the grid; otherwise False
def check_won (grid):
    for row in range (4):
        
        for column in range (4):
            if grid[row][column] >= 32:
                
                return True
    return False    

#return a copy of the grid          
def copy_grid (grid):
    grid2 = []
    for i in range(4):
        grid2.append([0]*4)

    for row in range (4):
        
        for column in range (4):
            grid2[row][column] = grid [row][column]
    
    return grid2

#check if 2 grids are equal - return boolean value
def grid_equal (grid1, grid2):
    for row in range (4):
        
        for column in range (4):
            if grid2[row][column] != grid1 [row][column]:    
                return False
    return True
