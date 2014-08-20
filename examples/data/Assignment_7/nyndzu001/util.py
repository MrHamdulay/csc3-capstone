"""Dzunisani"""
import copy

def create_grid(grid):
    
    height=4
    for i in range(height):
        grid.append([0]*4)    
    return grid

def print_grid(grid):
    print("+"+("-"*20)+"+")
    for col in range(4):
        print("|",end="")
        for row in range(4):
            if grid[col][row]==0:
                print("{:<5}".format(" "),end="")
            else:
                print("{:<5}".format(grid[col][row]),end="")
        print("|")
    print("+"+("-"*20)+"+")
    
def check_lost(grid):
      
    for col in range(len(grid)-1):
        for row in range(len(grid[col])-1):
            if grid[col][row]==0:
                return False        
            
            elif grid[col][row] == grid[col][row+1]:
                return False
                
            elif grid[col][row] == grid[col+1][row]:
                return False
             
        else:
            return True
            
def check_won(grid):
    
    for col in range(4):
        for row in range(4):
            if grid[col][row] >= 32:
                return True
            else:
                return False
                
            
def copy_grid(grid):
    
    grid2=copy.deepcopy(grid)
    
    return grid2
    
    
def grid_equal(grid1, grid2):
    
    if grid1 == grid2:
        return True
    
    else:
        return False    