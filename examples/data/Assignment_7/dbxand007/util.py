"""Cherise Dube
29 April 2014
Module to manipulate 2-D arrays of size 4x4"""


def create_grid(grid):
    """Create a 4x4 grid"""
    import random
    sub_grid=[]
    for i in range (5):
        grid.append(sub_grid)
        sub_grid=[]
        for j in range(4):
            sub_grid.append(random.randint(0,2048))
    grid.remove([])
            
    return grid
        

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","{:-^20}".format(""),"+",sep="")
    for i in range (4):
        for j in (grid[i]):
            if j==0:
                if grid[i].index(j)==0:
                    print("|","{0:<5}".format(""),end="")
                elif grid[i].index(j)==3:
                    print("{0:<5}".format(""),"|",sep="")
                    
                else:
                    print("{0:<5}".format(""),end="") 
                    
                
            else:
                if grid[i].index(j)==0:
                    print("|","{0:<5}".format(j),sep="",end="")
                    
                elif grid[i].index(j)==3:
                    print("{0:<5}".format(j),"|",sep="")
                    
                else:
                    print("{0:<5}".format(j),end="")
            
    print("+","{:-^20}".format(""),"+",sep="") 
                    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    count_zeros=0
    for i in range(4):          #Checks to see if there are 0 values
        for j in grid[i]:
            if j==0:
                count_zeros+=1
            else:
                continue
   
    count_equal=0  
    #Checks to see if there are adjacent values equal
    for i in range(3):
        for j in range (3):
            if grid[i][j]==grid[i][j+1] or grid[i][j]==grid[i+1][j]:
                count_equal+=1
            else:
                continue
      
    if count_equal==0 and count_zeros==0:
        return True 
    else:
        return False
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    count_large=0 #Counts numbers greater than 32
    for i in range(4):
        for j in grid[i]:
            if j>=32:
                count_large+=1
            else:
                continue
    if count_large>0:
        return True
    else:
        return False
                
        
            
             
def copy_grid(grid):
    """return a copy of the grid"""
    copy_grid=[]
    for i in range(4):
        for j in grid[i]:
            copy_grid.append(i)
    return copy_grid
    
def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False
    
                     
        