__author__ = 'JNSJOH014'
"""Utility functions to manipulate 2-dimensional arrays of size 4x4
27/04/2014"""

import copy
#create empty grid of 4x4
def create_grid(grid):
    #grid = []
    row = []
    for i in range (4):
        for j in range (4):
            row.append(0)
        grid.append(row)
        row = []

def print_grid(grid):
    form_string = "{0:<5}"#Columns of width=5, left-aligned, no fill character
    print("+",(5*4)*"-","+",sep="")
    for row in range(0,4):
        print("|",end="")
        for col in range(0,4):
            if grid[row][col]!=0:
                print(form_string.format(grid[row][col]),end="")
            else:
                print(form_string.format(" "),end="")
        print("|")
    print("+",(5*4)*"-","+",sep="")

def check_lost(grid):
    #Check if any block is empty
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
    #Check if any adjacent blocks are equal in value
    #Algorithm 1: Check horizontally
    row = 0
    col = 0
    while row<4:
        while col<3:
            if grid[row][col]== grid[row][col+1]:
               return False
            col+=1
        col=0
        row+=1
    #Algorithm 2: Check vertically
    row=0
    while col<4:
        while row<3:
            if grid[row][col]== grid[row+1][col]:
               return False
            row+=1
        row=0
        col+=1
    return True

def check_won (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True
    return False

def copy_grid(grid):
    temp = copy.deepcopy(grid)
    return temp

def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    return False
