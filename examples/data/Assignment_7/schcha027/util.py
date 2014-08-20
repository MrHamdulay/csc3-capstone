""" Charles Schleich-SCHCHA027
2014-May-01
"""
#Util program to test the deviously difficult 2048 program

import copy

def create_grid(grid):
#creates a 4x4 grid of 0's
    for i in range(4):
        grid.append([0,0,0,0])
    return grid
    
def print_grid (grid):
#print out a 4x4 grid in 5-width columns within a box
    print("+","-"*20,"+",sep="")
    for i in range(0,4):
        print("|",end="",sep="")
        for j in range(0,4):
            if grid[i][j]==0:
                print(" "*(5),sep="",end="")
            else:
                print(grid[i][j]," "*(5-len(str(grid[i][j]))),sep="",end="")
        print("|",sep="",end="")        
        print()
        
    print("+","-"*20,"+",sep="")    
        
def check_lost (grid):
#checks if the grid is full with no remaining possible moves
    
    trueOrFalse = True
    stoprun = False
    for i in range(0,4):
        for j in range(0,4):
            if grid[i][j] == 0:
                trueOrFalse = False
                stoprun =True
                break
        else:
            continue  # executed if the loop ended normally (no break)
        break   
    
    if stoprun == False:
        for i in range(0,4):
            for j in range(0,4):
                
                if j==3 and i==3:
                    1==1
                elif i==3:
                    if grid[i][j]== grid[i][j+1]:
                        trueOrFalse = False
                        break
                elif j==3:
                    if grid[i+1][j]== grid[i][j]:
                        trueOrFalse = False
                        break
                else:
                    if grid[i][j]== grid[i][j+1] or grid[i+1][j]== grid[i][j]:
                        trueOrFalse = False
                        break
    
    return trueOrFalse   

def check_won (grid):
#checks to see if there is a single block equal to or over 32
# returns true and alerts the player that he/she has won
    
    trueOrFalse = False
    for i in range(0,4):
        for j in range(0,4):
            if grid[i][j]>=32:
                trueOrFalse = True
                break
        else:
            continue
        break    
    return trueOrFalse

def copy_grid (grid):
#Makes a Copy of the grid and returns it
    
    newGrid = copy.deepcopy(grid)
    return newGrid 

def grid_equal (grid1, grid2):
#checks if two grids are equal
    for i in range(4):
        for j in range(4):
            if grid1[i][j] !=grid2[i][j]:
                return False
    return True
                
            