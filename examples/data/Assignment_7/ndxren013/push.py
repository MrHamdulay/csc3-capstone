def push_up (grid):
    """merge grid values upward"""

    for i in range (4):

        for j in range(4):

            if grid[i][j] == 0 :

                if i < 3:
                    grid[i][j] = grid[i+1][j]

            else:

                y = i

                while (y > 0 and grid[i][j] != 0):
                    y -= 1

                
                    

def push_down (grid):
    """merge grid values downward"""


def push_left(grid):
    """merge grid values left"""


def lush_right(grid):
    """merge grid values right""" 
