#Assignment 7
#Question 3
#Rabia Parker
#PRKRAB004
#Due Date: 02/04/14

def push_up (grid):
    """merge grid values upwards"""
    for grid_column in range(4): #create the columns
        for grid_row in range(3):
            count=1
            while count<(4-grid_row) and grid[grid_row][grid_column]==0: 
                grid[grid_row][grid_column]=grid[grid_row+count][grid_column]
                grid[grid_row+count][grid_column]=0
                count+=1
                
    for grid_column in range(4): #create the rows
        for grid_row in range(3):
            if grid[grid_row][grid_column] == grid[grid_row+1][grid_column]:
                grid[grid_row][grid_column]=2*grid[grid_row][grid_column]
                grid[grid_row+1][grid_column]=0
            
    for grid_column in range(4):
        for grid_row in range(3):
            count=1
            while count<(4-grid_row) and grid[grid_row][grid_column] == 0:
                grid[grid_row][grid_column]=grid[grid_row+count][grid_column]
                grid[grid_row+count][grid_column]=0
                count+=1
            

def push_down (grid):
    """merge grid values downwards"""
    for grid_column in range(4):
        for grid_row in range(3,0,-1):
            count=1
            while count<(grid_row+1) and grid[grid_row][grid_column]==0:
                grid[grid_row][grid_column]=grid[grid_row - count][grid_column]
                grid[grid_row - count][grid_column]=0
                count+=1
                
    for grid_column in range(4):
        for grid_row in range(3,0,-1):
            if grid[grid_row][grid_column]==grid[grid_row-1][grid_column]:
                grid[grid_row][grid_column]=2*grid[grid_row][grid_column]
                grid[grid_row-1][grid_column]=0
                
    for grid_column in range(4):
        for grid_row in range(3,0,-1):
            count=1
            while count<(grid_row+1) and grid[grid_row][grid_column]==0:
                grid[grid_row][grid_column]=grid[grid_row-count][grid_column]
                grid[grid_row-count][grid_column]=0
                count+=1
                
                
def push_left (grid):
    """merge grid values left"""
    for grid_row in range(4):
        for grid_column in range(3):
            count=1
            while count<(4-grid_column) and grid[grid_row][grid_column]==0:
                grid[grid_row][grid_column]=grid[grid_row][grid_column+count]
                grid[grid_row][grid_column+count]=0
                count+=1
                
    for grid_row in range(4):
        for grid_column in range(3):
            if grid[grid_row][grid_column]==grid[grid_row][grid_column+1]:
                grid[grid_row][grid_column]=2*grid[grid_row][grid_column]
                grid[grid_row][grid_column+1]=0
                
    for grid_row in range(4):
        for grid_column in range(3):
            count=1
            while count<(4-grid_column) and grid[grid_row][grid_column]==0:
                grid[grid_row][grid_column]=grid[grid_row][grid_column+count]
                grid[grid_row][grid_column+count]=0
                count+=1
                

def push_right (grid):
    """merge grid values right""" 
    for grid_row in range(4):
        for grid_column in range(3,0,-1):
            count=1
            while count<(grid_column+1) and grid[grid_row][grid_column]==0:
                grid[grid_row][grid_column]=grid[grid_row][grid_column-count]
                grid[grid_row][grid_column-count]=0
                count+=1
                
    for grid_row in range(4):
        for grid_column in range(3,0,-1):
            if grid[grid_row][grid_column]==grid[grid_row][grid_column-1]:
                grid[grid_row][grid_column]=2*grid[grid_row][grid_column]
                grid[grid_row][grid_column-1]=0
                
    for grid_row in range(4):
        for grid_column in range(3,0,-1):
            count=1
            while count<(grid_column+1) and grid[grid_row][grid_column]==0:
                grid[grid_row][grid_column]=grid[grid_row][grid_column-count]
                grid[grid_row][grid_column-count]=0
                count+=1
                
    #end of program
