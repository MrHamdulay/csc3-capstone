import util

def add_block (grid):
    """add a random number to a random location on the grid"""
    # set distributon of number possibilities
    options = [2,2,2,2,2,4]
    # get random number
    chosen = options[random.randint(0,len(options)-1)]
    found = False
    while (not found):
        # get random location
        x = random.randint (0, 3)
        y = random.randint (0, 3)
        # check and insert number
        if (grid[x][y] == 0):
            grid[x][y] = chosen
            found = True


#grid = [[0,0,0,0],[0,0,0,0],[0,0,2,0],[2,0,0,0]]
grid = [[3,3,4,5],[3,5,5,2],[0,5,2,2],[2,0,2,0]]
util.print_grid(grid)

#merge grid values upwards
def push_right (grid):
    
    #merging them
    for col in range(4):
        for row in range(3,-1,-1):
            if grid[col][row] == grid[col][row-1]:
                #merges them
                grid[col][row] = grid[col][row] + grid[col][row-1]
                grid[col][row-1] = 0
    #shifting       
    util.print_grid(grid)            
    count = 1
    while count < 4:
        for col in range(4):
            for row in range(3,0,-1):
                if grid[col][row] == 0:
                    if grid[col][row-1] != 0:
                        grid[col][row] = grid[col][row-1]
                        grid[col][row-1] = 0
        count = count + 1 
        
    #merging again
    for col in range(4):
        for row in range(3,0,-1):
            if grid[col][row] == grid[col][row-1]:
                #merges them
                grid[col][row] = grid[col][row] + grid[col][row-1]
                grid[col][row-1] = 0
    
    util.print_grid(grid)
    return grid
                
push_right(grid)
                
                

                
            