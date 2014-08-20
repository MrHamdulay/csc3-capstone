"""Assignment 7, question 2, util.py
by Jonathan Ovadia 
1 May 2014"""
import copy
def main():
    print(__name__)
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in grid:
        zero = i[0]
        one= i[1]
        two= i[2]
        three= i[3]
        if i[0]==0:zero =" "
        if i[1]==0:one =" "
        if i[2]==0:two =" "
        if i[3]==0:three =" "
        line ="|" +str(zero) + " "*(5-len(str(zero)))+str(one) + " "*(5-len(str(one)))+str(two) + " "*(5-len(str(two)))+str(three) + " "*(5-len(str(three))) + "|"
        print(line)
    print("+--------------------+")
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    no_zeros = True
    for i in grid:
        for j in i :
            if j == 0:
                no_zeros = False
    no_equal_adjacent_valuse = True
    for y in range(len(grid)):
        for x in range(y):
            if y ==0:
                if grid[y][x] ==grid[y+1][x]:
                    no_equal_adjacent_valuse = False
            if x ==0:
                if grid[y][x] ==grid[y][x+1]:
                    no_equal_adjacent_valuse = False
            if y ==3:
                if grid[y][x] ==grid[y-1][x]:
                    no_equal_adjacent_valuse = False
            if x ==3:
                if grid[y][x] ==grid[y][x-1]:
                    no_equal_adjacent_valuse = False
            if y ==1 and x ==1:
                if grid[y][x] ==grid[y-1][x] or grid[y][x] ==grid[y+1][x] or grid[y][x] ==grid[y][x-1]or grid[y][x] ==grid[y][x+1]:
                    no_equal_adjacent_valuse = False
            if y ==1 and x ==2:
                if grid[y][x] ==grid[y-1][x] or grid[y][x] ==grid[y+1][x] or grid[y][x] ==grid[y][x-1]or grid[y][x] ==grid[y][x+1]:
                    no_equal_adjacent_valuse = False
            if y ==2 and x ==1:
                if grid[y][x] ==grid[y-1][x] or grid[y][x] ==grid[y+1][x] or grid[y][x] ==grid[y][x-1]or grid[y][x] ==grid[y][x+1]:
                    no_equal_adjacent_valuse = False
            if y ==2 and x ==2:
                if grid[y][x] ==grid[y-1][x] or grid[y][x] ==grid[y+1][x] or grid[y][x] ==grid[y][x-1]or grid[y][x] ==grid[y][x+1]:
                    no_equal_adjacent_valuse = False
    if no_zeros and no_equal_adjacent_valuse:
        return True
    else:
        return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
            for j in i :
                j = str(j)
                if j.isdigit():
                    j = int(j)
                else:
                    j = 0
                if j >= 32:
                    return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    new_list = copy.deepcopy(grid)
    return new_list

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False

if __name__=="__main__": main()