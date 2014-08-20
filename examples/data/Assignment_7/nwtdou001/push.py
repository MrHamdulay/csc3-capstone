'''push.py
defines the push functions for 2048
douglas newton
29 april 2014'''

'''
{
{0, 0, 0, 0},
{0, 0, 0, 0},
{0, 0, 0, 0},
{0, 0, 0, 0},
}
'''

# {0,0,0,0}
# pushing towards the beginning of the line
# 0020
#

def shift(line,i):
    for j in range(i,3):
        line[j] = line[j+1]
        line[j+1] = 0

def remove_gaps(line):
    for i in range(3,-1,-1):
        # if there is a gap
        if line[i]==0:
            # then shift each element after the gap towards the beginning
            shift(line,i)
        
def push(line):
    remove_gaps(line)
    for i in range(3):
        # check for 'twin values' from the beginning
        if line[i]==line[i+1]:
            # double the first value in the pair, 'remove' the second (set to 0)
            line[i] *= 2
            line[i+1] = 0
    # then remove gaps again - since the pairing could have made more gaps
    remove_gaps(line)
#-----------------

def push_left(grid):
    for row in grid:
        push(row)

def push_right(grid):
    for row in grid:
        line = [0]*4
        for i in range(4):
            line[i] = row[3-i]
        push(line)
        for i in range(4):
            row[i] = line[3-i]

def push_up(grid):
    for i in range(4):
        line = [0]*4
        for j in range(4):
            line[j] = grid[j][i]
        push(line)
        for j in range(4):
            grid[j][i] = line[j]

def push_down(grid):
    for i in range(4):
        line = [0]*4
        for j in range(3,-1,-1):
            line[3-j] = grid[j][i]
        push(line)
        for j in range(3,-1,-1):
            grid[3-j][i] = line[j]

#-----------------

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x],end=',')
        print()