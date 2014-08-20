
import copy
def create_grid(grid):
  
    for i in range(4):
        grid.append([0] * 4) 
    
def print_grid (grid):
   
    print("+--------------------+")    
    for rw in range (4):
        for colum  in range (4):
            if colum  == 0:
                print("|",end="")
            if grid[rw][colum ] == 0:
                print(" "*5,end="",sep="")
            if grid[rw][colum ] != 0:
                print(grid[rw][colum ]," "*(5-len(str(grid[rw][colum ]))),sep="",end="")
            if colum  == 3:
                print("|",end="")            
        print()
    print("+--------------------+")
        
    

def check_lost (grid):
   
    x = True
    for rw in range (4):
        for colum  in range(4):
            left = colum -1         
            right = colum +1
            top = rw-1
            bottom = rw+1           
            if grid[rw][colum ] == 0: 
                return False
            elif rw == 0 and colum  == 3: 
                if grid[rw][colum ] == grid[bottom][colum ] or grid[rw][colum ] == grid[rw][left]: 
                    return False
            elif rw == 0 and colum  == 0:
                if grid[rw][colum ] == grid[bottom][colum ] or grid[rw][colum ] == grid[rw][right]:
                    return False
            elif rw == 3 and colum  == 0:   
                if grid[rw][colum ] == grid[top][colum ] or grid[rw][colum ] == grid[rw][right]:
                    return False
            elif rw == 3 and colum  == 3:  
                if grid[rw][colum ] == grid[top][colum ] or grid[rw][colum ] == grid[rw][left]:
                    return False            
            elif rw == 0: 
                if grid[rw][colum ] == grid[bottom][colum ] or grid[rw][colum ] == grid[rw][left] or grid[rw][colum ] == grid[rw][right]:
                    return False
            elif rw == 3: 
                if grid[rw][colum ] == grid[top][colum ] or grid[rw][colum ] == grid[rw][left] or grid[rw][colum ] == grid[rw][right]:
                    return False    
            elif colum  == 0: 
                if grid[rw][colum ] == grid[rw][right] or grid[rw][colum ] == grid[top][colum ] or grid[rw][colum ] == grid[bottom][colum ]:
                    return False
            elif colum  == 0:
                if grid[rw][colum ] == grid[rw][left] or grid[rw][colum ] == grid[top][colum ] or grid[rw][colum ] == grid[bottom][colum ]:
                    return False  
    return True
            
            
            
        
            
                
    

def check_won (grid):
    
    x = False
    for rw in range(4):
        for colum  in range(4):
            
            if grid[rw][colum ] >= 32:
                return True
    return x

def copy_grid (grid):
   
    gridcopy = copy.deepcopy(grid)
    return gridcopy 

def grid_equal (grid1, grid2):
    
    return grid1 == grid2