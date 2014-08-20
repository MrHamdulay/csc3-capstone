def push_up(grid):
    for x in range(4):
        for y in range(3):
            zero_count = 0
            while grid[y][x] == 0 and zero_count < 4:
                for i in range(y,3):
                    grid[i][x] = grid[i+1][x]
                grid[3][x] = 0
                zero_count+=1
        for y in range(3):
            if grid[y][x] == grid[y+1][x]:
                grid[y][x] *= 2
                for i in range(y+1,3):
                    grid[i][x] = grid[i+1][x]
                grid[3][x] = 0

def push_down(grid):
    for x in range(4):
        for y in range(3,0,-1):
            zero_count = 0
            while grid[y][x] == 0 and zero_count < 4:
                for i in range(y,0,-1):
                    grid[i][x] = grid[i-1][x]
                grid[0][x] = 0
                zero_count+=1
        for y in range(3,0,-1):
            if grid[y][x] == grid[y-1][x]:
                grid[y][x] *= 2
                for i in range(y-1,0,-1):
                    grid[i][x] = grid[i-1][x]
                grid[0][x] = 0

def push_left(grid):
    for y in range(4):
        for x in range(3):
            zero_count = 0
            while grid[y][x] == 0and zero_count < 4:
                for i in range(x,3):
                    grid[y][i] = grid[y][i+1]
                grid[y][3] = 0
                zero_count+=1
        for x in range(3):
            if grid[y][x] == grid[y][x+1]:
                grid[y][x] *= 2
                for i in range(x+1,3):
                    grid[y][i] = grid[y][i+1]
                grid[y][3] = 0

def push_right(grid):
    for y in range(4):
        for x in range(3,0,-1):
            zero_count = 0
            while grid[y][x] == 0 and zero_count < 4:
                for i in range(x,0,-1):
                    grid[y][i] = grid[y][i-1]
                grid[y][0] = 0
                zero_count+=1
        for x in range(3,0,-1):
            if grid[y][x] == grid[y][x-1]:
                grid[y][x] *= 2
                for i in range(x-1,0,-1):
                    grid[y][i] = grid[y][i-1]
                grid[y][0] = 0

##def push_up(grid):
##    for x in range(4):
##        zero_count = 0
##        y = 0
##        while y < 3 and zero_count < 4:
##            if grid[y][x] == 0:
##                for i in range(y,3):
##                    grid[i][x] = grid[i+1][x]
##                grid[3][x] = 0
##                zero_count+=1
##                continue
##            
##            if grid[y][x] == grid[y+1][x]:
##                grid[y][x] *= 2
##                y+=1
##                for i in range(y,3):
##                    grid[i][x] = grid[i+1][x]
##                grid[3][x] = 0
##                continue
##            y+=1
##
##
##
##def push_down(grid):
##    for x in range(4):
##        y = 3
##        zero_count = 0
##        while y > 0 and zero_count < 4:
##            if grid[y][x] == 0:
##                for i in range(y,-1,-1):
##                    grid[i][x] = grid[i-1][x]
##                grid[0][x] = 0
##                zero_count+=1
##                continue
##            
##            if grid[y][x] == grid[y-1][x]:
##                grid[y][x] *= 2
##                y-=1
##                for i in range(y,-1,-1):
##                    grid[i][x] = grid[i-1][x]
##                grid[0][x] = 0
##                continue
##            y-=1

##def push_left(grid):
##    for y in range(4):
##        x = 0
##        zero_count = 0
##        while x < 3 and zero_count < 4:
##            if grid[y][x] == 0:
##                for i in range(x,3):
##                    grid[y][i] = grid[y][i+1]
##                grid[y][3] = 0
##                zero_count+=1
##                continue
##            
##            if grid[y][x] == grid[y][x+1]:
##                grid[y][x] *= 2
##                x+=1
##                for i in range(x,3):
##                    grid[y][i] = grid[y][i+1]
##                grid[x][3] = 0
##                continue
##            x+=1
##
##def push_right(grid):
##    for y in range(4):
##        x = 3
##        zero_count = 0
##        while x > 0 and zero_count < 4:
##            if grid[y][x] == 0:
##                for i in range(x,-1,-1):
##                    grid[y][i] = grid[y][i-1]
##                grid[y][0] = 0
##                zero_count+=1
##                continue
##            
##            if grid[y][x] == grid[y][x-1]:
##                grid[y][x] *= 2
##                x-=1
##                for i in range(x,-1,-1):
##                    grid[y][i] = grid[y][i-1]
##                grid[y][0] = 0
##                continue
##            x-=1
##    
