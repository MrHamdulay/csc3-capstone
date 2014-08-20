''' Yongama Giwu
30 april 2014
Program to manipulate a grid in arrays'''

import copy
def create_grid(grid): #Create a 4 column and 4 row grid 
    height = 4
    for i in range (height):
        grid.append ([0] * 4)



def print_grid(grid):
    #print out grid 
    grid=copy_grid(grid)
    height=len(grid)
    string="{0:<5}"
    for i in range(height):
        for j in range(height):
            grid[i][j]=string.format(grid[i][j])

    #print out grid
    print('+','-'*(height*5),'+',sep='')
    for row in range (height):
        print('|',end='')
        for col in range (height):
            if eval(grid[row][col])!=0:
                print (grid[row][col],end='')
            else:
                print('     ',end='')

        print('|')
    print('+','-'*(height*5),'+',sep='')



def check_lost(grid):
    #return True if there are no zero values and no adjacent values that are equal; else return false
    prime = True
    for row in range(len(grid)):
        for column in range(len(grid)):
            if grid[row][column] == 0:
                prime = False
            if row< 3:
                if  grid[row][column] == grid[row+1][column]:
                    prime = False
            if row>0:
                if grid[row][column]==grid[row-1][column]:
                    prime = False
            if column < 3:
                if grid[row][column]==grid[row][column+1]:
                    prime = False
            if column >0:
                if grid[row][column]==grid[row][column-1]:
                    prime = False
    return prime




def check_won (grid):
    #return True if a value>=32 is found in the grid; else return False
    prime= False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]>=32:
                prime = True
    return prime

def copy_grid (grid):
    #return a copy of the grid
    grid_copy=[]
    for item in grid:
        grid_copy.append(list(item))
    return grid_copy

def grid_equal (grid1, grid2):
    #check if 2 grids are equal-return boolean 
    prime= True
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid1[i][j] != grid2[i][j]:
                prime = False
    return prime








