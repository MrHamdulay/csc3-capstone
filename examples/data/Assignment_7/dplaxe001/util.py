'''Util functions used for question 2 and 2048 game
Axel du Plessis
02-05-2014'''

def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
        
def print_grid(grid):
    form = '{0:<5}' 
    print("+--------------------+")
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                if col == 0:
                    print("|"+form.format(""),end = "")
                else:
                    print(form.format(""),end = "")
            else:
                if col == 0:
                    print("|"+form.format(str(grid[row][col])),end = "")
                else:
                    print(form.format(str(grid[row][col])),end = "")                
        print('|')
    print("+--------------------+")
        
#def check_lost(grid):
    #for row in range(4):
        #for col in range(4):  
            #if row == 3:
                #if col == 3:
                    #if grid[row][col] == 0:
                        #return False
                #else:
                    #if grid[row][col] == 0 or grid[row][col] == grid[row][col+1]:
                        #return False
            #elif col == 3:
                #if grid[row][col] == 0 or grid[row][col] == grid[row+1][col]:
                    #return False
            #else:
                #if grid[row][col] == 0 or grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row][col+1]:
                    #return False
                
    #return True

def check_lost(grid):
    for row in [0,1,2]:
        for col in range(4):  
            if grid[row][col] == 0 or grid[row][col] == grid[row+1][col]:
                    return False
    for row in range(4):
        for col in [0,1,2]:  
            if grid[row][col] == 0 or grid[row][col] == grid[row][col+1]:
                    return False               
    return True

def check_won(grid):
    for row in range(4):
            for col in range(4):     
                if grid[row][col] >=32:
                    return True
    return False

def copy_grid(grid):
    grid2 = []
    for i in range(4):
        grid2.append([" "]*4)
    
    for row in range(4):
            for col in range(4):          
                grid2[row][col] = grid[row][col]
    
    return grid2
    
def grid_equal(grid1,grid2):
    for row in range(4):
        for col in range(4):       
            if grid1[row][col] != grid2[row][col]:
                return False 
    return True 