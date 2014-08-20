''' Utility program for 2048
Author: Raees Eland
Date: 30 April 2014'''

import copy

'''creates a 2D array'''
def create_grid(grid):
    height = 4
    for i in range (height):
        grid.append ([0] * 4)
    return grid
   
def print_grid (grid):
    0==''
    s='{0:<5}'
    p='{0:<5}'
    print('+--------------------+')
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                if j==0:
                    print('|',s.format(''),sep='',end='') # prints and empty space 
                elif j==3:
                    print(p.format(''),'|',sep='',end='')
                else:
                    print(s.format(''),end='') 
               
            else:
                if j==0:
                    print('|',s.format(grid[i][j]),sep='',end='')
                elif j==3:
                    print(p.format(grid[i][j]),'|',sep='',end='')
                else:
                    print(s.format(grid[i][j]),end='')
        print()
    print('+--------------------+') 

'''checks if you lost the game'''    
def check_lost (grid):
    for i in range(4):
            for j in range(4):
                if grid[i][j]==0: # checks if there are empty gaps in the list
                    return False
                
    for i in range(3):
        for j in range(3):
            if grid[i][j]==grid[i+1][j] or  grid[i][j]==grid[i+1][j]: 
                return False
    return True        

'''checks if you won the game'''
def check_won (grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]>=32:
                return True
    return False
        
'''copies a list'''        
def copy_grid (grid):
    grid1=copy.deepcopy(grid)
    return grid1

'''ckecks if two grids are equal'''
def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False
    
    


    
