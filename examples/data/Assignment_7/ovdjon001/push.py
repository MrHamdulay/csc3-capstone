"""Assingment 7, question 3, push.py
by Jonathan Ovadia 
1 May 2014"""
def main():
    print( __name__)

def push_up (grid):
    """merge grid values upwards"""
    for i in range(3):
        for x in  range(4):
            for y in range(3):
                if grid[y][x] == 0:
                    grid[y][x] = grid[y+1][x]
                    grid[y+1][x] = 0
    for x in  range(4):
        for y in range(3):
            if grid[y][x] == grid[y+1][x]:
                grid[y][x] = grid[y][x]*2
                grid[y+1][x] = 0
    for i in range(3):
        for x in  range(4):
            for y in range(3):
                if grid[y][x] == 0:
                    grid[y][x] = grid[y+1][x]
                    grid[y+1][x] = 0


def push_down (grid):
    """merge grid values downwards"""
    for i in range(3):
        for x in  range(4):
            for y in range(1,4):
                if grid[y][x] == 0:
                    grid[y][x] = grid[y-1][x]
                    grid[y-1][x] = 0
    for x in  range(4):
        for y in range(1,4):
            if grid[y][x] == grid[y-1][x]:
                grid[y][x] = grid[y][x]*2
                grid[y-1][x] = 0
    for i in range(3):
        for x in  range(4):
            for y in range(1,4):
                if grid[y][x] == 0:
                    grid[y][x] = grid[y-1][x]
                    grid[y-1][x] = 0


def push_left (grid):
    """merge grid values left"""
    for i in range(3):
        for x in  range(3):
            for y in range(4):
                if grid[y][x] == 0:
                    grid[y][x] = grid[y][x+1]
                    grid[y][x+1] = 0
    for x in  range(3):
        for y in range(4):
            if grid[y][x] == grid[y][x+1]:
                grid[y][x] = grid[y][x]*2
                grid[y][x+1] = 0
    for i in range(3):
        for x in  range(3):
            for y in range(4):
                if grid[y][x] == 0:
                    grid[y][x] = grid[y][x+1]
                    grid[y][x+1] = 0

def push_right (grid):
    """merge grid values right"""
    for i in range(3):
        for x in  range(1,4):
            for y in range(4):
                if grid[y][x] == 0:
                    grid[y][x] = grid[y][x-1]
                    grid[y][x-1] = 0
    for x in  range(1,4):
        for y in range(4):
            if grid[y][x] == grid[y][x-1]:
                grid[y][x] = grid[y][x]*2
                grid[y][x-1] = 0
    for i in range(3):
        for x in  range(1,4):
            for y in range(4):
                if grid[y][x] == 0:
                    grid[y][x] = grid[y][x-1]
                    grid[y][x-1] = 0


if __name__ == "__main__":main()