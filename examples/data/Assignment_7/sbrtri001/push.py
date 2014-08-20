''' Assignment 7, question 3
2048 game functions: this program makes use of modules in pushAdd.py
Tristan Subroyen
30 April 2014 '''

import pushAdd

def push_up (grid):
    ''' merge grid values upwards '''
    for i in range (4):
        pushAdd.shiftSpaceUp (i,grid)
        pushAdd.mergeValUp (i, grid)
        pushAdd.shiftSpaceUp (i, grid)
        
def push_down (grid):
    ''' merge grid values downwards '''
    for i in range (4):
        pushAdd.shiftSpaceDown (i, grid)
        pushAdd.mergeValDown (i, grid)
        pushAdd.shiftSpaceDown (i, grid)

def push_left (grid):
    ''' merge grid values left '''
    for j in range (4):
        pushAdd.shiftSpaceLeft (j, grid)
        pushAdd.mergeValLeft (j, grid)
        pushAdd.shiftSpaceLeft(j, grid)
        
def push_right (grid):
    ''' merge grid values right '''
    for j in range (4):
        pushAdd.shiftSpaceRight (j, grid)
        pushAdd.mergeValRight (j, grid)
        pushAdd.shiftSpaceRight (j, grid)