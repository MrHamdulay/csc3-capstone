'''
Prashanth Sridharan
SRDPRA001
Assignment 07
Question 3
'''
#p is the variable name for row
#q is the variable name for column
import copy 

def create_grid(grid): 
    for p in range (4): #loops the row in a given range
        grid.append ([0] * 4) #creates the row of the grid
        
def print_grid (grid): 
    print('+--------------------+') #printing the header
    for p in grid:
        print('|',end='')
        for q in p: 
            q=str(q)
            if q=='0':
                print(' '.ljust(5),end='') #formats to the 5-character width
            else:
                print(q.ljust(5),end='')
        print('|')        
        
    print('+--------------------+') #printing the footer

def check_lost (grid): 
    for p in range(len(grid)):
        for q in range(len(grid) - 1):
            if grid[p][q]==0: 
                return False 
            elif grid[p][q]==grid[p][q+1]: 
                return False
            
    for p in range(len(grid) - 1): 
        for q in range(len(grid)):    
            if grid[p][q]==grid[p+1][q]:
                return False #Indicates that the game is over, then return True
    else:
        return True
    
def check_won (grid): 
    for p in range(len(grid)):
            for q in range(len(grid[p])):
                if grid[p][q]>=32:
                    return True
    else:
        return False

def copy_grid (grid): 
    CopyGrid=copy.deepcopy(grid) #deepcopying the original grid
    return CopyGrid

def grid_equal (grid1, grid2): #function that checks if grids are equal
    for p in range(len(grid1)):
            for q in range(len(grid1[p])):
                if grid1[p][q]==grid2[p][q]:
                    continue
                else:
                    return False
    return True