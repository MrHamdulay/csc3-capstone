#Shaylan Lalloo
#LlLSHA008
#Pushes grid in directions

def push_up (grid):
    changed = []
    for i in range(4):
        changed.append([False,] * 4)
    #Makes a change grid so that a block doesn't merge multiple times
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                continue
            #Don't move 0's
            k = i
            #row of block to move
            tmp = grid[i][j]
            #store the value of the place
            grid[i][j] = 0
            #make current place 0. Useful to shorten code
            while k > 0 and grid[k][j] == 0:
                k -= 1
                #keep going up until you reach end of grid or another number
            if grid[k][j] == tmp and changed[k][j] == False:
                #if the above number is the same and that block hasn't already merged with something, then merge it
                grid[k][j] *= 2
                changed[k][j] = True
                #mark the block as having been changed
                continue
            if grid[k][j] != 0:
                #will occure when it hit a block, then the current block should be at the one below it
                k += 1
            #change the location stored to the correct number
            grid[k][j] = tmp


#copied the push up but used similarity by just altering the loop and a few lines
def push_down(grid):
    changed = []
    for i in range(4):
        changed.append([False,] * 4)
    for i in range(3, -1, -1):
        #needs to be checked bottom up
        for j in range(4):
            if grid[i][j] == 0:
                continue
            k = i
            tmp = grid[i][j]
            grid[i][j] = 0
            while k < 3 and grid[k][j] == 0:
                k += 1
                #instead of decrease, an increase occurs
            if grid[k][j] == tmp and changed[k][j] == False:
                grid[k][j] *= 2
                changed[k][j] = True
                continue
            if grid[k][j] != 0:
                #instead of increase, a decrease occurs
                k -= 1
            grid[k][j] = tmp


#again using similarity
def push_left(grid):
    changed = []
    for i in range(4):
        changed.append([False,] * 4)
    #swapped i and j to allow for direction change
    for j in range(4):
        for i in range(4):
            if grid[j][i] == 0:
                continue
            k = i
            tmp = grid[j][i]
            grid[j][i] = 0
            while k > 0 and grid[j][k] == 0:
                k -= 1
            if grid[j][k] == tmp and changed[j][k] == False:
                grid[j][k] *= 2
                changed[j][k] = True
                continue
            if grid[j][k] != 0:
                k += 1
            grid[j][k] = tmp

#similarly reflect like push down was to push up
def push_right(grid):
    changed = []
    for i in range(4):
        changed.append([False,] * 4)
    for j in range(3, -1, -1):
        for i in range(3, -1, -1):
            if grid[j][i] == 0:
                continue
            k = i
            tmp = grid[j][i]
            grid[j][i] = 0
            while k < 3 and grid[j][k] == 0:
                k += 1
            if grid[j][k] == tmp and changed[j][k] == False:
                grid[j][k] *= 2
                changed[j][k] = True
                continue
            if grid[j][k] != 0:
                k -= 1
            grid[j][k] = tmp


#Testing code below

##
##mygrid = [[0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 2, 0]]
##
##for i in mygrid:
##    print(i)
##
##print()
##
##push_right(mygrid)
##
##for i in mygrid:
##    print(i)
