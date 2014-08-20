"""Daniel Schwartz
SCHDAN037
push module for question 3
april 2014"""


def push_up(grid):
    """merge grid values upwards"""
    #push all blocks into empty spaces
    for loop in range(3):   # 3 because thats the most it will go up
        for row in range(4):
            for col in range(4):
                #dont look at top row, unmovable
                if row != 0:
                    #dont look at empty places
                    if grid[row][col] != 0:
                        #if space above is empty, move there
                        if grid[row - 1][col] == 0:
                            grid[row - 1][col] = grid[row][col]
                            grid[row][col] = 0
    # once all blocks moved up into empty spaces
    # double all the same blocks together going upward
    # this is done separately to make sure to only double once per move
    for row in range(4):
        for col in range(4):
            if row != 0:  # ignore bottom row
                if grid[row - 1][col] == grid[row][col]:
                    #if two blocks are same double and move downward
                    grid[row - 1][col] *= 2
                    grid[row][col] = 0

    # after doubling there are still possible spaces left open that shouldnt be there
    # so do the up pushing again once
    for row in range(4):
        for col in range(4):
            #dont look at top row, unmovable
            if row != 0:
                #dont look at empty places
                if grid[row][col] != 0:
                    #if space above is empty, move there
                    if grid[row - 1][col] == 0:
                        grid[row - 1][col] = grid[row][col]
                        grid[row][col] = 0


def push_down(grid):
    """merge grid values downwards"""
    #push all blocks into empty spaces
    for loop in range(3):   # 3 because thats the most it will go down
        for row in range(4):
            for col in range(4):
                #dont look at bottom row, unmovable
                if row != 3:
                    #dont look at empty places
                    if grid[row][col] != 0:
                        #if space bellow is empty, move there
                        if grid[row + 1][col] == 0:
                            grid[row + 1][col] = grid[row][col]
                            grid[row][col] = 0
    # once all blocks moved down into empty spaces
    # double all the same blocks together going downward
    # this is done separately to make sure to only double once per move
    # when doubling downward, check from the bottom upwards not from the top
    # this prevents double merging in one move
    for row in range(3, -1, -1):
        for col in range(3, -1, -1):
            if row != 3:  # ignore bottom row
                if grid[row + 1][col] == grid[row][col]:
                    #if two blocks are same double and move downward
                    grid[row + 1][col] *= 2
                    grid[row][col] = 0

    # after doubling there are still possible spaces left open that shouldnt be there
    # so do the down pushing again once
    for row in range(4):
        for col in range(4):
            #dont look at bottom row, unmovable
            if row != 3:
                #dont look at empty places
                if grid[row][col] != 0:
                    #if space bellow is empty, move there
                    if grid[row + 1][col] == 0:
                        grid[row + 1][col] = grid[row][col]
                        grid[row][col] = 0


def push_left(grid):
    """merge grid values left"""
    #push all blocks into empty spaces
    for loop in range(3):   # 3 because thats the most it will go left
        for row in range(4):
            for col in range(4):
                #dont look at left col, unmovable
                if col != 0:
                    #dont look at empty places
                    if grid[row][col] != 0:
                        #if space to the left is empty, move there
                        if grid[row][col - 1] == 0:
                            grid[row][col - 1] = grid[row][col]
                            grid[row][col] = 0
    # once all blocks moved left into empty spaces
    # double all the same blocks together going left
    # this is done separately to make sure to only double once per move
    for row in range(4):
        for col in range(4):
            if col != 0:  # ignore left col
                if grid[row][col-1] == grid[row][col]:
                    #if two blocks are same double and move left
                    grid[row][col - 1] *= 2
                    grid[row][col] = 0

    # after doubling there are still possible spaces left open that shouldnt be there
    # so do the left pushing again once
    for row in range(4):
        for col in range(4):
            #dont look at left col, unmovable
            if col != 0:
                #dont look at empty places
                if grid[row][col] != 0:
                    #if space to the left is empty, move there
                    if grid[row][col - 1] == 0:
                        grid[row][col - 1] = grid[row][col]
                        grid[row][col] = 0


def push_right(grid):
    """merge grid values right"""
    #push all blocks into empty spaces
    for loop in range(3):   # 3 because thats the most it will go left
        for row in range(4):
            for col in range(4):
                #dont look at right col, unmovable
                if col != 3:
                    #dont look at empty places
                    if grid[row][col] != 0:
                        #if space to the left is empty, move there
                        if grid[row][col + 1] == 0:
                            grid[row][col + 1] = grid[row][col]
                            grid[row][col] = 0
    # once all blocks moved right into empty spaces
    # double all the same blocks together going right
    # this is done separately to make sure to only double once per move
    # when doubling from the right, check from the bottom upwards not from the top
    # this prevents double merging in one move
    for row in range(3, -1, -1):
        for col in range(3, -1, -1):
            if col != 3:  # ignore right col
                if grid[row][col + 1] == grid[row][col]:
                    #if two blocks are same double and move right
                    grid[row][col + 1] *= 2
                    grid[row][col] = 0
    # after doubling there are still possible spaces left open that shouldnt be there
    # so do the right pushing again once
    for row in range(4):
        for col in range(4):
            #dont look at right col, unmovable
            if col != 3:
                #dont look at empty places
                if grid[row][col] != 0:
                    #if space to the left is empty, move there
                    if grid[row][col + 1] == 0:
                        grid[row][col + 1] = grid[row][col]
                        grid[row][col] = 0