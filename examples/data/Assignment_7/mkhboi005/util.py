"""Tumi Mkhawana
28 April 2014
Assignment 7 Question 2"""

def create_grid(grid) : 
    for i in range(4):
        grid.append([" "]*4)

def print_grid(grid):
    print("+"+"-"*20+"+")
    for row in range (4):
        print("|",end="")
        for col in range(4):
            if col==3:
                if grid[row][col]==0:
                    grid[row][col]=" "
                print("{0:<5}".format(grid[row][col])+"|")
            else:
                if grid[row][col]==0:
                    grid[row][col]= " "
                print("{0:<5}".format(grid[row][col]),end="")
    
    print("+"+"-"*20+"+")

def check_lost (grid):
    lost = True
    for row in range(4):
        for col in range(4):
            if (grid[row][col]==0):
                lost= False
    for row in range(3):
        for col in range(3):
            if grid[row][col] != grid[row+1][col] or grid[row][col] != grid[row][col+1]:
                lost = False
    return lost 

def check_won(grid):
    won = False
    for row in range(4):
        for col in range(4):
            if grid[row][col] >=32:
                won= True
    return won

def copy_grid (grid):
    newgrid=[]
    for i in range(4):
        newgrid.append([" "]*4)
    for row in range(4):
        for col in range(4):
            newgrid[row][col]=grid[row][col]
    return newgrid

def grid_equal (grid1, grid2):
    find = True
    for row in range(4):
        for col in range(4):
            if grid1[row][col] != grid2[row][col]:
                find = False
    return find