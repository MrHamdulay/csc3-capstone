'''IRFAN HABIB
   Utility program
   2014/05/01'''

global grid
grid = []

def create_grid (grid):
    for j in range(4):
        row = []
        for k in range(4):
            row.append(0)# build a list of 4 zeros
        grid.append(row)   # add to the main array
        

def print_grid (grid):
    print('+', 20*'-','+', sep ='')
    for  i in range(4):
            for j in range(4):
                if j == 0:
                    print('|',end='')                
                if grid[i][j] == 0:
                    print("{0:<5}".format(" "), end="")
                else:
                    print("{0:<5}".format(grid[i][j]), end="")
                if j == 3:
                    print('|',end='\n')       
    print('+', 20*'-','+', sep ='')

def check_lost(grid):
    
    for i in range(4):
        
        for num in range(4):
            if grid[i][num] == 0:
                return False
        
        for num in range(3):
            if grid[i][num] == grid[i][num+1]:
                return False

    for i in range(3):
        for num in range(4):
            if grid[i][num] == grid[i+1][num]:
                return False
   
    return True
def check_won (grid):
    for i in grid:
        for a in i:
            if a >= 32:
                return True
    return False

def copy_grid(grid) :
    copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            copy[i][j] = grid[i][j]
    return copy

def grid_equal (grid1,grid2):
    for i in range(4):
            for j in range(4): 
                if grid1[i][j] != grid2[i][j]:
                    return False
    return True


    
            
            
    
        
        
        
    