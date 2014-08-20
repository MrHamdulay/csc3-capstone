# Megan Swartz
# SWRMEG005 
# Assignment 7-Question 2

def create_grid(grid):
    for i in range(4): #create grid
        grid.append([0]*4)

def print_grid (grid):
    print ("+"+"-"*20+"+") #Print out grid in columns within a box
    for i in range(4):
        print ("|",end='')
        for s in range(4):
            if grid[i][s] == 0:
                print ("     ",end='')
            else:
                print (str(grid[i][s])+(" "*(5-len(str(grid[i][s])))),end='')
        print ("|")
    print ("+"+"-"*20+"+")
    
def check_lost (grid):
    same = 0
    zero = 0
    for i in range(3):
        for s in range(1,4):
            if grid[i][s] == grid[i][s-1] or grid[i][s] == grid[i+1][s]:
                same+=1
                break
   
    for i in range(4):
        if 0 in grid[i]:
            zero+=1
            break
    if same==0 and zero==0:
        return True
    else:
        return False
            
def check_won (grid):
    won = 0 #True or False
    for i in range(4):
            for s in range(4):
                if grid[i][s] >= 32:
                    won +=1
                    break
    if won == 0:
        return False
    else:
        return True
                
def copy_grid (grid):
    copy = [] #Return grid
    for i in range(4):
        copy.append([0]*4)
    for i in range(4):
        for s in range(4):
            copy[i][s] = grid[i][s]
    return copy

def grid_equal (grid1, grid2):
    #Return Boolean expression 
    if grid1 == grid2:
        return True
    else:
        return False