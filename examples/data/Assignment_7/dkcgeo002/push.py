__author__ = 'George de Kock'
"""Set of merging functions that merge adjacent equal values and eliminate gaps
    2014-04-27 """


def push_up(grid):
    for b in range(4):
        for a in range(3):
            x = 1
            while grid[a][b] == 0:
                i = 1
                while a+i < 4:
                    grid[a+i-1][b] = grid[a+i][b]
                    grid[a+i][b] = 0
                    i += 1
                x += 1
                if x > 4:
                    break

    for b in range(4):
        for a in range(3):
            if grid[a][b] == grid[a+1][b]:
                grid[a][b] *= 2
                grid[a+1][b] = 0

    for b in range(4):
        for a in range(3):
            x = 1
            while grid[a][b] == 0:
                i = 1
                while a+i < 4:
                    grid[a+i-1][b] = grid[a+i][b]
                    grid[a+i][b] = 0
                    i += 1
                x += 1
                if x > 4:
                    break


def push_down(grid):
    for b in range(4):
        for a in range(3,0,-1):
            x = 1
            while grid[a][b] == 0:
                i = 1
                while a-i >=0:
                    grid[a-i+1][b]= grid[a-i][b]
                    grid[a-i][b] = 0
                    i += 1
                x += 1
                if x > 4:
                    break

    for b in range(4):
        for a in range(3,0,-1):
            if grid[a][b] == grid[a-1][b]:
                grid[a][b] *= 2
                grid[a-1][b] = 0

    for b in range(4):
        for a in range(3,0,-1):
            x = 1
            while grid[a][b] == 0:
                i = 1
                while a-i >=0:
                    grid[a-i+1][b]= grid[a-i][b]
                    grid[a-i][b] = 0
                    i += 1
                x += 1
                if x > 4:
                    break


def push_left(grid):
    for a in range(4):
        for b in range(3):
            x = 1
            while grid[a][b] == 0:
                i =1
                while b+i < 4:
                    grid[a][b+i-1] = grid[a][b+i]
                    grid[a][b+i] = 0
                    i +=1
                x += 1
                if x > 4:
                    break

    for a in range(4):
        for b in range(3):
            if grid[a][b] == grid[a][b+1]:
                grid[a][b] *= 2
                grid[a][b+1] = 0

    for a in range(4):
        for b in range(3):
            x =1
            while grid[a][b] == 0:
                i =1
                while b+i < 4:
                    grid[a][b+i-1] = grid[a][b+i]
                    grid[a][b+i] = 0
                    i +=1
                x += 1
                if x > 4:
                    break


def push_right(grid):
    for a in range(4):
        for b in range(3,0,-1):
            x = 1
            while grid[a][b] == 0:
                i =1
                while b-i >= 0:
                    grid[a][b-i+1] = grid[a][b-i]
                    grid[a][b-i] = 0
                    i +=1
                x += 1
                if x > 4:
                    break

    for a in range(4):
        for b in range(3,0,-1):
            if grid[a][b] == grid[a][b-1]:
                grid[a][b] *= 2
                grid[a][b-1] = 0

    for a in range(4):
        for b in range(3,0,-1):
            x =1
            while grid[a][b] == 0:
                i =1
                while b-i >= 0:
                    grid[a][b-i+1] = grid[a][b-i]
                    grid[a][b-i] = 0
                    i +=1
                x += 1
                if x > 4:
                    break