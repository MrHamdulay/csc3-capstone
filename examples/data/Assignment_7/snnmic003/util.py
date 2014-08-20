#Question 2 Assignment 7, Manipulate 2-D arrays
# Michael Sanne
# 2014/05/01

def create_grid(grid):
    #create a 4x4 grid
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    for i in range (4):
        x1.append(0)
        x2.append(0)
        x3.append(0)    
        x4.append(0)    
    
    grid.append(x1)
    grid.append(x2)
    grid.append(x3)
    grid.append(x4)
   
#Prints grid with 0 as empty spaces and a column width of 5
def print_grid (grid):
    print ("+" + 20*("-") + "+")
    for j in range (len(grid)):
        print ("|", end ="")
        for i in range (len(grid[j])):
            if (grid[j][i] != 0):
                print ("{0:<5}".format(grid[j][i]), end = "")
            else:
                print (5*" ", end = "")
        print ("|")
    print ("+" + 20*("-") + "+")
#Determines if player has lost yet 
def check_lost (grid):
    lost = True
    for j in range (len(grid)):
        for i in range (len(grid[j])):
            if (grid [j][i] == 0):
                lost = False
                break
            elif (j<len(grid) -1 and j>0 and i<(len(grid[j])-1) and i>0):
                if (grid[j][i] == grid[j][i+1]):
                    lost = False
                    break
                elif (grid [j][i] == grid[j][i-1]):
                    lost = False
                    break
                elif (grid[j][i] == grid[j+1][i]):
                    lost = False
                    break
                elif (grid [j][i] == grid[j-1][i]):
                    lost = False
                    break
                
                elif (grid [j][i-1] == grid[j+1][i-1]):
                    lost = False
                    break
                elif (grid [j][i-1] == grid[j-1][i-1]):
                    lost = False
                    break
                elif (grid [j][i+1] == grid[j+1][i+1]):
                    lost = False
                    break
                elif (grid [j][i+1] == grid[j-1][i+1]):
                    lost = False
                    break
                
                elif (grid [j-1][i] == grid[j-1][i+1]):
                    lost = False
                    break
                elif (grid [j-1][i] == grid[j-1][i-1]):
                    lost = False
                    break
                elif (grid [j+1][i] == grid[j+1][i+1]):
                    lost = False
                    break
                elif (grid [j+1][i] == grid[j+1][i-1]):
                    lost = False
                    break
        if lost == False:
                break
    return lost
#Determines whether player has won the game
def check_won (grid):
    won = False
    for j in range (len(grid)):
        for i in range (len (grid[j])):
            if (grid[j][i] >=32):
                won = True
                break
        if won == True:
            break
    return won

#Creates a copy of the grid
def copy_grid (grid):
    test_Grid = []
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    for i in range (len(grid[0])):
        x1.append(grid[0][i])
        x2.append(grid[1][i])
        x3.append(grid[2][i])    
        x4.append(grid[3][i])    
    
    test_Grid.append(x1)
    test_Grid.append(x2)
    test_Grid.append(x3)
    test_Grid.append(x4)
    return test_Grid

#Checks if the grid 1 is identical to grid2
def grid_equal (grid1, grid2):
    equal = True
    if (len(grid1) == len(grid2)):
        for j in range (len(grid1)):
            if (len(grid1[j]) == len (grid2[j])):
                for i in range (len(grid1[j])):
                    if (grid1[j][i] != grid2[j][i]):
                        equal = False
                        break
                if equal == False:
                    break
            else:
                equal = False
    else:
        equal = False
    return equal