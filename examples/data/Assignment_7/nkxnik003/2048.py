#NIkhil Jiten Naik
#NKXNIK003 
#ComSci Assignment 7
#2048

import random
import util
import push

def add_block (grid):

    options = [2,2,2,2,2,4]
    chosen = options[random.randint(0,len(options)-1)]
    found = False
    while (not found):
        x = random.randint (0, 3)
        y = random.randint (0, 3)
        if (grid[x][y] == 0):
            grid[x][y] = chosen
            found = True

def play ():
    
    grid = []
    util.create_grid (grid)
    add_block (grid)
    add_block (grid)
    won_message = False
    while (True):
        util.print_grid (grid)
        key = input ("Enter a direction:\n")
        if (key in ['x', 'u', 'd', 'l', 'r']):
            saved_grid = util.copy_grid (grid)
            if (key == 'x'):
                return
            elif (key == 'u'):
                push.push_up (grid)
            elif (key == 'd'):
                push.push_down (grid)
            elif (key == 'r'):
                push.push_right (grid)
            elif (key == 'l'):
                push.push_left (grid)
            if util.check_lost (grid):
                print ("Game Over!")
                return
            elif util.check_won (grid) and not won_message:
                print ("Won!")
                won_message = True  
            if not util.grid_equal (saved_grid, grid):
                add_block (grid)

random.seed (12)
play ()
