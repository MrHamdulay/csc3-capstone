#Assignment 7 - Question 3
#Module for 2048 game
#Aidan de Nobrega
#27/04/2014

def push_up (grid):
    """merge grid values upwards"""
    #comments in this function are applicable in further functions
    for i in range(4): #row
        for j in range(4):
            merged = False
            #column
            #iterates through each point
            #starts top left of grid, ends bottom right
            #if coord is white space(0), continues to next coord
            if grid[i][j] == 0:
                continue         
            else:
                spaceabove = True #flag
                attop = False #flag
                #as long as a number CAN move up...
                while spaceabove and not attop:
                    #t allows a number to move more than a single position
                    for t in range(1, 4): 
                        if i - t < 0: #is number against top?
                            attop = True
                        elif grid[i - t][j] != 0:#is there an empty spot above?
                            spaceabove = False
                            if not merged and grid[i - t][j] == grid[i - (t - 1)][j]:
                                grid[i - t][j] *= 2 #upper number doubles
                                grid[i - (t-1)][j] = 0
                                merged = True
                        else:
                            #number moves up until one of the flags drops
                            grid[i - t][j] = grid[i - (t - 1)][j]
                            grid[i - (t - 1)][j] = 0
                            
def push_down (grid):
    """merge grid values downwards"""
    #please read comments from push_up() function
    for i in range(3, -1, -1): 
        for j in range(4):
            merged = False
            #iteration starts bottom left of grid, ends top right
            if grid[i][j] == 0:
                continue
            else:
                spacebelow = True
                atbottom = False
                while spacebelow and not atbottom:
                    for t in range(1, 4):
                    #i + 1 in each case because looking at rows with greater index values, i.e, rows below
                        if i + t > 3:
                            atbottom = True
                        elif grid[i + t][j] != 0: 
                            spacebelow = False
                            if not merged and grid[i + t][j] == grid[i + (t-1)][j]:
                                grid[i + t][j] *= 2 #number below doubles 
                                grid[i + (t-1)][j] = 0 #number above becomes white space(0)  
                                merged = True
                        else:
                            grid[i + t][j] = grid[i + (t - 1)][j]
                            grid[i + (t - 1)][j] = 0

def push_left (grid):
    """merge grid values left"""
    #focus is on j(columns) rather than i(rows)
    for i in range(4):
        for j in range(4):
            merged = False
            if grid[i][j] == 0:
                continue
            else:
                spaceleft = True
                atleft = False
                while spaceleft and not atleft:
                    for t in range(1, 4):
                        #t is added/taken from j instead of i
                        if j - t < 0:
                            atleft = True
                        elif grid[i][j - t] != 0:
                            spaceleft = False
                            if not merged and grid[i][j - t] == grid[i][j - (t-1)]:
                                grid[i][j - t] *= 2
                                grid[i][j - (t-1)] = 0
                                merged = True
                        else:
                            grid[i][j - t] = grid[i][j - (t - 1)]
                            grid[i][j - (t - 1)] = 0   

def push_right (grid):
    """merge grid values right"""
    for i in range(4):
        for j in range(3, -1, -1):
            merged = False        
            if grid[i][j] == 0:
                continue
            else:
                spaceright = True
                atright = False
                while spaceright and not atright:
                    for t in range(1, 4):
                        if j + t > 3:
                            atright = True
                        elif grid[i][j + t] != 0:
                            spaceright = False
                            if not merged and grid[i][j + t] == grid[i][j + (t-1)]:
                                grid[i][j + t] *= 2
                                grid[i][j + (t-1)] = 0 
                                merged = True
                        else:
                            grid[i][j + t] = grid[i][j + (t - 1)]
                            grid[i][j + (t - 1)] = 0
                           