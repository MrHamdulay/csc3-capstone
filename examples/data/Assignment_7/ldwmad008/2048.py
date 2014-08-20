''' 2048 pushes
Frans Ledwaba
02 May 2014'''

height = 4

def push_up(grid):
    for x in range(height):
        for y in range(height):
            if grid[x][y] == grid[x][y]:
                return grid[x][y]
        
def push_down(grid):
    for x in range(height):
        for y in range(height):
            if grid[x][y] == grid[x][y]:
                return grid[x][y] + grid[x][y]   

def push_left(grid):
    for x in range(height):
        for y in range(height):
            if grid[x][y] == grid[x-1][y]:
                return grid[x][y] + grid[x][y]   

def push_right(grid):
    for x in range(height):
        for y in range(height):
            if grid[x][y] == grid[x+1][y]:
                return grid[x][y] + grid[x][y]  