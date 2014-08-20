#Soham Singh
#SNGSOH004
#Assignment 7
#Question 3 - push.py

import copy 

def create_grid(grid): 
    
    for p in range (0,4): #to iterate through the rows
        
        grid.append ([0]*4) #creating each row
        
def print_grid (grid):
    
    print('+--------------------+') #printing header
    for p in grid:
        print('|',end='')
        for q in p: 
            
            q=str(q)
            
            if q=='0':
                print(' '.ljust(5),end='') #formats the output to a string of 5 character width
            else:
                print(q.ljust(5),end='')
        print('|')        
        
    print('+--------------------+') #printing footer

def check_lost (grid): 
    
    for p in range(len(grid)):
        
        for q in range(len(grid)-1):
            
            if grid[p][q]==0: #if there are still empty spaces
                
                return False 
            
            elif grid[p][q]==grid[p][q+1]: #if there are adjacent, equal values
                
                return False
            
    for p in range(len(grid) - 1): 
        
        for q in range(len(grid)):
            
            if grid[p][q]==grid[p+1][q]:
                
                return False 
            
    else:
        
        return True
    
def check_won (grid): 
    
    for p in range(len(grid)):
        
            for q in range(len(grid[p])):
                
                if grid[p][q]>=32:
                    
                    return True #they have won if there is a value of 32 or greater
                
    else:
        
        return False

def copy_grid (grid): 
    
    newGrid=copy.deepcopy(grid) #deepcopying the original grid (as you cannot simply say newGrid = grid)
    
    return newGrid

def grid_equal (grid1, grid2): 
    
    for p in range(len(grid1)):
        
        
            for q in range(len(grid1[p])):
                
                if grid1[p][q]==grid2[p][q]:
                    
                    continue
                
                else:
                    return False #the first occurence of a difference will return false
    return True