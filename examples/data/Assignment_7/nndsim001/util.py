# This is a module called util.py and contains the six functions:

# create_grid(grid)
#       create a 2-d array
# print_grid (grid) 
#       prints a 2-d array
# check_lost (grid)
#       checks each row and column for equal adjacent values
# check_won (grid) 
#       checks if grid is full populated and if there is a number >= 32
# copy_grid (grid)
#       creates a copy of a 2-d array
# grid_equal (grid1, grid2) 
#       checks if two 2-d array's are equal

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 30 April 2014


def create_grid(grid):
    """create a 4x4 grid"""
    grit = grid #pass parameter to a local variable
    height = 4
    for i in range (height):
        grit.append ([0] * 4) #create 4 x 4 list
    return grit


def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    grit = grid #pass parameter to a local variable
    print("+--------------------+") #print top boarder
    for i in range(len(grit)):
        print("|",end='')
        for j in range(len(grit)):
            if grit[i][j] != 0:
                print("{0:<5}".format(grit[i][j]),end='')# dont' print zeros
            else:
                print("{0:<5}".format(" "),end='')# print the 2-d list
        print("|")
    print("+--------------------+") #print bottom boarder


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    grit = grid #pass parameter to local variable for manipulation
    
    # Search for a zero at any position of the grid
    for i in range(len(grit)):
        for j in range(len(grit)):
            if grit[i][j] == 0: #check every position for a zero
                return False
            
    # Horizontal search for equal adjacent values
    for i in range(len(grit)):
        for j in range(len(grit) - 1):
            if grit[i][j] == grit[i][j + 1]:
                return False #no 2 or more values equal in a row
    
    # Vertical search for for equal adjacent values
    for i in range(len(grit) - 1):
        for j in range(len(grit)):
            if grit[i][j] == grit[i+1][j]:
                return False #no 2 or more values equal in a column
    return True


def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    grit = grid # pass parameter to a local variable
    for i in range(len(grit)):
        for j in range(len(grit)):
            if grit[i][j] >= 32:
                return True #breakout of loop and return True
            else:
                continue #continue searching for numbers >= 32
    return False #return false if no such number if found


def copy_grid (grid):
    """return a copy of the grid"""
    grit1 = grid #pass parameter to local variable
    grit2 = [] #store a copy of the original grid here
    grit2 = create_grid(grit2) #initialize dummy grid with zeros
    for i in range(len(grit1)):
        for j in range(len(grit2)):
            grit2[i][j] = grit1[i][j] #copies original grid to dummy grid
    return grit2


def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    gri1, gri2 = grid1,grid2 #pass parameter to local variable
    yes = True
    
    for i in range(len(gri1)):
        for j in range(len(gri2)):
            if gri1[i][j] != gri2[i][j]:
                yes = False
                return False #break out of loop if a mismatch is found
            else:
                yes = True #continue checking if the items match
                continue
    return yes


#Sample I/O:
# 2
# +--------------------+
# |2         2         |
# |     4         8    |
# |     16        128  |
# |2    2    2    2    |
# +--------------------+

#Sample I/O:
# 7
# True

#Sample I/O:
# 9
# True

#Sample I/O:
# 17
# 4 4
# 16 16
# 2 2
# 64 4
# 64 16
# 64 2

#Sample I/O:
# 18
# True