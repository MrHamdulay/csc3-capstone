# Merges  values in a grid for 2048 game
# Conor O'Sullivan
# 28/04/2014
    
#merge grid values upwards
def push_up (grid):
    space_up(grid)
    for row in range(3):
        for col in range(4):
            if grid[row][col] == grid[row+1][col]:
                grid[row][col] += grid[row+1][col]
                grid[row+1][col] = 0
    space_up(grid)
    return grid
    
#eliminates spaces when grid merged up   
def space_up(grid):
    for x in range(3):
        for col in range(4):
            for row in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row+1][col]
                    grid[row+1][col] = 0
    return grid
        
#merge grid values downwards
def push_down (grid):
    space_down(grid)
    for row in range(3):
        for col in range(4):
            if grid[3-row][col] == grid[2-row][col]:
                grid[3-row][col] += grid[2-row][col]
                grid[2-row][col] = 0    
    space_down(grid)
    return grid

#eliminates spaces when grid merged down
def space_down(grid):
    for x in range(3):
        for row in range(3):
            for col in range(4):
                if grid[3-row][col] == 0:
                    grid[3-row][col] = grid[2-row][col]
                    grid[2-row][col] = 0
    return grid

    
#merge grid values left
def push_left (grid):
    grid = space_left(grid)
    for row in range(4):
            for col in range(3):
                if grid[row][col] == grid[row][col+1]:
                    grid[row][col] += grid[row][col+1]
                    grid[row][col+1] = 0
    grid = space_left(grid)
    return grid
    
#eliminates spaces when grid merged left
def space_left(grid):
    for x in range(3):
        for row in range(4):
            for col in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col+1]
                    grid[row][col+1] = 0
    return grid
    
#merge grid values right
def push_right (grid):
    space_right(grid)
    for row in range(4):
        for col in range(3):
            if grid[row][3-col] == grid[row][2-col]:
                grid[row][3-col] += grid[row][2-col]
                grid[row][2-col] = 0
    space_right(grid)
    return grid    
    
#eliminates spaces when grid merged right
def space_right(grid):
    for x in range(3):
        for row in range(4):
            for col in range(3):
                if grid[row][3-col] == 0:
                    grid[row][3-col] = grid[row][2-col]
                    grid[row][2-col] = 0
    return grid
    
    
    
    
#Insures functions will not run when module is imported    
if __name__ == '__main__':
    push_left()
    push_down()
    push_up()
    push_right()