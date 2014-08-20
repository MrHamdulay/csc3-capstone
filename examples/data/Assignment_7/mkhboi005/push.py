def push_up(grid):
  for row in range(3):
    for col in range(4):
        if grid[row][col] == grid[row+1][col]:
              grid[row][col] = grid[row+1][col]*2
              grid[row+1][col] = 0
              
              while grid[row][col]==0:
                grid[row][col]= grid[row+1][col]
              

def push_down(grid):
        for col in range(4):
            for row in range(3):
                if grid[row][col] == grid[row+1][col]:
                    grid[row+1][col] = grid[row][col]*2
                    grid[row][col] = 0
                    

def push_left (grid):
        for row in range(4):
            for col in range(3):
                if grid[row][col] == grid[row][col+1]:
                    grid[row][col] = grid[row][col]*2
                    grid[row][col+1] = 0
                    

def push_right (grid):
        for row in range(4):
            for col in range(3):
                if grid[row][col] == grid[row][col+1]:
                    grid[row][col+1] = grid[row][col]*2
                    grid[row][col] = 0
                  