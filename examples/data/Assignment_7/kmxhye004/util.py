
import copy
def create_grid(grid):
  
    for i in range(4):
        grid.append([0] * 4) 
    
def print_grid (grid):
   
    print("+--------------------+")    
    for rows in range (4):
        for column  in range (4):
            if column  == 0:
                print("|",end="")
            if grid[rows][column ] == 0:
                print(" "*5,end="",sep="")
            if grid[rows][column ] != 0:
                print(grid[rows][column ]," "*(5-len(str(grid[rows][column ]))),sep="",end="")
            if column  == 3:
                print("|",end="")            
        print()
    print("+--------------------+")
        
    

def check_lost (grid):
   
    x = True
    for rows in range (4):
        for column  in range(4):
            left = column -1         
            right = column +1
            top = rows-1
            bott = rows+1           
            if grid[rows][column ] == 0: 
                return False
            elif rows == 0 and column  == 3: 
                if grid[rows][column ] == grid[bott][column ] or grid[rows][column ] == grid[rows][left]: 
                    return False
            elif rows == 0 and column  == 0:
                if grid[rows][column ] == grid[bott][column ] or grid[rows][column ] == grid[rows][right]:
                    return False
            elif rows == 3 and column  == 0:   
                if grid[rows][column ] == grid[top][column ] or grid[rows][column ] == grid[rows][right]:
                    return False
            elif rows == 3 and column  == 3:  
                if grid[rows][column ] == grid[top][column ] or grid[rows][column ] == grid[rows][left]:
                    return False            
            elif rows == 0: 
                if grid[rows][column ] == grid[bott][column ] or grid[rows][column ] == grid[rows][left] or grid[rows][column ] == grid[rows][right]:
                    return False
            elif rows == 3: 
                if grid[rows][column ] == grid[top][column ] or grid[rows][column ] == grid[rows][left] or grid[rows][column ] == grid[rows][right]:
                    return False    
            elif column  == 0: 
                if grid[rows][column ] == grid[rows][right] or grid[rows][column ] == grid[top][column ] or grid[rows][column ] == grid[bott][column ]:
                    return False
            elif column  == 0:
                if grid[rows][column ] == grid[rows][left] or grid[rows][column ] == grid[top][column ] or grid[rows][column ] == grid[bott][column ]:
                    return False  
    return True
            
            
            
        
            
                
    

def check_won (grid):
    
    x = False
    for rows in range(4):
        for column  in range(4):
            
            if grid[rows][column ] >= 32:
                return True
    return x

def copy_grid (grid):
   
    gridcopy = copy.deepcopy(grid)
    return gridcopy 

def grid_equal (grid1, grid2):
    
    return grid1 == grid2