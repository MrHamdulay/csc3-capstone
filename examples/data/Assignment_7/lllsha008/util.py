#Shaylan Lalloo
#LLLSHA008
#Does basic functions of 2048


from copy import *

neigh = [[0, 1], [1, 0], [-1, 0], [0, -1]]
def coval(x, y):
    return 0 <= x < 4 and 0 <= y < 4
#valid coordinate checker

def create_grid(grid):
    for i in range(4):
        x = [0,] * 4
        grid.append(x)
    #makes a new grid
        
def print_grid(grid):
    print('+' + '-' * 20 + '+')
    #output first line
    for i in range(4):
        for j in range(22):
            if j == 0 or j == 21:
                #if at end, output border
                print('|', end = '')
            elif j % 5 == 1:
                #if it's a starting point, output the number unless a 0
                if grid[i][(j - 1)//5] == 0:
                    print(' ', end = '')
                else:
                    print(grid[i][(j - 1)//5], end = '')
            else:
                #if characters aren't being used by numbers, output space
                if j % 5 == 0 or j % 5 > len(str(grid[i][(j - 1)//5])):
                    print(' ', end = '')
        print()
        #output next line
    print('+' + '-' * 20 + '+')
    #output last line

def check_lost(grid):
    for i in grid:
        for j in i:
            if j == 0:
                return False
            #if something is 0, then there is a not loss
    for i in range(4):
        for j in range(4):
            for k in neigh:
                tmpx = i + k[0]
                tmpy = j + k[1]
                #checks neighbouring pieces and if there is something equal, it causes a definite not loss
                if coval(tmpx, tmpy) == False:
                    continue
                if grid[tmpx][tmpy] == grid[i][j]:
                    return False
    #if false hasn't happened earlier, then it's true and the guy lost
    return True

def check_won(grid):
    for i in grid:
        for j in i:
            if j >= 32:
                return True
            #checks if they won by looking for a value greater than 32
    return False

def copy_grid(grid):
    #returns a copy of grid
    return deepcopy(grid)

def grid_equal(grid1, grid2):
    #checks if they are equal
    return grid1 == grid2
