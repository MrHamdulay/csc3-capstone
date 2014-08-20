"""Promise Mashinini
2014/05/02

writing functions"""

from copy import deepcopy#this copies the list but has a different memory locatoion
def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])
        
def print_grid (grid):
    print('+--------------------+')
    """ print out a grid of strings/characters"""
    for row in range (4):
        
        print('|',end='')
        for col in range (4):
            if grid[row][col]==0:
                print ("{0:<5}".format(' '),end="")
            else:
                print ("{0:<5}".format(grid[row][col]),end="")
        
        print ('|',end='')    
        print()
    print('+--------------------+')  


def check_lost(grid):
    
    for i in range(4):
        for j in range(4):
            
            
            if grid[i][j]==0:
                return False
            if i!=3 and grid[i][j]==grid[i+1][j] :
                return False
            if j != 0 and grid[i][j]==grid[i][j-1] :
                return False
            if j != 3 and grid[i][j]==grid[i][j+1] :
                return False
            if i!=0 and grid[i][j]==grid[i-1][j]  :
                return False            
    else:
        return True
       
           
            
def check_won(grid):
    for i in grid:
        for j in i:
            if j>=32:
                return True 
    else:
        return False
        
def copy_grid(grid):#using the deepcopy to copy the list
    grid3=[]
    create_grid(grid3)
    grid3=deepcopy(grid)
    return grid3
    
    
    
    
    
def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True 
    else:
        return False
    

    
        
            
    
         
             
    
    
    
