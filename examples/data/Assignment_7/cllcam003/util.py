 # program of fuctions for question 3
 # Cameron Collum
 # 29 April 2014

grid=[]
def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])
    return grid
    
def print_grid(grid):
    print("+--------------------+")    
    for i in range(4):
        print("|",end="")
        for j in range(4):
            if grid[i][j]!=0:
                print("{0:<5}".format(grid[i][j]),end="")
            else: 
                print("     ",end="")
        print("|")    
    print("+--------------------+") 

def check_lost(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return False
            else: continue   
    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1]:
                return False 
            else:
                continue
    
    for i in range(3):
        for j in range(4):
            if grid[i][j]==grid[i+1][j]:
                return False
            else:
                continue
    return True
def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True
            else:    
                continue
    return False
        
import copy
def copy_grid(grid):
    return copy.deepcopy(grid)

def grid_equal (grid1, grid2):
    for i in range(4):
            for j in range(4):
                if grid1[i][j]==grid2[i][j]:
                    continue
                else:
                    return False
    return True           
            
            
                
                
    
                            
                             
                        
                    
                    
    
    


    
    
    

 
        
        