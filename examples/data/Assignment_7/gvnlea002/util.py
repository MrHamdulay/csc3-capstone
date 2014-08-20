""" different functions for the 2048 game
leandra govender
30 april 2014"""
import copy

def create_grid(grid):                                                 
        for i in range(4):
                grid.append ([0,0,0,0])                            #add 4 4x4 grid to the list
                                                       

def print_grid(grid):
        print("+--------------------+")                             #print the first line
        for i in range(len(grid)):
                print("|",end="")                                    # at the beginning of each line print "|"
                for j in range(len(grid)):
                        if grid[i][j]==0:
                                print('{0:<5}'.format(""),end="")    #if the position is empty do not print anything
                        else:
                                print('{0:<5}'.format(grid[i][j]),end="")   #if position on a grid is not empty print thr number  that is in that position
                print("|")                                            #at the end each row in the grid print "|"    
        print("+--------------------+")                               #print the last line
                            
def check_lost(grid):
        for row in range(4):
                for col in range(4):
                        if grid[row][col]==0:
                                return False
                        if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
                                return False 
                        if grid[0][3]==grid[0][2] or grid[0][3]==grid[1][3]:
                                return False            
                        if grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
                                return False
                        if grid[3][3]==grid[2][3] or grid[3][3]==grid[3][2]:
                                return False 
                        if grid[0][1]==grid[0][2] or grid[0][1]==grid[1][1]:
                                return False 
                        if grid[0][2]==grid[1][2]:
                                return False    
                        if grid[1][1]==grid[2][1] or grid[1][1]==grid[1][2] or grid[1][1]==grid[1][0]:
                                return False
                        if grid[2][1]==grid[2][0] or grid[2][1]==grid[2][2] or grid[2][1]==grid[3][1]:
                                return False 
                        if grid[1][0]==grid[2][0]:
                                return False
                        if grid[1][2]==grid[1][3] or grid[1][2]==grid[2][2]:
                                return False
                        if grid[2][2]==grid[2][3] or grid[2][2]==grid[3][2]:
                                return False
                        if grid[3][1]==grid[3][2]:
                                return False
                        else:
                                return True
       
    
    
def check_won(grid):
        won= False
        for i in range(4):
                for j in range (4):
                        if grid[i][j] >= 32:
                                won = True
        return won
                        
    
    
    
    
def copy_grid(grid):
        return copy.deepcopy(grid)             # use deepcopy function returns an original copy
    
    
def grid_equal(grid1,grid2):
        if grid1== grid2:
                return True
        else:
                return False