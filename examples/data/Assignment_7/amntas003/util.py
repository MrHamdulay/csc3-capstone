#AMNTAS003  #Tashfia Amin   #Due Date: 2 May 2014
#Question 2: Assignment 7   #Create a 2d array of size 4x4

#function to create the grid
def create_grid(grid):
    height = 4
    for i in range (height):
        grid.append (["0"] * 4)           

#Create variables to use withint print_grid module
y = "+--------------------+"
#function to print the grid in 5-width columns within a box
def print_grid(grid):
    print(y)
    for i in grid:
        print('|',end="")
        for x in i:
            if x == 0:
                x = ""
            print("{0:<5}".format(x),end="")
        print('|')
    print(y)

#function to check  if player has lost
def check_lost(grid):
    check = 0
    height = 4
    for i in grid:
        for x in i:
            if x == ' ':
                return false
    for i in range(len(grid)):
        for x in range (height):
            right = x+1
            if 0 <= right < 4:
                if grid[i][x] == grid[i][right]:
                    return False
            left = x-1
            if 0 <= left <= 4:
                if grid[i][x] == grid[i][left]:
                    return False
            up = i-1
            if 0 <= up < 4:
                if grid[i][x] == grid[up][x]:
                    return False
            down = i+1
            if 0 <= down < 4:
                    if grid[i][x] == grid[down][x]:
                        return False
    return True     

#function to check if player has won by getting more than 32
def check_won(grid):
    check = 0
    for i in grid:
        for x in i:
            if x >= 32:
                check +=1
    if check == 0:
        return False
    elif check != 0:
        return True    

#function to copy the grid
def copy_grid(grid):
    new_grid = []
    height = 4
    create_grid(new_grid)
    for i in range (height):
        for x in range (height):
            new_grid[i][x] = grid[i][x]
    return new_grid    

#function to check if two grids are equal and return True or return False if not the same
def grid_equal(grid1, grid2):
    if grid1 == grid2:
            return True
    else:
        return False
    
if __name__ == '__main__':
    grid = []
    create_grid(grid)
    print_grid(grid)